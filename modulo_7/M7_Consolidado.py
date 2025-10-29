import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.metrics import adjusted_rand_score
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# =====================================================
# 1. Carga y exploración de datos
# =====================================================
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

# Preprocesamiento
df_limpio = df.drop(['País'], axis=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_limpio)

# =====================================================
# 2. Aplicación de algoritmos de clusterización
# =====================================================

# -------------------------
# 2.1. Método del codo
# -------------------------
inercia = []
ks = range(2, 9)
for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inercia.append(km.inertia_)

# Mostrar los valores de inercia
print("Valores de inercia (SSE) para cada K:")
for k, sse in zip(ks, inercia):
    print(f"K={k} → {sse:.2f}")

# Gráfico del codo
plt.figure(figsize=(6, 4))
plt.plot(list(ks), inercia, marker='o')
plt.xlabel('Número de clusters K')
plt.ylabel('Inercia (Suma de errores cuadráticos)')
plt.title('Método del codo')
plt.grid()
plt.show()

# -------------------------
# 2.2. Método de la silueta
# -------------------------
ks_silhouette = range(2, len(df))
silhouette_scores = []
for k in ks_silhouette:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    etiquetas = km.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, etiquetas)
    silhouette_scores.append(sil)
    print(f"K={k}, Silhouette Score={sil:.3f}")

# Gráfico de la silueta
plt.figure(figsize=(6, 4))
plt.plot(list(ks_silhouette), silhouette_scores, marker='o')
plt.xlabel('Número de clusters K')
plt.ylabel('Silhouette score')
plt.title('Método de la silueta')
plt.grid()
plt.show()

# -------------------------
# 2.3. K-Means final
# -------------------------
modelo = KMeans(n_clusters=3, random_state=42, n_init=10)
modelo.fit(X_scaled)
df['Cluster'] = modelo.labels_
print('Etiquetas de cluster asignadas (K=3):', modelo.labels_)

# -------------------------
# 2.4. Clustering jerárquico
# -------------------------
Z = linkage(X_scaled, method='ward')
plt.figure(figsize=(8, 5))
dendrogram(Z, labels=df['País'].values)
plt.title('Dendrograma de agrupamiento jerárquico')
plt.show()

# Cortar en 3 clusters (para comparar con KMeans)
clusters_hier = fcluster(Z, t=3, criterion="maxclust")
df["Cluster_Hier"] = clusters_hier
print("Comparación de clusters KMeans vs Jerárquico:")
print(df[["País", "Cluster", "Cluster_Hier"]])
ari = adjusted_rand_score(df["Cluster"], df["Cluster_Hier"])
print(f"Similitud entre KMeans y Jerárquico (ARI): {ari:.3f}")

# -------------------------
# 2.5. DBSCAN
# -------------------------

# Gráfico K-Distance para estimar eps
min_samples = 3
neighbors = NearestNeighbors(n_neighbors=min_samples)
neighbors_fit = neighbors.fit(X_scaled)
distancias, indices = neighbors_fit.kneighbors(X_scaled)
distancias = np.sort(distancias[:, -1])

plt.figure(figsize=(6,4))
plt.plot(distancias)
plt.ylabel(f"Distancia al {min_samples}-ésimo vecino")
plt.xlabel("Puntos ordenados")
plt.title("Gráfico de K-Distance para DBSCAN")
plt.grid()
plt.show()

# DBSCAN probando distintos parámetros
eps_values = [1.5, 2.5, 3.5]
min_samples_values = [2, 3]

for eps_val in eps_values:
    for ms in min_samples_values:
        dbscan = DBSCAN(eps=eps_val, min_samples=ms)
        labels = dbscan.fit_predict(X_scaled)

        df[f"DBSCAN_eps{eps_val}_ms{ms}"] = labels
        print(f"\n=== DBSCAN con eps={eps_val}, min_samples={ms} ===")
        print(df[["País", f"DBSCAN_eps{eps_val}_ms{ms}"]].to_string(index=False))

# =====================================================
# 3. Reducción de dimensionalidad - PCA
# =====================================================
pca_full = PCA()
pca_full.fit(X_scaled)

# Varianza explicada acumulada
varianza_acum = np.cumsum(pca_full.explained_variance_ratio_)
print("Varianza explicada acumulada por componentes:")
for i, var in enumerate(varianza_acum):
    print(f"Componente {i+1}: {var:.4f}")

# Determinar número de componentes para explicar >= 90%
n_componentes_90 = np.argmax(varianza_acum >= 0.90) + 1
print(f"\nNúmero mínimo de componentes que explican >=90% de la varianza: {n_componentes_90}")

# --- Visualización en 2D con las dos primeras componentes principales
pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X_scaled)

plt.figure(figsize=(8,6))
plt.scatter(X_pca_2d[:,0], X_pca_2d[:,1], c=df["Cluster"], cmap="viridis", s=100, alpha=0.8)
plt.title("PCA 2D: países en las dos primeras componentes")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.grid(True)
plt.show()

# =====================================================
# 4. Reducción de dimensionalidad - t-SNE
# =====================================================
perplexities = [2, 3, 5, 7]

plt.figure(figsize=(12, 8))
for i, perp in enumerate(perplexities, 1):
    tsne = TSNE(n_components=2, perplexity=perp, random_state=42)
    X_tsne = tsne.fit_transform(X_scaled)

    plt.subplot(2, 2, i)
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=df["Cluster"], cmap="viridis", s=100, alpha=0.7)
    plt.title(f't-SNE (perplexity={perp})')
    plt.xlabel("Dim 1")
    plt.ylabel("Dim 2")

plt.tight_layout()
plt.show()
