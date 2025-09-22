# ===============================================
# ANÁLISIS DE CLUSTERING CON IRIS Y MAKE_MOONS
# ===============================================

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_iris, make_moons
from sklearn.cluster import KMeans,DBSCAN

# ===============================================
# 1) CARGA Y PREPARACIÓN DE DATOS IRIS
# ===============================================
# Cargamos el dataset Iris (150 muestras, 4 características)
iris = load_iris()

# Seleccionamos solo las primeras 30 filas para análisis más rápido
# Nota: usar todo el dataset (iris.data) daría mejor estimación de K
X = iris.data[:30, :]  # primeras 30 filas

# ===============================================
# 2) CLUSTERING JERÁRQUICO (DENDROGRAMA)
# ===============================================
# Calculamos la matriz de enlace usando el método Ward
# Ward minimiza la varianza intra-cluster al fusionar clusters
Z = linkage(X, method='ward')

# Descomentamos para ver el dendrograma
# plt.figure(figsize=(12,6))
# dendrogram(Z)
# plt.title('Dendrograma de agrupamiento jerarquico')
# plt.show()

# ===============================================
# 3) MÉTODO DEL CODO PARA K-MEANS
# ===============================================
# Calculamos WCSS (Within-Cluster Sum of Squares) para diferentes valores de K
# WCSS mide la suma de distancias cuadráticas de cada punto a su centroide
wcss = []

for i in range(1,11):
  # Creamos modelo K-Means con i clusters
  # init='k-means++': inicialización inteligente de centroides
  # random_state=42: reproducibilidad de resultados
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42, max_iter=300, n_init=10)
  kmeans.fit(X)  # Entrenamos el modelo
  wcss.append(kmeans.inertia_)  # Guardamos el WCSS (inercia)

# Graficamos el método del codo
# El "codo" indica el número óptimo de clusters
plt.plot(range(1,11),wcss, marker = 'o')
plt.xticks(range(1,11))
plt.title('Metodo del codo')
plt.xlabel('Numero de clusters (k)')
plt.ylabel('WCSS')
plt.show()

# ===============================================
# 4) DBSCAN EN DATOS MAKE_MOONS
# ===============================================
# Generamos datos sintéticos en forma de dos lunas entrelazadas
# noise=0.1: añade ruido gaussiano para hacer más realista
X, _ = make_moons(n_samples = 300, noise = 0.1, random_state = 42)   ### el guion bajo se usa para que ignore las etiquetas que entrega, en este caso, el make_moons

# Aplicamos DBSCAN (Density-Based Spatial Clustering)
# eps=0.3: radio máximo de vecindario para considerar puntos como vecinos
# min_samples=5: mínimo número de puntos en un vecindario para formar un cluster
db = DBSCAN(eps = 0.3, min_samples = 5)
etiquetas_db = db.fit_predict(X)  # Obtenemos las etiquetas de cluster (-1 = ruido)

# Visualizamos los resultados
# Los puntos se colorean según su cluster asignado
# Los puntos de ruido (etiqueta -1) aparecen en color diferente
plt.scatter(X[:,0], X[:,1], c=etiquetas_db, cmap='plasma')
plt.title('DBSCAN')
plt.show()