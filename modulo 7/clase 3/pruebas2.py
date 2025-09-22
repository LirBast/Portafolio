import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification

# Crear datos sintéticos con escalas muy diferentes
np.random.seed(42)
n_samples = 100

# Variable 1: Edad (escala pequeña: 20-60)
edad = np.random.uniform(20, 60, n_samples)

# Variable 2: Salario (escala grande: 20,000-80,000)
salario = np.random.uniform(20000, 80000, n_samples)

# Crear etiquetas basadas en una regla simple
# Personas jóvenes con salario alto = clase 1, resto = clase 0
y = ((edad < 40) & (salario > 50000)).astype(int)

X = np.column_stack([edad, salario])

print("Datos originales:")
print(f"Edad - Min: {edad.min():.1f}, Max: {edad.max():.1f}, Media: {edad.mean():.1f}")
print(f"Salario - Min: {salario.min():.0f}, Max: {salario.max():.0f}, Media: {salario.mean():.0f}")

# Estandarizar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nDatos estandarizados:")
print(f"Edad - Min: {X_scaled[:,0].min():.2f}, Max: {X_scaled[:,0].max():.2f}, Media: {X_scaled[:,0].mean():.2f}")
print(f"Salario - Min: {X_scaled[:,1].min():.2f}, Max: {X_scaled[:,1].max():.2f}, Media: {X_scaled[:,1].mean():.2f}")

# Crear visualización
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Datos originales - Scatter plot
axes[0,0].scatter(X[y==0, 0], X[y==0, 1], c='red', alpha=0.6, label='Clase 0')
axes[0,0].scatter(X[y==1, 0], X[y==1, 1], c='blue', alpha=0.6, label='Clase 1')
axes[0,0].set_xlabel('Edad')
axes[0,0].set_ylabel('Salario')
axes[0,0].set_title('Datos Originales (Sin Estandarizar)')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)

# 2. Datos estandarizados - Scatter plot
axes[0,1].scatter(X_scaled[y==0, 0], X_scaled[y==0, 1], c='red', alpha=0.6, label='Clase 0')
axes[0,1].scatter(X_scaled[y==1, 0], X_scaled[y==1, 1], c='blue', alpha=0.6, label='Clase 1')
axes[0,1].set_xlabel('Edad (estandarizada)')
axes[0,1].set_ylabel('Salario (estandarizado)')
axes[0,1].set_title('Datos Estandarizados')
axes[0,1].legend()
axes[0,1].grid(True, alpha=0.3)

# 3. Comparación de distribuciones - Edad
axes[1,0].hist(X[:, 0], bins=15, alpha=0.7, color='skyblue', label='Original')
axes[1,0].hist(X_scaled[:, 0], bins=15, alpha=0.7, color='orange', label='Estandarizada')
axes[1,0].set_xlabel('Valores')
axes[1,0].set_ylabel('Frecuencia')
axes[1,0].set_title('Distribución: Edad')
axes[1,0].legend()
axes[1,0].grid(True, alpha=0.3)

# 4. Comparación de distribuciones - Salario
axes[1,1].hist(X[:, 1], bins=15, alpha=0.7, color='skyblue', label='Original')
axes[1,1].hist(X_scaled[:, 1], bins=15, alpha=0.7, color='orange', label='Estandarizada')
axes[1,1].set_xlabel('Valores')
axes[1,1].set_ylabel('Frecuencia')
axes[1,1].set_title('Distribución: Salario')
axes[1,1].legend()
axes[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Demostrar el impacto en KNN
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# KNN sin estandarizar
knn_original = KNeighborsClassifier(n_neighbors=5)
knn_original.fit(X_train, y_train)
pred_original = knn_original.predict(X_test)
acc_original = accuracy_score(y_test, pred_original)

# KNN con estandarización
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_scaled = KNeighborsClassifier(n_neighbors=5)
knn_scaled.fit(X_train_scaled, y_train)
pred_scaled = knn_scaled.predict(X_test_scaled)
acc_scaled = accuracy_score(y_test, pred_scaled)

print(f"\n--- Impacto en KNN ---")
print(f"Precisión sin estandarizar: {acc_original:.3f}")
print(f"Precisión con estandarización: {acc_scaled:.3f}")
print(f"Mejora: {acc_scaled - acc_original:.3f}")