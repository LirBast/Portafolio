import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import regularizers
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# =====================================================
# 1. Carga y exploración de datos
# =====================================================

df = pd.read_csv(r'C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 8\consolidado\dataset_natalidad.csv')

print(df.head())       
print(df.shape)
print('\n' + '='*80 + '\n')
print(df.info())
print('\n' + '='*80 + '\n')
print(df.describe())
print('\n' + '='*80 + '\n')
print('Cantidad de datos nulos')
print(df.isnull().sum())
print('\n' + '='*80 + '\n')

# Limpieza de datos
df_limpio = df.drop(columns=['País'])
print(df_limpio.head())
print('\n' + '='*80 + '\n')

# Correlaciones
corr = df_limpio.corr()
plt.figure(figsize=(12,8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Matriz de Correlación entre Variables Socioeconómicas')
plt.show()


# =====================================================
# 2. Diseño y entrenamiento del modelo
# =====================================================

X = df_limpio.drop(columns=['Tasa_Natalidad'])
y = df_limpio['Tasa_Natalidad']

print('Dimensiones de X:', X.shape)
print('Dimensiones de y:', y.shape)
print('\n' + '='*80 + '\n')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print('Dimensiones de entrenamiento:', X_train_scaled.shape, y_train.shape)
print('Dimensiones de prueba:', X_test_scaled.shape, y_test.shape)
print('\n' + '='*80 + '\n')

# ==========================
#  PCA
# ==========================
pca = PCA(n_components=0.95)  # conserva 95% de la varianza
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

print('Dimensiones reducidas con PCA:', X_train_pca.shape)

# -----------------------------------------------------
# Modelo base (sin PCA)
# -----------------------------------------------------
model = Sequential([
    Dense(64, activation='relu', input_dim=X_train_scaled.shape[1]),
    Dense(32, activation='relu'),
    Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')

epocas = 150
funcion_pare = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

historial_base = model.fit(X_train_scaled, y_train,
                           epochs=epocas,
                           batch_size=32,
                           validation_split=0.2,
                           verbose=0,
                           callbacks=[funcion_pare])

# -----------------------------------------------------
# Modelo con PCA
# -----------------------------------------------------
model_pca = Sequential([
    Dense(64, activation='relu', input_dim=X_train_pca.shape[1]),
    Dense(32, activation='relu'),
    Dense(1)
])
model_pca.compile(optimizer='adam', loss='mean_squared_error')

historial_pca = model_pca.fit(X_train_pca, y_train,
                              epochs=epocas,
                              batch_size=32,
                              validation_split=0.2,
                              verbose=0,
                              callbacks=[funcion_pare])

# Historial del modelo base
historial_df = pd.DataFrame(historial_base.history)
historial_df['epoch'] = range(1, len(historial_df)+1)

plt.figure(figsize=(8,5))
plt.plot(historial_base.history['loss'], label='Entrenamiento (Base)')
plt.plot(historial_base.history['val_loss'], label='Validación (Base)')
plt.plot(historial_pca.history['loss'], label='Entrenamiento (PCA)')
plt.plot(historial_pca.history['val_loss'], label='Validación (PCA)')
plt.xlabel('Épocas')
plt.ylabel('Pérdida (MSE)')
plt.title(f'Curva de pérdida: Modelo Base vs PCA')  
plt.legend()
plt.grid(True)
plt.show()


# -----------------------------------------------------
# Modelos con diferentes configuraciones (sin PCA)
# -----------------------------------------------------
resultados = []

# Guardar modelo base en la tabla
resultados.append({
    'Configuración': 'BASE: relu + Adam(0.001) + MSE',
    'Loss final': historial_base.history['loss'][-1],
    'Val Loss final': historial_base.history['val_loss'][-1]})

# Guardar modelo PCA en la tabla
resultados.append({
    'Configuración': 'PCA: relu + Adam(0.001) + MSE',
    'Loss final': historial_pca.history['loss'][-1],
    'Val Loss final': historial_pca.history['val_loss'][-1]})

# 1. tanh + Adam(0.001) + MSE
model1 = Sequential([
    Dense(64, activation='tanh', input_dim=X_train_scaled.shape[1]),
    Dense(32, activation='tanh'),
    Dense(1)
])
model1.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
historial1 = model1.fit(X_train_scaled, y_train, epochs=epocas, batch_size=32, validation_split=0.2, verbose=0, callbacks=[funcion_pare])
resultados.append({'Configuración': 'tanh + Adam(0.001) + MSE',
                   'Loss final': historial1.history['loss'][-1],
                   'Val Loss final': historial1.history['val_loss'][-1]})

# 2. relu + SGD(0.01) + MSE
model2 = Sequential([
    Dense(64, activation='relu', input_dim=X_train_scaled.shape[1]),
    Dense(32, activation='relu'),
    Dense(1)
])
model2.compile(optimizer=SGD(learning_rate=0.01), loss='mse')
historial2 = model2.fit(X_train_scaled, y_train, epochs=epocas, batch_size=32, validation_split=0.2, verbose=0, callbacks=[funcion_pare])
resultados.append({'Configuración': 'relu + SGD(0.01) + MSE',
                   'Loss final': historial2.history['loss'][-1],
                   'Val Loss final': historial2.history['val_loss'][-1]})

# 3. relu + Adam(0.001) + Dropout
model3 = Sequential([
    Dense(64, activation='relu', input_dim=X_train_scaled.shape[1]),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(1)
])
model3.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
historial3 = model3.fit(X_train_scaled, y_train, epochs=epocas, batch_size=32, validation_split=0.2, verbose=0, callbacks=[funcion_pare])
resultados.append({'Configuración': 'relu + Adam(0.001) + Dropout',
                   'Loss final': historial3.history['loss'][-1],
                   'Val Loss final': historial3.history['val_loss'][-1]})

# 4. relu + Adam(0.001) + L2
model4 = Sequential([
    Dense(64, activation='relu', input_dim=X_train_scaled.shape[1], kernel_regularizer=regularizers.l2(0.01)),
    Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dense(1)
])
model4.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
historial4 = model4.fit(X_train_scaled, y_train, epochs=epocas, batch_size=32, validation_split=0.2, verbose=0, callbacks=[funcion_pare])
resultados.append({'Configuración': 'relu + Adam(0.001) + L2',
                   'Loss final': historial4.history['loss'][-1],
                   'Val Loss final': historial4.history['val_loss'][-1]})

# 5. relu + Adam(0.001) + MAE
model5 = Sequential([
    Dense(64, activation='relu', input_dim=X_train_scaled.shape[1]),
    Dense(32, activation='relu'),
    Dense(1)
])
model5.compile(optimizer=Adam(learning_rate=0.001), loss='mae')
historial5 = model5.fit(X_train_scaled, y_train, epochs=epocas, batch_size=32, validation_split=0.2, verbose=0, callbacks=[funcion_pare])
resultados.append({'Configuración': 'relu + Adam(0.001) + MAE',
                   'Loss final': historial5.history['loss'][-1],
                   'Val Loss final': historial5.history['val_loss'][-1]})

# Tabla comparativa final de configuraciones
tabla_resultados = pd.DataFrame(resultados)
print('\n Comparación de configuraciones:')
print(tabla_resultados)


# =====================================================
# 3. Evaluación y optimización del modelo
# =====================================================

# Evaluar modelo BASE con datos de prueba
predicciones_base = model.predict(X_test_scaled).ravel()
mse_base = mean_squared_error(y_test, predicciones_base)
mae_base = mean_absolute_error(y_test, predicciones_base)
r2_base  = r2_score(y_test, predicciones_base)

print('\nMétricas en TEST (modelo BASE)')
print(f'MSE: {mse_base:.3f} | MAE: {mae_base:.3f} | R²: {r2_base:.3f}')

# Evaluar modelo PCA con datos de prueba
predicciones_pca = model_pca.predict(X_test_pca).ravel()
mse_pca = mean_squared_error(y_test, predicciones_pca)
mae_pca = mean_absolute_error(y_test, predicciones_pca)
r2_pca  = r2_score(y_test, predicciones_pca)

print('\nMétricas en TEST (modelo PCA)')
print(f'MSE: {mse_pca:.3f} | MAE: {mae_pca:.3f} | R²: {r2_pca:.3f}')

# Comparar primeros 10 valores reales vs predichos (PCA)
print('\nComparación de los primeros 10 valores reales vs predichos (PCA):')
for i in range(10):
    print(f"Real: {y_test.iloc[i]:.2f} | Predicción: {predicciones_pca[i]:.2f}")
