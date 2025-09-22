import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN, KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

np.random.seed(42)
import os
import kagglehub

# Download latest version
path = kagglehub.dataset_download("vjchoudhary7/customer-segmentation-tutorial-in-python")

print("Path to dataset files:", path)

print("Archivos disponibles:", os.listdir(path))
dataset_path = os.path.join(path, "Mall_Customers.csv")
df = pd.read_csv(dataset_path)

print("Información del dataset:")
print(f"Forma del dataset: {df.shape}")
print(f"Valores faltantes: {df.isna().sum().sum()}")
print(f"Filas duplicadas: {df.duplicated().sum()}")

df2 = df.copy()
if 'CustomerID' in df2.columns:
    df2.drop(columns='CustomerID', axis=1, inplace=True)
if 'Gender' in df2.columns:
    df2['Gender'] = df2['Gender'].map({'Male': 1, 'Female': 0}).astype('int64')

features = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)'] #Seleccion variables relevantes

if 'Gender' in df2.columns:
    features.append('Gender')

X = df2[features].copy()
print(X.head())

#ajustar los datos, para asegurarnos que toda las variables tenga la misma importancia en la escala a la hora de entrenar el modelo (valor - media)/std para cada columna
escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)
#Los algoritmos kmeans, dbscan son sensible a las distancia por eso se escala
print(X_escalado[:5])

#Elegir el k optimo, metodo del codo
inercia = []
Ks = range(2, 11)

for k in Ks:
  kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
  kmeans.fit(X_escalado) #entrenando para ese k
  inercia.append(kmeans.inertia_) #calculando los errores cuadraticos del modelo (el mas bajo es el mejor o mas optimo)

plt.figure(figsize=(6,4))
plt.plot(list(Ks), inercia, marker='o')
plt.title('Metodo del codo (Elbow method)')
plt.xlabel('Numero de clusters (k)')
plt.ylabel('Inercia SSE')
plt.grid(True)
plt.show()

silhouette_scores = []

for k in Ks:
  kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
  etiqueta = kmeans.fit_predict(X_escalado)
  sil = silhouette_score(X_escalado, etiqueta)
  silhouette_scores.append(sil)

plt.figure(figsize=(6,4))
plt.plot(list(Ks), silhouette_scores, marker='o')
plt.title('Silhouette Score')
plt.xlabel('Numero de clusters (k)')
plt.ylabel('Silhouette Score')
plt.grid(True)
plt.show()

best_k_sil = Ks[int(np.argmax(silhouette_scores))]
best_k_sil, max(silhouette_scores)


#Mejor k

#k_optimo = int(best_k_sil)
k_optimo = 4

print(k_optimo)

kmeans = KMeans(n_clusters=k_optimo, random_state=42, n_init=10)
etiquetas = kmeans.fit_predict(X_escalado)
df_kmeans = df2.copy()
df_kmeans['Cluster'] = etiquetas
centroides_escalados = kmeans.cluster_centers_

#PCA se reducen las dimensiones
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_escalado)
centroides_pca = pca.transform(centroides_escalados)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=etiquetas, cmap='viridis', s=40)
plt.scatter(centroides_pca[:,0], centroides_pca[:,1],color='red', s=200, marker='X')
plt.title(f'Kmeans k ={k_optimo} N PCA (2D)')
plt.xlabel('Componente Principal 1 (PC1)')
plt.ylabel('Componente Principal 2 (PC2)')
plt.grid(True)
plt.show()

perfil = (df_kmeans.groupby('Cluster')[['Age', 'Annual Income (k$)', 'Spending Score (1-100)'] +
 (['Gender'] if 'Gender' in df_kmeans.columns else [])].agg(['count','mean','median','min','max']).round(2))

perfil

sil_final = silhouette_score(X_escalado, etiquetas)
print('Silhouette Score final:', sil_final)

dbscan = DBSCAN(eps=0.9, min_samples=5)
etiquetas_dbscan = dbscan.fit_predict(X_escalado)
df_dbscan = df2.copy()
df_dbscan['DBSCAN'] = etiquetas_dbscan
df_dbscan['DBSCAN'].value_counts().sort_index()

mask = etiquetas_dbscan != -1

if mask.sum() > 0 and len(np.unique(etiquetas_dbscan[mask])) > 1:
  sil_dbscan = silhouette_score(X_escalado[mask], etiquetas_dbscan[mask])
else:
  sil_dbscan = np.nan

print('Silhouete dbscan: ',sil_dbscan)

X_dbscan_pca = pca.fit_transform(X_escalado)

plt.figure(figsize=(6, 5))
plt.scatter(X_dbscan_pca[:, 0], X_dbscan_pca[:, 1], c=etiquetas_dbscan, cmap='viridis', s=40)
plt.title('DBSCAN en espacio PCA (2D)')
plt.xlabel('Componente Principal 1 (PC1)')
plt.ylabel('Componente Principal 2 (PC2)')
plt.grid(True)
plt.show()

#Prefiero dbscan a kmeans cuando quiero