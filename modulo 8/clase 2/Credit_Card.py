# Importación de librerías necesarias para el análisis de datos, modelado y visualización
import os
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, r2_score, precision_score, f1_score, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# Descarga del conjunto de datos de fraudes en tarjetas de crédito desde Kaggle
path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")

# Ruta al archivo CSV del dataset
dataset_path = os.path.join(path, 'creditcard.csv')

# Carga del dataset en un DataFrame de pandas con manejo de errores
try:
    df = pd.read_csv(dataset_path)
    print('El Dataset cargado exitosamente')
except FileNotFoundError:
    print(f'Error: el archivo "{dataset_path}" no se encontro')

# Análisis de la distribución de clases (fraude vs no fraude)
print('Conteo de Clases')
class_counts = df['Class'].value_counts()
print(class_counts)

# Cálculo de porcentajes de transacciones fraudulentas y no fraudulentas
total_transacciones = len(df)
porcentaje_fraude = (class_counts[1] / total_transacciones) * 100
porcentaje_no_fraude = (class_counts[0] / total_transacciones) * 100
print(f'Porcentaje de transacciones fraudulentas: {porcentaje_fraude:.4f}%')
print(f'Porcentaje de transacciones no fraudulentas: {porcentaje_no_fraude:.4f}%')

# Visualización de la distribución de clases (fraude vs no fraude)
plt.figure(figsize=(8, 6))
sns.countplot(x='Class', data=df)
plt.title('Distribución de Clases')
plt.xlabel('Clase (0: No Fraude, 1: Fraude)')
plt.ylabel('Numero de transacciones')
plt.xticks([0, 1], ['No Fraude', 'Fraude'])
plt.show()

# Separación de características (X) y etiqueta objetivo (y)
X = df.drop('Class', axis=1)
y = df['Class']

# Escalado de las columnas Time y Amount para normalizar su rango
scaler = StandardScaler()
X['Time'] = scaler.fit_transform(X[['Time']])     # Normaliza la columna Time
X['Amount'] = scaler.fit_transform(X[['Amount']]) # Normaliza la columna Amount

# Mostrar las primeras filas de X para verificar los cambios
print(X.head())

# División en conjuntos de entrenamiento y prueba
# stratify=y asegura que la proporción de clases se mantenga en ambos conjuntos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Mostrar la distribución de clases en entrenamiento y prueba (proporciones)
print(f'Clase de entrenamiento: \n {y_train.value_counts(normalize=True)} ')
print(f'Clase de prueba: \n {y_test.value_counts(normalize=True)}')

# Definición de pesos de clase para abordar el desbalance (aumenta la importancia de la clase minoritaria)
# Aquí se da mucho más peso a la clase 1 (fraude) para que el modelo preste más atención a esos ejemplos
class_weight = {0: 1, 1: 50}

# Número de características de entrada para la construcción del modelo
input_dim = X_train.shape[1]
print(f'Numero de caracteristicas de entrada: {input_dim}')

# Construcción del modelo de red neuronal
modelo = Sequential()
modelo.add(Dense(64, input_dim=input_dim, activation='relu'))
modelo.add(Dropout(0.5))
modelo.add(Dense(32, activation='relu'))
modelo.add(Dropout(0.5))
modelo.add(Dense(1, activation='sigmoid'))

# Compilación del modelo con optimizador Adam, función de pérdida binaria y métrica de precisión
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print('\nResumen de la arquitectura del modelo\n')
modelo.summary()

# Configuración del callback EarlyStopping para detener el entrenamiento cuando la pérdida de validación deja de mejorar
# Se detiene si no hay mejora en 10 épocas consecutivas y restaura los mejores pesos del modelo
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Entrenamiento del modelo con los datos de entrenamiento y validación
# Se utilizan 50 épocas, tamaño de lote 32, y se aplican pesos de clase para manejar el desbalance
history = modelo.fit(
    X_train, y_train, 
    epochs=50, 
    batch_size=32, 
    validation_data=(X_test, y_test), 
    class_weight=class_weight, 
    callbacks=[early_stopping]
)

# Evaluación del modelo en el conjunto de prueba
loss, accuracy = modelo.evaluate(X_test, y_test, verbose=0)
print(f'Perdida(loss): {loss:.4f}')
print(f'Precisión(accuracy): {accuracy:.4f}')

# Predicción de probabilidades y conversión a etiquetas binarias (0 o 1)
y_pred_proba = modelo.predict(X_test)
y_prediction = (y_pred_proba > 0.5).astype('int64')

# Cálculo y visualización de la matriz de confusión
confusion_matrix_result = confusion_matrix(y_test, y_prediction)
print('Matriz de confusion')
print(confusion_matrix_result)

# Visualización gráfica de la matriz de confusión
plt.figure(figsize=(8, 6))
sns.heatmap(
    confusion_matrix_result, 
    annot=True, 
    fmt='d', 
    cmap='Blues', 
    xticklabels=['No fraude','Fraude'], 
    yticklabels=['No fraude','Fraude']
)
plt.show()

# Impresión del reporte de clasificación con métricas detalladas por clase
print(classification_report(y_test, y_prediction, target_names=['No fraude','Fraude']))

# Gráfico de la pérdida (loss) durante el entrenamiento
plt.figure(figsize=(12, 6))
plt.plot(history.history['loss'], label='Perdida (Entrenamiento)')
plt.title('Curvas de perdidas del modelo')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.legend()
plt.show()

# Gráfico de la precisión (accuracy) para entrenamiento y validación
plt.figure(figsize=(12, 6))
plt.plot(history.history['accuracy'], label='Precision (Entrenamiento)')
plt.plot(history.history['val_accuracy'], label='Precision de validacion')
plt.title('Curvas de precision del modelo')
plt.xlabel('Épocas')
plt.ylabel('Precision')
plt.legend()
plt.show()

# Construcción de una transacción "simulada" basada en las medias de las transacciones fraudulentas
# Se calcula la media de cada característica usando solo las filas con Class == 1 (fraude)
transaccion_fraudulenta = {
    'Time': np.mean(df[df['Class'] == 1]['Time']),
    'V1': np.mean(df[df['Class'] == 1]['V1']),
    'V2': np.mean(df[df['Class'] == 1]['V2']),
    'V3': np.mean(df[df['Class'] == 1]['V3']),
    'V4': np.mean(df[df['Class'] == 1]['V4']),
    'V5': np.mean(df[df['Class'] == 1]['V5']),
    'V6': np.mean(df[df['Class'] == 1]['V6']),
    'V7': np.mean(df[df['Class'] == 1]['V7']),
    'V8': np.mean(df[df['Class'] == 1]['V8']),
    'V9': np.mean(df[df['Class'] == 1]['V9']),
    'V10': np.mean(df[df['Class'] == 1]['V10']),
    'V11': np.mean(df[df['Class'] == 1]['V11']),
    'V12': np.mean(df[df['Class'] == 1]['V12']),
    'V13': np.mean(df[df['Class'] == 1]['V13']),
    'V14': np.mean(df[df['Class'] == 1]['V14']),
    'V15': np.mean(df[df['Class'] == 1]['V15']),
    'V16': np.mean(df[df['Class'] == 1]['V16']),
    'V17': np.mean(df[df['Class'] == 1]['V17']),
    'V18': np.mean(df[df['Class'] == 1]['V18']),
    'V19': np.mean(df[df['Class'] == 1]['V19']),
    'V20': np.mean(df[df['Class'] == 1]['V20']),
    'V21': np.mean(df[df['Class'] == 1]['V21']),
    'V22': np.mean(df[df['Class'] == 1]['V22']),
    'V23': np.mean(df[df['Class'] == 1]['V23']),
    'V24': np.mean(df[df['Class'] == 1]['V24']),
    'V25': np.mean(df[df['Class'] == 1]['V25']),
    'V26': np.mean(df[df['Class'] == 1]['V26']),
    'V27': np.mean(df[df['Class'] == 1]['V27']),
    'V28': np.mean(df[df['Class'] == 1]['V28']),
    'Amount': np.mean(df[df['Class'] == 1]['Amount'])
}

# Crear DataFrame de una sola fila con la transacción simulada
nueva_transaccion_df = pd.DataFrame([transaccion_fraudulenta])

# Escalado de las columnas Time y Amount para que estén en la misma escala que los datos de entrada
# Nota: aquí se vuelve a ajustar el escalador con el ejemplo nuevo (fit_transform).
# En producción sería mejor usar el scaler entrenado previamente (ej. saved_scaler.transform).
nueva_transaccion_df['Time'] = scaler.fit_transform(nueva_transaccion_df[['Time']])
nueva_transaccion_df['Amount'] = scaler.fit_transform(nueva_transaccion_df[['Amount']])

# Predicción de la probabilidad de fraude y conversión a clase binaria usando un umbral
prediccion_proba = modelo.predict(nueva_transaccion_df)
# Se usa un umbral de 0.05 (más sensible) para decidir si es fraude; ajustar según el balance FPR/TPR deseado
prediccion_class = (prediccion_proba > 0.05).astype('int64')

print('\nPrediccion de una transaccion simulada\n')
print(f'Probabilidad de fraude: {prediccion_proba[0][0]:.4f}')

# Interpretación de la predicción
if prediccion_class[0][0] == 1:
    print('El modelo predice que la transaccion es fraudulenta')
else:
    print('El modelo predice que la transaccion es legitima')


# Librerías para ajuste de hiperparámetros (hyperparameter tuning):
 
# -Optuna https://optuna.org/?spm=a2ty_o01.29997173.0.0.56c0c921uIEXb4
 
# -Keras Tuner https://keras.io/keras_tuner/?spm=a2ty_o01.29997173.0.0.56c0c921uIEXb4