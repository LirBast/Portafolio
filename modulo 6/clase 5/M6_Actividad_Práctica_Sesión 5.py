import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# 1. Carga de datos (1 punto) 
# Carga el conjunto de datos proporcionado en el material complementario y realiza una exploración 
# inicial de los datos. Asegúrate de revisar si existen valores faltantes o anomalías en los datos. 

df = pd.read_csv(r'C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 6\clase 5\clientes.csv')

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

# 2. Aplicación de modelos de clasificación (6 puntos) 
# Implementa los siguientes modelos de clasificación y evalúa su desempeño: 

# Regresión logística: Implementa el modelo y analiza cómo la función sigmoidea afecta la clasificación. 

# Variables
X = df[['Edad', 'Ingresos', 'Historial_Compras', 'Suscripcion_Actual']]
y = df['Contratara_Servicio']

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

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
accuraci = accuracy_score(y_test, y_pred_scaled)

print('\n' + '='*80 + '\n')
print('Resultados del modelo de regresión logística')
print(f'Accuracy: {accuraci:.4f}')
print(f'Matriz de confusión: {matriz}')
print('\n' + '='*80 + '\n')
print('Reporte de Clasificación completo:')
print(classification_report(y_test, y_pred_scaled, digits=4))
print('\n' + '='*80 + '\n')

# K-Nearest Neighbors (K-NN): Prueba distintos valores de k y analiza su impacto en la exactitud. 
valores_k = [1, 3, 5, 7, 9, 11, 13, 15]

for k in valores_k:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_pred_knn = knn.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred_knn)
    print(f'K = {k}, Accuracy = {acc:.3f}')
print('\n' + '='*80 + '\n')

# Árbol de decisión: Ajusta los hiperparámetros del modelo y analiza las medidas de impureza de los nodos.
tree = DecisionTreeClassifier(max_depth=2, min_samples_split=10, min_samples_leaf=20, criterion='gini', random_state=42)
tree.fit(X_train_scaled, y_train)

y_pred_tree = tree.predict(X_test_scaled)
accuracy_tree = accuracy_score(y_test, y_pred_tree)

print(f'Accuracy: {accuracy_tree:.4f}')
print('Reporte de Clasificación:')
print(classification_report(y_test, y_pred_tree, digits=4))

# Bosques aleatorios: Aplica bagging para mejorar la predicción y analiza la importancia de las variables.
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42, n_jobs=-1)
rf.fit(X_train_scaled, y_train)

# Predicciones
y_pred_rf = rf.predict(X_test_scaled)

# Métricas
accuracy_rf = accuracy_score(y_test, y_pred_rf)
matriz_rf = confusion_matrix(y_test, y_pred_rf)

print('\n' + '='*80 + '\n')
print('Resultados del modelo Random Forest')
print(f'Accuracy: {accuracy_rf:.4f}')
print(f'Matriz de confusión:\n{matriz_rf}')
print('\nReporte de Clasificación:')
print(classification_report(y_test, y_pred_rf, digits=4))

importancia = pd.Series(rf.feature_importances_, index=X_train.columns)
print('\nImportancia de las variables en Random Forest:')
print(importancia.sort_values(ascending=False))

# SVM con distintos kernels
kernels = ['linear', 'poly', 'rbf', 'sigmoid']

for k in kernels:
    print('\n' + '='*80)
    print(f'Resultados con kernel: {k.upper()}')
    svm = SVC(kernel=k, probability=True, random_state=42)
    svm.fit(X_train_scaled, y_train)

    y_pred_svm = svm.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred_svm)

    print(f'Accuracy: {acc:.4f}')
    print('Reporte de Clasificación:')
    print(classification_report(y_test, y_pred_svm, digits=4))
