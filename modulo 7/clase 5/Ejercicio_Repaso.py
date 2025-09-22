import kagglehub
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

#Importacion de los datos
# Download latest version
path = kagglehub.dataset_download("vjchoudhary7/customer-segmentation-tutorial-in-python")

print("Path to dataset files:", path)

print("Archivos disponibles:", os.listdir(path))
dataset_path = os.path.join(path, 'Mall_Customers.csv')
df = pd.read_csv(dataset_path)

#Exploracion de los datos

print(df.head())
print("\n" + "="*80 + "\n")
print(df.info())
print("\n" + "="*80 + "\n")
print(df.describe())
print("\n" + "="*80 + "\n")

sns.pairplot(df, hue='Gender') #hue coloriar los puntos
plt.suptitle('Relaciones entre variables en dataset de clientes', y=1.02)
plt.show()

print("\n" + "="*80 + "\n")

fig, axes = plt.subplots(1,3, figsize=(18,6)) #1 fila, 3 columnas - figsize tamaño del lienso en pulgadas
sns.boxplot(x='Gender', y='Age', data=df, ax=axes[0])
axes[0].set_title('Distribucion de la edad por genero')
sns.boxplot(x='Gender', y='Annual Income (k$)', data=df, ax=axes[1])
axes[1].set_title('Distribucion de la ingreso por genero')
sns.boxplot(x='Gender', y='Spending Score (1-100)', data=df, ax=axes[2])
axes[2].set_title('Distribucion Indice de gasto por genero')
plt.tight_layout()
plt.show()
print("\n" + "="*80 + "\n")
#Preprocesamiento de los datos
#Algoritmos como Kmeans se basa en distancias entonces los datos deben estar escalados

df_codificado = pd.get_dummies(df, columns=['Gender'], drop_first=True) #drop_first evita colinealidad
print(df_codificado.head())
print("\n" + "="*80 + "\n")

caract_num = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
X = df_codificado[caract_num]
print(X.head())

print("\n" + "="*80 + "\n")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled[:5])
print("\n" + "="*80 + "\n")

#Definir k optimo
inercia = []
rango_k = range(1,11)

for k in rango_k:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    kmeans.fit(X_scaled)
    inercia.append(kmeans.inertia_)

plt.figure(figsize=(8,6))
plt.plot(rango_k, inercia, marker='o', linestyle='--')
plt.xlabel('Numero de clusters (k)')
plt.xticks(rango_k)
plt.ylabel('Inercia')
plt.title('Metodo del codo para KMeans')
plt.grid(True)
plt.show()

#Coeficiente de silueta
silhouette_scores = []

for k in range(2,11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    labels = kmeans.fit_predict(X_scaled)
    silhouette_scores.append(silhouette_score(X_scaled, labels))

print("\n" + "="*80 + "\n")

plt.figure(figsize=(8,6))
plt.plot(range(2,11), silhouette_scores, marker='o', linestyle='--')
plt.xlabel('Numero de clusters (k)')
plt.xticks(range(2,11))
plt.ylabel('Coeficiente de silueta')
plt.title('Metodo silueta para KMeans')
plt.grid(True)
plt.show()
print("\n" + "="*80 + "\n")

#Entrenar el modelo con el K optimo = 6

kmeans = KMeans(n_clusters=6, random_state=42, n_init='auto')
kmeans.fit(X_scaled)
df['Cluster'] = kmeans.labels_

print(df.head())
print("\n" + "="*80 + "\n")
#Aplicacion de clustering jerarquico (aglomerativo - Divisivo)
#Linkage usa la distancia minima entre puntos de dos cluster - Ward metodo mas usado minimiza la varianza total dentro de los cluster

Z = linkage(X_scaled, method='ward')

plt.figure(figsize=(15,8))
# z es la matriz de enlace de la funcion linkage que realiza el agrupamiento jerarquico informacion de la distancia y la union de los cluster, truncate es el metodo de corte, con p establecimos cual va a ser los ultimos cluster
dendrogram(Z, labels=df.index, truncate_mode='lastp', p=12)
plt.xlabel('Indice de muestra')
plt.ylabel('Distancia euclidiana')
plt.title('Dendrograma de clustering jerarquico')
plt.show()

#Aplicacion del clustering aglomerativo
print("\n" + "="*80 + "\n")
agg_clustering = AgglomerativeClustering(n_clusters=4)
df['Agg cluster'] = agg_clustering.fit_predict(X_scaled)

print(df['Agg cluster'].value_counts())
print("\n" + "="*80 + "\n")


#Aplicacion de la mezcla gaussiana, indica la probabilidad de que un punto pertenezca a cada cluster

gmm = GaussianMixture(n_components=6, random_state=42)
gmm.fit(X_scaled)
df['GMM cluster'] = gmm.predict_proba(X_scaled).round(5)
print(df.head())

#PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print(f'Varianza explicada por los dos componentes principales: {pca.explained_variance_ratio_.sum():.2f}')

#TSNE
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)

fig, axes = plt.subplots(2,3, figsize=(20,12))
fig.suptitle('Visualizacion de clusters', fontsize=20)

#Kmeans con PCA
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=df['KM Cluster'], ax=axes[0,0], palette='viridis')
axes[0,0].set_title('Kmeans con PCA')
axes[0,0].set_xlabel('Componente principal 1')
axes[0,0].set_ylabel('Componente principal 2')

#Agglomerative con PCA
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=df['Agg cluster'], ax=axes[0,1], palette='viridis')
axes[0,1].set_title('Clustering jerarquico con PCA')
axes[0,1].set_xlabel('Componente principal 1')
axes[0,1].set_ylabel('Componente principal 2')

#GMM con PCA
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=df['GMM cluster'], ax=axes[0,2], palette='viridis')
axes[0,2].set_title('GMM con PCA')
axes[0,2].set_xlabel('Componente principal 1')
axes[0,2].set_ylabel('Componente principal 2')

#Kmeans con TSNE
sns.scatterplot(x=X_tsne[:,0], y=X_tsne[:,1], hue=df['KM Cluster'], ax=axes[1,0], palette='viridis')
axes[1,0].set_title('Kmeans con TSNE')
axes[1,0].set_xlabel('TSNE 1')
axes[1,0].set_ylabel('TSNE 2')

#Agglomerative con TSNE
sns.scatterplot(x=X_tsne[:,0], y=X_tsne[:,1], hue=df['Agg cluster'], ax=axes[1,1], palette='viridis')
axes[1,1].set_title('Clustering jerarquico con TSNE')
axes[1,1].set_xlabel('TSNE 1')
axes[1,1].set_ylabel('TSNE 2')

#GMM con TSNE
sns.scatterplot(x=X_tsne[:,0], y=X_tsne[:,1], hue=df['GMM cluster'], ax=axes[1,2], palette='viridis')
axes[1,2].set_title('GMM con TSNE')
axes[1,2].set_xlabel('TSNE 1')
axes[1,2].set_ylabel('TSNE 2')