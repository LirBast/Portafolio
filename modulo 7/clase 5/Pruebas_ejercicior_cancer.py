import kagglehub
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
import numpy as np
from sklearn.decomposition import PCA

# Descargar la última versión del dataset desde Kaggle
path = kagglehub.dataset_download("uciml/breast-cancer-wisconsin-data")

print("Path to dataset files:", path)
print("Archivos disponibles:", os.listdir(path))

# Cargar el archivo CSV en un DataFrame
dataset_path = os.path.join(path, 'data.csv')
df = pd.read_csv(dataset_path)

# Exploración inicial de los datos
print(df.head())       # Primeras filas para ver estructura
print("\n" + "="*80 + "\n")
print(df.info())       # Información general: tipos y nulos
print("\n" + "="*80 + "\n")
print(df.describe())   # Estadísticas descriptivas
print("\n" + "="*80 + "\n")

# Preparar datos para clustering: eliminar columnas no numéricas o irrelevantes
df_limpio = df.drop(['id', 'diagnosis', 'Unnamed: 32'], axis=1, errors='ignore')

# Escalado de características para normalizar la influencia de cada variable
ss = StandardScaler()
X_scaled = ss.fit_transform(df_limpio)  # CORRECCIÓN: usar df_limpio en lugar de X

# Método del codo para elegir número óptimo de clusters
inercia = []
ks = range(2, 11)  # Probar k desde 2 hasta 10

for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inercia.append(km.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(list(ks), inercia, marker='o')
plt.xlabel('K clusters')
plt.ylabel('Inercia (Suma de errores cuadráticos)')
plt.title('Método del codo')
plt.grid()
plt.show()

# Método de la silueta para evaluar la calidad del clustering
silhouette_scores = []

for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    etiquetas = km.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, etiquetas)
    silhouette_scores.append(sil)

plt.figure(figsize=(6, 4))
plt.plot(list(ks), silhouette_scores, marker='o')
plt.xlabel('K clusters')
plt.ylabel('Silhouette score')
plt.title('Método de la silueta')
plt.grid()
plt.show()

# Selección del mejor k según el máximo silhouette score
best_k_sil = ks[int(np.argmax(silhouette_scores))]
print(f"Mejor número de clusters según silhouette score: {best_k_sil} con valor {max(silhouette_scores):.4f}")

k_optimo = int(best_k_sil)

# Aplicar KMeans con el k óptimo
km = KMeans(n_clusters=k_optimo, random_state=42, n_init=10)
etiquetas = km.fit_predict(X_scaled)

# Convertir X_scaled a DataFrame para facilitar manipulación y añadir cluster
X_scaled_df = pd.DataFrame(X_scaled, columns=df_limpio.columns)
X_scaled_df['Cluster'] = etiquetas

# Obtener centroides en el espacio escalado
centroides = km.cluster_centers_

# Reducir dimensionalidad a 2D para visualización con PCA
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_scaled)
centroides_pca = pca.transform(centroides)

# Graficar clusters y centroides en espacio PCA 2D
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=etiquetas, cmap='viridis', alpha=0.6)
plt.scatter(centroides_pca[:, 0], centroides_pca[:, 1], marker='x', s=200, color='black', label='Centroides')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.title(f'KMeans con k = {k_optimo} en espacio PCA (2D)')
plt.legend()
plt.grid()
plt.show()