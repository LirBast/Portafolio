import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns


# 3. Evaluación de un modelo de clasificación (5 puntos) 
# • Datos de clasificación: Utiliza el conjunto de datos proporcionado para evaluar un modelo 
# de clasificación que predice si un cliente comprará o no un producto en función de 
# características como la edad, el ingreso y el historial de compras.

df= pd.read_csv(r'C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 6\clase 6\datos_clasificacion.csv')

print(df.head())

# Exploración inicial de los datos
print(df)       # Mostrar las primeras filas para ver la estructura
print(df.shape)
print('\n' + '='*80 + '\n')
print(df.info())       # Información general: tipos de datos y valores nulos
print('\n' + '='*80 + '\n')
print(df.describe())   # Estadísticas descriptivas básicas
print('\n' + '='*80 + '\n')
print('Cantidad de datos nulos')
print(df.isnull().sum())
print('\n' + '='*80 + '\n') # Cantidad de datos nulos


# Variables
X = df.drop('Comprara', axis=1)  # Todas las columnas excepto la variable objetivo
y = df['Comprara']

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalado de los datos
scaler = StandardScaler()

# Ajustar el escalador SOLO con los datos de entrenamiento y transformar ambos conjuntos
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Convertir de nuevo a DataFrame para mantener los nombres de las columnas
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

# Modelo de regresión logística
log_reg_scaled = LogisticRegression(max_iter=1000, random_state=42)
log_reg_scaled.fit(X_train_scaled, y_train)

# Predicciones
y_pred_scaled = log_reg_scaled.predict(X_test_scaled)
y_proba_scaled = log_reg_scaled.predict_proba(X_test_scaled)

matriz = confusion_matrix(y_test, y_pred_scaled)


plt.figure(figsize=(5,4))
sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues', xticklabels=['No Compra', 'Compra'], yticklabels=['No Compra', 'Compra'])
plt.xlabel('Predicción')
plt.ylabel('Valor Real')
plt.title('Matriz de Confusión')
plt.show()


accuraci = accuracy_score(y_test, y_pred_scaled)

print('\n' + '='*80 + '\n')
print('Resultados del modelo de regresión logística')
print(f'Accuracy: {accuraci:.4f}')
print(f'Matriz de confusión: {matriz}')
print('\n' + '='*80 + '\n')
print('Reporte de Clasificación completo:')
print(classification_report(y_test, y_pred_scaled, digits=4))
print('\n' + '='*80 + '\n')


y_scores = y_proba_scaled[:, 1]  # Prob. clase positiva
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
auc_score = roc_auc_score(y_test, y_scores)

plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, color='blue', label=f'AUC = {auc_score:.2f}')
plt.plot([0,1], [0,1], color='red', linestyle='--')
plt.xlabel("Tasa de Falsos Positivos (1 - Especificidad)")
plt.ylabel("Tasa de Verdaderos Positivos (Sensibilidad)")
plt.title("Curva ROC")
plt.legend()
plt.show()