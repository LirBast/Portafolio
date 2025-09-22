import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder, PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt


# 1. Carga de datos (1 punto) 
# Carga el conjunto de datos proporcionado en el material complementario y realiza una exploración 
# inicial de los datos. Asegúrate de revisar si existen valores faltantes o anomalías en los datos. 


df = pd.read_csv(r'C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 6\clase 4\datos_inmuebles.csv')

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

# 2. Aplicación de modelos de regresión (5 puntos) 
# Regresión Lineal: 
# • Aplica un modelo de regresión lineal para predecir el precio de los inmuebles en función de 
# las características proporcionadas. 
# • Evalúa el desempeño del modelo utilizando el error cuadrático medio (MSE).

le = LabelEncoder()
df['Ubicación_encoded'] = le.fit_transform(df['Ubicación'])

print(df)
print(df.shape)

# 4. Separar X (features) e y (target)
X = df[['Tamaño_m2', 'Habitaciones', 'Ubicación_encoded', 'Año_Construcción']]
y = df['Precio_USD']

# 5. Dividir en conjunto de entrenamiento y prueba (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalado de características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Crear y entrenar modelo
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 7. Hacer predicciones
y_pred = model.predict(X_test_scaled)

# 8. Evaluación del modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Resultados del modelo:')
print(f'Error Cuadrático Medio (MSE): {mse:,.2f}')
print(f'R2 Score: {r2:.4f}')

# Regresión Polinómica: 
# • Transforma las variables de entrada utilizando características polinómicas de grado 2. 
# • Ajusta un modelo de regresión lineal sobre los datos transformados. 
# • Calcula el error cuadrático medio y compara con la regresión lineal. 

polinomi = PolynomialFeatures(degree=2, include_bias=False)
X_train_polinomi = polinomi.fit_transform(X_train_scaled)
X_test_polinomi = polinomi.transform(X_test_scaled)

print(f'Dimensiones originales: {X_train.shape}')
print(f'Dimensiones transformadas (polinómicas): {X_train_polinomi.shape}')

# 2. Ajustar modelo lineal con características polinómicas
poly_model = LinearRegression()
poly_model.fit(X_train_polinomi, y_train)

# 3. Predicciones
y_pred_poly = poly_model.predict(X_test_polinomi)

# 4. Evaluación
mse_poly = mean_squared_error(y_test, y_pred_poly)
rmse_poly = np.sqrt(mse_poly)
mae_poly = mean_absolute_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print('Resultados del modelo:')
print(f'Error Cuadrático Medio (MSE): {mse_poly:,.2f}')
print(f'Raíz del MSE (RMSE): {rmse_poly:,.2f}')
print(f'Error Absoluto Medio (MAE): {mae_poly:,.2f}')
print(f'R2 Score: {r2_poly:.4f}')
print('\n' + '='*80 + '\n')


# Árbol de Decisión: 
# • Implementa un modelo de regresión basado en árboles de decisión. 
# • Evalúa el rendimiento del modelo usando MSE y analiza su capacidad de generalización. 

#1. crear el modelo
tree_model = DecisionTreeRegressor(random_state=42, max_depth=5)
tree_model.fit(X_train_scaled, y_train)

# 2. Predicciones
y_pred_tree = tree_model.predict(X_test_scaled)

# 3. Evaluación
mse_tree = mean_squared_error(y_test, y_pred_tree)
rmse_tree = np.sqrt(mse_tree)
mae_tree = mean_absolute_error(y_test, y_pred_tree)
r2_tree = r2_score(y_test, y_pred_tree)

print(f'Error Cuadrático Medio (MSE): {mse_tree:,.2f}')
print(f'Raíz del MSE (RMSE): {rmse_tree:,.2f}')
print(f'Error Absoluto Medio (MAE): {mae_tree:,.2f}')
print(f'R² Score: {r2_tree:.4f}')
print('\n' + '='*80 + '\n')

# 3. Análisis de resultados (4 puntos) 
# Comparación de modelos: 
# • Explica las diferencias en los resultados obtenidos entre los tres modelos de regresión. 
# • Compara los valores de MSE y analiza cuál modelo se ajusta mejor a los datos.


print(f'Comparacion entre modelos')
print(f'Lineal: MSE = {mse:,.2f}')
print(f'Lineal R2 Score: {r2:.4f}')
print(f'Polinómica: MSE = {mse_poly:,.2f}')
print(f'Polinómica R2 Score: {r2_poly:.4f}')
print(f'Arbol: MSE = {mse_tree:,.2f}')
print(f'Arbol R2 Score : {r2_tree:.4f}')
print('\n' + '='*80 + '\n')


# Alinear índices para armar un dataset claro
X_test_view = X_test.reset_index(drop=True)
y_test_view = y_test.reset_index(drop=True)

df_pred = pd.DataFrame({
    'Precio_real': y_test_view,
    'Pred_Lineal': y_pred,
    'Pred_Polinomica': y_pred_poly,
    'Pred_Arbol': y_pred_tree
})

# Residuales (error = real - predicción)
df_pred['Res_Lineal'] = df_pred['Precio_real'] - df_pred['Pred_Lineal']
df_pred['Res_Polinomica'] = df_pred['Precio_real'] - df_pred['Pred_Polinomica']
df_pred['Res_Arbol'] = df_pred['Precio_real'] - df_pred['Pred_Arbol']

# Opcional: anexar features para análisis
df_pred_full = pd.concat([X_test_view.reset_index(drop=True), df_pred], axis=1)

print('\n=== Vista de predicciones ===')
print(df_pred_full.head(10))

plt.figure(figsize=(15, 4))

# Línea guía 45°
min_val = min(df_pred[['Precio_real','Pred_Lineal','Pred_Polinomica','Pred_Arbol']].min())
max_val = max(df_pred[['Precio_real','Pred_Lineal','Pred_Polinomica','Pred_Arbol']].max())

# Lineal
plt.subplot(1, 3, 1)
plt.scatter(df_pred['Precio_real'], df_pred['Pred_Lineal'], alpha=0.6, s=25)
plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2)
plt.title('Paridad: Regresión Lineal')
plt.xlabel('Precio real'); plt.ylabel('Precio predicho'); plt.grid(alpha=0.3)

# Polinómica
plt.subplot(1, 3, 2)
plt.scatter(df_pred['Precio_real'], df_pred['Pred_Polinomica'], alpha=0.6, s=25, color='tab:orange')
plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2)
plt.title('Paridad: Regresión Polinómica')
plt.xlabel('Precio real'); plt.ylabel('Precio predicho'); plt.grid(alpha=0.3)

# Árbol
plt.subplot(1, 3, 3)
plt.scatter(df_pred['Precio_real'], df_pred['Pred_Arbol'], alpha=0.6, s=25, color='tab:green')
plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2)
plt.title('Paridad: Árbol de Decisión')
plt.xlabel('Precio real'); plt.ylabel('Precio predicho'); plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12,4))

# Elige el modelo a analizar (ejemplo: polinómico)
pred = df_pred['Pred_Polinomica']
res = df_pred['Res_Polinomica']

plt.scatter(pred, res, alpha=0.6, s=25)
plt.axhline(0, color='r', linestyle='--', lw=2)
plt.title('Residuales vs Predicción (Polinómica)')
plt.xlabel('Precio predicho'); plt.ylabel('Residual (real - predicho)')
plt.grid(alpha=0.3)
plt.show()

importances = pd.Series(tree_model.feature_importances_, index=X.columns).sort_values(ascending=True)

plt.figure(figsize=(6,4))
importances.plot(kind='barh', color='tab:green')
plt.title('Importancia de variables (Árbol de Decisión)')
plt.xlabel('Importancia')
plt.tight_layout()
plt.show()