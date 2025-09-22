from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np


np.random.seed(0)

X = np.random.rand(100, 2)*10


# Listas para guardar métricas
wcss = []
silhouettes_score = []
K_range = range(2, 11) # Silhouette score necesita al menos 2 clusters



for k in K_range:
    kmeans = KMeans(n_clusters = k, random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    silhouettes_score.append(silhouette_score(X, kmeans.labels_))

plt.plot(K_range, wcss, 'bo-')
plt.title('Metodo del codo')
plt.xlabel('K')
plt.ylabel('WCSS')
plt.show()

plt.plot(K_range, silhouettes_score, 'ro-')
plt.title('Metodo de la silueta')
plt.xlabel('K')
plt.ylabel('silhouettes score')
plt.show()