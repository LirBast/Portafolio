import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
iris = load_iris()
X = iris.data
Z = linkage(X, method = 'ward')

plt.figure(figsize = (12, 10))
dendrogram(Z)
plt.title('Dendrograma de agrupamiento jerarquico')
plt.show()


wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42, max_iter = 300, n_init = 10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11),wcss)
plt.title('Metodo del codo')
plt.xlabel('Numero de cluster (k)')
plt.ylabel('WCSS')
plt.show()