import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.metrics import adjusted_rand_score
from sklearn.neighbors import NearestNeighbors


# 1. Carga y exploración de datos (1 punto) 
# • Carga el dataset proporcionado, que contiene información sobre la popularidad de distintos 
# géneros musicales en países como Chile, EE.UU., México, Corea, Japón, Alemania, Rusia e 
# Italia. 
# • Analiza las características del dataset, identificando distribuciones y tendencias iniciales. 


# 1. Carga y exploración de datos
df = pd.read_csv(r'C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 7\consolidado\dataset_generos_musicales.csv')

# Exploración inicial
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


df_limpio = df.drop(['País'], axis=1)

print(df_limpio.dtypes)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_limpio)


# 2. Aplicación de algoritmos de clusterización (5 puntos) 
# K-Means: 
# • Aplica el algoritmo K-Means con un valor inicial de K=3. 
# • Determina el valor óptimo de K utilizando el método del codo y el coeficiente de silueta. 

modelo = KMeans(n_clusters = 3, random_state = 42, n_init =  10 )
modelo.fit(X_scaled)

df['Cluster'] = modelo.labels_

print('Etiquetas de cluster asignadas:', modelo.labels_)


inercia = []
ks = range(2, 9)  # Probar k desde 2 hasta 9

for k in ks:
    km = KMeans(n_clusters = k, random_state = 42, n_init = 10)
    km.fit(X_scaled)
    inercia.append(km.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(list(ks), inercia, marker='o')
plt.xlabel('K clusters')
plt.ylabel('Inercia (Suma de errores cuadráticos)')
plt.title('Método del codo')
plt.grid()
plt.show()

ks_silhouette = range(2, len(df))

silhouette_scores = []

for k in ks_silhouette:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    etiquetas = km.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, etiquetas)
    silhouette_scores.append(sil)

plt.figure(figsize=(6, 4))
plt.plot(list(ks_silhouette), silhouette_scores, marker='o')
plt.xlabel('K clusters')
plt.ylabel('Silhouette score')
plt.title('Método de la silueta')
plt.grid()
plt.show()


# Clustering jerárquico: 
# • Genera un dendrograma y determina el número óptimo de clusters. 
# • Aplica clustering jerárquico y compara con los resultados de K-Means.

Z = linkage(X_scaled, method = 'ward')

plt.figure(figsize = (8, 5))
dendrogram(Z, labels=df['País'].values)
plt.title('Dendrograma de agrupamiento jerarquico')
plt.show()

from sklearn.metrics import adjusted_rand_score

# Cortar dendrograma en 3 clusters (mismo que KMeans inicial)
clusters_hier = fcluster(Z, t=3, criterion="maxclust")
df["Cluster_Hier"] = clusters_hier

print("Comparación de clusters:")
print(df[["País", "Cluster", "Cluster_Hier"]])

ari = adjusted_rand_score(df["Cluster"], df["Cluster_Hier"])
print(f"Similitud entre KMeans y Jerárquico (ARI): {ari:.3f}")

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8,6))
plt.scatter(X_pca[:,0], X_pca[:,1], c=df["Cluster"], cmap="viridis", s=100)
for i, txt in enumerate(df["País"]):
    plt.annotate(txt, (X_pca[i,0], X_pca[i,1]), xytext=(5,5), textcoords="offset points")
plt.title("Clusters KMeans visualizados en PCA 2D")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.show()

# DBSCAN: 
# • Aplica DBSCAN con diferentes valores de eps y MinPts. 
# • Justifica la elección de los parámetros y analiza si DBSCAN identifica agrupaciones

dbscan = DBSCAN(eps=5, min_samples=2)
labels_dbscan = dbscan.fit_predict(X_scaled)

df["Cluster_DBSCAN"] = labels_dbscan
print("Clusters DBSCAN:")
print(df[["País", "Cluster_DBSCAN"]])

 ============================
# 1. Cálculo de K-Distance
# ============================

min_samples = 3  # puedes ajustar (ej: 2, 3, 4)
neighbors = NearestNeighbors(n_neighbors=min_samples)
neighbors_fit = neighbors.fit(X_scaled)
distancias, indices = neighbors_fit.kneighbors(X_scaled)

# Tomamos la distancia al último vecino (k-dist)
distancias = np.sort(distancias[:, -1])

plt.figure(figsize=(6,4))
plt.plot(distancias)
plt.ylabel(f"Distancia al {min_samples}-ésimo vecino")
plt.xlabel("Puntos ordenados")
plt.title("Gráfico de K-Distance para DBSCAN")
plt.grid()
plt.show()

# ============================
# 2. Elección de eps
# ============================
# 👀 Aquí revisas la gráfica y eliges el "codo".
# Supongamos que el codo se observa en ~2.5
eps_optimo = 2.5  

# ============================
# 3. Aplicación de DBSCAN
# ============================

dbscan = DBSCAN(eps=eps_optimo, min_samples=min_samples)
labels_dbscan = dbscan.fit_predict(X_scaled)

df["Cluster_DBSCAN"] = labels_dbscan
print("Clusters DBSCAN:")
print(df[["País", "Cluster_DBSCAN"]])

# ============================
# 4. Visualización en PCA 2D
# ============================

plt.figure(figsize=(8,6))
plt.scatter(X_pca[:,0], X_pca[:,1], c=labels_dbscan, cmap="tab10", s=100)
for i, txt in enumerate(df["País"]):
    plt.annotate(txt, (X_pca[i,0], X_pca[i,1]), xytext=(5,5), textcoords="offset points")
plt.title(f"DBSCAN con eps={eps_optimo}, min_samples={min_samples}")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.show()