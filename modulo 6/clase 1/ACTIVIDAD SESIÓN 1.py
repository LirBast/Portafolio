import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv(r'C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 6\clase 1\viviendas.csv')

# 1. Carga y Exploración Inicial del Dataset (1 punto) 

# Exploración inicial de los datos
print(df.head())       # Mostrar las primeras filas para ver la estructura
print('\n' + '='*80 + '\n')
print(df.info())       # Información general: tipos de datos y valores nulos
print('\n' + '='*80 + '\n')
print(df.describe())   # Estadísticas descriptivas básicas
print('\n' + '='*80 + '\n')



# 2. Limpieza de Datos (1 punto)

### limpieza de datos nulos
print(df.isnull().sum()) 
print('\n' + '='*80 + '\n')
df_limpio = df.dropna()

print(df_limpio.head())
print(df_limpio.info())     
print('\n' + '='*80 + '\n')

### corregir tipos
### desppues del analisis explotorio por el momento y por la cantidad de datos no es ncesario cambiar el tipo de datos

# 3. Análisis Exploratorio de Datos (2 puntos)

# Superficie vs Precio
plt.figure(figsize=(14,6))
plt.scatter(df_limpio['superficie'], df_limpio['precio'], alpha=0.7, c='blue', edgecolors='k')
plt.title('Relación Superficie vs Precio')
plt.xlabel('Superficie (m²)')
plt.ylabel('Precio')
plt.grid(True, alpha = 0.5)
plt.show()

# Habitaciones vs Precio
plt.figure(figsize=(14,6))
plt.scatter(df_limpio['habitaciones'], df_limpio['precio'], alpha=0.7, c='green', edgecolors='k')
plt.title('Relación Habitaciones vs Precio')
plt.xlabel('Número de Habitaciones')
plt.ylabel('Precio')
plt.grid(True, alpha = 0.5)
plt.show()

# Boxplot Precio
plt.figure(figsize=(10,6))
plt.boxplot(df_limpio['precio'])
plt.title('Boxplot Precio - Detección de Outliers')
plt.ylabel('Precio')
plt.grid(True, alpha = 0.5)
plt.show()

# Boxplot Superficie
plt.figure(figsize=(10,6))
plt.boxplot(df_limpio['superficie'])
plt.title('Boxplot Superficie - Detección de Outliers')
plt.ylabel('Superficie (m²)')
plt.grid(True, alpha = 0.5)
plt.show()

# Boxplot Habitaciones
plt.figure(figsize=(10,6))
plt.boxplot(df_limpio['habitaciones'])
plt.title('Boxplot Habitaciones - Detección de Outliers')
plt.ylabel('Número de Habitaciones')
plt.grid(True, alpha = 0.5)
plt.show()


# 4. Codificación de variables categóricas (1 punto) 
# • Convierte la variable barrio a variables numéricas utilizando One-Hot Encoding.

# 4. Codificación de variables categóricas (1 punto)

# One-Hot Encoding para la variable barrio
df_encoded = pd.get_dummies(df_limpio, columns=['barrio'], prefix='barrio')

print('Dataset después del One-Hot Encoding:')
print(df_encoded.head())
print('\n' + '='*80 + '\n')

print('Información del dataset codificado:')
print(df_encoded.info())
print('\n' + '='*80 + '\n')

print('Columnas creadas:')
print(df_encoded.columns.tolist())
print('\n' + '='*80 + '\n')

print('Forma del dataset:')
print(f'Antes: {df_limpio.shape}')
print(f'Después: {df_encoded.shape}')

# 5. División del Dataset (1 punto) 
# • Separa el dataset en un conjunto de entrenamiento (80%) y uno de prueba (20%).

# Separar características (X) y variable objetivo (y)
X = df_encoded.drop('precio', axis=1)  # Todas las columnas excepto precio
y = df_encoded['precio']               # Solo la columna precio

print('Características (X):')
print(X.head())
print('\n' + '='*80 + '\n')

print('Variable objetivo (y):')
print(y.head())
print('\n' + '='*80 + '\n')

# Separar en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train)
print('\n')
print(X_test)
print('\n')
print(y_train)
print('\n')
print(y_test)
print('\n') 

# 6.Entrenamiento de un Modelo de Regresión Lineal (2 puntos) 

### creacion del modelo
model = LinearRegression()

## entrenamiento del modelo
model.fit(X_train, y_train)

## realizar predicciones
y_prediccion = model.predict(X_test)

print('Coeficientes del modelo:')
print('\n') 
for feat, coef in zip(X.columns, model.coef_):
    print(f'{feat}: {coef:.2f}')
print(f'Intercepto: {model.intercept_:.2f}')

# 7. Evaluación del Modelo (2 puntos) 

# Error cuadrático medio (MSE)
MSE = mean_squared_error(y_test, y_prediccion)

# Raíz del error cuadrático medio (RMSE)
RMSE = np.sqrt(MSE)

# R2 Score
R2 = r2_score(y_test, y_prediccion)

print(f'El valor del Error Cuadrático Medio (MSE) es: {MSE:.2f}')
print(f'El valor de la Raíz del Error Cuadrático Medio (RMSE) es: {RMSE:.2f}')
print(f'El valor del Coeficiente de Determinación (R²) es: {R2:.2f}')


print('Interpretación del desempeño:')
if R2 > 0.7:
    print('El modelo explica bien la variabilidad del precio (R² alto).')
else:
    print('El modelo no logra explicar suficientemente la variabilidad del precio.')


### El modelo de regresión lineal muestra un buen desempeño, ya que explica el 78% de la variabilidad del
### precio (R² = 0.78) y presenta un error promedio de alrededor de 10 mil unidades (RMSE ≈ 10,076), lo que
### indica que es una herramienta adecuada para estimar los precios de las viviendas con las variables consideradas.