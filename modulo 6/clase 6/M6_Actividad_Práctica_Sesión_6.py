# 1. Carga de datos (1 punto) 
# • Descarga los conjuntos de datos proporcionados en el material complementario. 
# • Carga los datos 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_csv(r'C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 6\clase 6\datos_regresion.csv')

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

# one-hot encoding a la variable categorica
df = pd.get_dummies(df, columns=['Categoria'], prefix='Categoria')
print('Datos después del One-Hot Encoding:')
print(df.head())
print(df.shape)

# 2. Evaluación de un modelo de regresión (4 puntos) 

# Variables
X = df.drop('Valor_Ventas', axis=1)  # Todas las columnas excepto la variable objetivo
y = df['Valor_Ventas']

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

# Modelo de Regresión Lineal
lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train)

# Predicciones
y_pred = lin_reg.predict(X_test_scaled)

# Métricas de regresión 
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print('\n' + '='*80 + '\n')
print(f'MAE (Error Absoluto Medio): {mae:.2f}')
print(f'MSE (Error Cuadrático Medio): {mse:.2f}')
print(f'RMSE (Raíz del Error Cuadrático Medio): {rmse:.2f}')
print(f'R² (Coeficiente de Determinación): {r2:.4f}')


