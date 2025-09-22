import kagglehub
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# Descargar la última versión del dataset desde Kaggle
path = kagglehub.dataset_download("uciml/breast-cancer-wisconsin-data")

print("Path to dataset files:", path)  # Mostrar ruta donde se descargó el dataset
print("Archivos disponibles:", os.listdir(path))  # Listar archivos en esa ruta

# Construir la ruta completa al archivo CSV y cargarlo en un DataFrame
dataset_path = os.path.join(path, 'data.csv')
df = pd.read_csv(dataset_path)

# Exploración inicial de los datos
print(df.head())       # Mostrar las primeras filas para ver la estructura
print("\n" + "="*80 + "\n")
print(df.info())       # Información general: tipos de datos y valores nulos
print("\n" + "="*80 + "\n")
print(df.describe())   # Estadísticas descriptivas básicas
print("\n" + "="*80 + "\n")

# Limpieza de datos: eliminar columnas no relevantes para clustering
df_limpio = df.drop(['id', 'diagnosis', 'Unnamed: 32'], axis=1)

# Escalado de características para normalizar la influencia de cada variable
scaler = StandardScaler()
X_scalados = scaler.fit_transform(df_limpio)

print("Datos escalados correctamente")
print("Shape de los datos escalados:", X_scalados.shape)  # Mostrar dimensiones de los datos escalados

# Preparar lista para guardar las inercias (suma de distancias cuadradas dentro de clusters)
inercias = []

# Probar diferentes números de clusters (k) para el método del codo
Ks = range(1, 11)  # k desde 1 hasta 10

for k in Ks:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)  # Crear modelo KMeans
    kmeans.fit(X_scalados)  # Ajustar modelo a los datos escalados
    inercias.append(kmeans.inertia_)  # Guardar la inercia para este k

# Graficar el método del codo para visualizar la inercia según k
plt.figure(figsize=(8,6))
plt.plot(list(Ks), inercias, marker='o')
plt.xlabel("Número de Clusters (k)")
plt.ylabel("Inercia")
plt.title("Método del Codo")
plt.grid(True)
plt.show()

# Aplicar KMeans con k=2 (elegido tras observar el gráfico del codo)
kmeans_final = KMeans(n_clusters=2, random_state=42, n_init=10)
clusters = kmeans_final.fit_predict(X_scalados)  # Obtener etiquetas de cluster para cada muestra

# Añadir la columna 'Cluster' al DataFrame original para comparar con diagnóstico
df['Cluster'] = clusters
print(df[['diagnosis', 'Cluster']].head())  # Mostrar primeras filas con diagnóstico y cluster asignado

# Obtener los centroides de los clusters en el espacio escalado
centroides = kmeans_final.cluster_centers_
df_centroides = pd.DataFrame(centroides, columns=df_limpio.columns)

print("\n" + "="*80 + "\n")
print(df_centroides)  # Mostrar centroides para interpretar características promedio de cada cluster

