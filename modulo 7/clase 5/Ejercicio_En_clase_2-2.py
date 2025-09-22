import kagglehub
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

print("="*80)
print("ETAPA 1: DESCARGA Y CARGA DEL DATASET")
print("="*80)

# Download latest version
print("Descargando dataset desde Kaggle...")
path = kagglehub.dataset_download("fedesoriano/heart-failure-prediction")
print(f"✓ Dataset descargado exitosamente")
print(f"Path to dataset files: {path}")

print("\nVerificando archivos disponibles...")
archivos = os.listdir(path)
print(f"Archivos disponibles: {archivos}")

# Cargar el dataset
dataset_path = os.path.join(path, 'heart.csv')
print(f"\nCargando dataset desde: {dataset_path}")
df = pd.read_csv(dataset_path)
print(f"✓ Dataset cargado exitosamente con {df.shape[0]} filas y {df.shape[1]} columnas")

print("\n" + "="*80)
print("ETAPA 2: EXPLORACIÓN INICIAL DE LOS DATOS")
print("="*80)

print("Primeras 5 filas del dataset:")
print(df.head())

print('\n' + '-'*50)
print("INFORMACIÓN GENERAL DEL DATASET:")
print('-'*50)
print(df.info())

print('\n' + '-'*50)
print("ESTADÍSTICAS DESCRIPTIVAS:")
print('-'*50)
print(df.describe())

print('\n' + '-'*50)
print("VALORES NULOS POR COLUMNA:")
print('-'*50)
print(df.isnull().sum())

print('\n' + '-'*50)
print("DISTRIBUCIÓN DE LA VARIABLE OBJETIVO (HeartDisease):")
print('-'*50)
print(df['HeartDisease'].value_counts())
print(f"Porcentaje de casos positivos: {(df['HeartDisease'].sum() / len(df)) * 100:.2f}%")

print("\n" + "="*80)
print("ETAPA 3: PREPROCESAMIENTO DE DATOS")
print("="*80)

print("Identificando columnas categóricas...")
columns_categoricas = df.select_dtypes(include='object').columns.to_list()
print(f"Columnas categóricas encontradas: {columns_categoricas}")

if columns_categoricas:
    print(f"\nAplicando codificación One-Hot a {len(columns_categoricas)} columnas categóricas...")
    print("Nota: Se usa drop_first=True para evitar multicolinealidad")
    df_procesado = pd.get_dummies(df, columns=columns_categoricas, drop_first=True)
    print(f"✓ Codificación completada. Nuevas dimensiones: {df_procesado.shape}")
else:
    print("No se encontraron columnas categóricas para procesar")
    df_procesado = df.copy()

print(f"\nColumnas después del preprocesamiento:")
print(df_procesado.columns.tolist())

print("\nPrimeras 5 filas del dataset procesado:")
print(df_procesado.head())

print("\n" + "="*80)
print("ETAPA 4: DIVISIÓN DEL DATASET")
print("="*80)

print("Separando variables independientes (X) y dependiente (y)...")
X = df_procesado.drop('HeartDisease', axis=1)  # Variables independientes
y = df_procesado['HeartDisease']  # Variable objetivo

print(f"✓ Variables independientes (X): {X.shape[1]} características")
print(f"✓ Variable objetivo (y): {len(y)} muestras")

print(f"\nDividiendo dataset en conjuntos de entrenamiento (80%) y prueba (20%)...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"✓ División completada:")
print(f"  - Conjunto de entrenamiento: {X_train.shape[0]} muestras, {X_train.shape[1]} características")
print(f"  - Conjunto de prueba: {X_test.shape[0]} muestras, {X_test.shape[1]} características")
print(f"  - Distribución en entrenamiento: {y_train.value_counts().to_dict()}")
print(f"  - Distribución en prueba: {y_test.value_counts().to_dict()}")

print("\n" + "="*80)
print("ETAPA 5: ENTRENAMIENTO DEL MODELO")
print("="*80)

print("Inicializando modelo de Regresión Logística...")
print("Parámetros: max_iter=1000 (para asegurar convergencia)")
modelo_logistico = LogisticRegression(max_iter=1000, random_state=42)

print("Entrenando modelo con datos de entrenamiento...")
modelo_logistico.fit(X_train, y_train)
print("✓ Modelo entrenado exitosamente")

print(f"\nCoeficientes del modelo (primeros 10):")
coeficientes = pd.DataFrame({
    'Característica': X.columns[:10],
    'Coeficiente': modelo_logistico.coef_[0][:10]
}).sort_values('Coeficiente', key=abs, ascending=False)
print(coeficientes)

print("\n" + "="*80)
print("ETAPA 6: PREDICCIONES Y EVALUACIÓN")
print("="*80)

print("Realizando predicciones en conjunto de prueba...")
y_pred = modelo_logistico.predict(X_test)
y_pred_proba = modelo_logistico.predict_proba(X_test)[:, 1]
print("✓ Predicciones completadas")

print(f"\nDistribución de predicciones:")
unique, counts = pd.Series(y_pred).value_counts().sort_index().items()
for val, count in zip(unique, counts):
    print(f"  - Clase {val}: {count} predicciones ({count/len(y_pred)*100:.1f}%)")

print("\n" + "-"*50)
print("MÉTRICAS DE EVALUACIÓN:")
print("-"*50)

# Precisión (Accuracy)
precision = accuracy_score(y_test, y_pred)
print(f"Precisión (Accuracy): {precision:.4f} ({precision*100:.2f}%)")
print("  → Porcentaje de predicciones correctas")

# Matriz de confusión
print(f"\nMatriz de Confusión:")
matriz_confusion = confusion_matrix(y_test, y_pred)
print(matriz_confusion)
print("  → Filas: Valores reales | Columnas: Predicciones")
print(f"  → Verdaderos Negativos: {matriz_confusion[0,0]}")
print(f"  → Falsos Positivos: {matriz_confusion[0,1]}")
print(f"  → Falsos Negativos: {matriz_confusion[1,0]}")
print(f"  → Verdaderos Positivos: {matriz_confusion[1,1]}")

# Reporte de clasificación detallado
print(f"\nReporte de Clasificación Detallado:")
reporte_clasificacion = classification_report(y_test, y_pred)
print(reporte_clasificacion)

# AUC-ROC
auc = roc_auc_score(y_test, y_pred_proba)
print(f"AUC (Área bajo la curva ROC): {auc:.4f}")
print(f"  → Interpretación: {auc*100:.1f}% de probabilidad de distinguir correctamente")
print(f"    entre un paciente sano y uno con enfermedad cardíaca")

if auc >= 0.9:
    interpretacion = "Excelente"
elif auc >= 0.8:
    interpretacion = "Bueno"
elif auc >= 0.7:
    interpretacion = "Aceptable"
else:
    interpretacion = "Pobre"
print(f"  → Calificación del modelo: {interpretacion}")

print("\n" + "="*80)
print("ETAPA 7: VISUALIZACIÓN DE RESULTADOS")
print("="*80)

print("Generando curva ROC...")
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

plt.figure(figsize=(10, 8))
plt.plot(fpr, tpr, label=f'Modelo Logístico (AUC = {auc:.3f})', linewidth=2, color='blue')
plt.plot([0, 1], [0, 1], 'k--', label='Modelo Aleatorio (AUC = 0.5)', linewidth=1)
plt.fill_between(fpr, tpr, alpha=0.2, color='blue')

plt.xlabel('Tasa de Falsos Positivos (FPR)', fontsize=12)
plt.ylabel('Tasa de Verdaderos Positivos (TPR)', fontsize=12)
plt.title('Curva ROC - Predicción de Enfermedad Cardíaca', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Añadir texto explicativo
plt.text(0.6, 0.2, f'Mejor que aleatorio\nsi AUC > 0.5\n\nNuestro modelo:\nAUC = {auc:.3f}', 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7),
         fontsize=10)

print("✓ Gráfica generada exitosamente")
plt.show()

print("\n" + "="*80)
print("RESUMEN FINAL DEL ANÁLISIS")
print("="*80)
print(f"📊 Dataset: {df.shape[0]} muestras, {df.shape[1]} características originales")
print(f"🔄 Preprocesamiento: {df_procesado.shape[1]} características después de codificación")
print(f"📈 Modelo: Regresión Logística")
print(f"🎯 Precisión: {precision:.1%}")
print(f"📉 AUC-ROC: {auc:.3f} ({interpretacion})")
print(f"✅ El modelo {'tiene un buen rendimiento' if auc >= 0.8 else 'necesita mejoras'} para predecir enfermedad cardíaca")
print("="*80)