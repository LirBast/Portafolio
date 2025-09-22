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

print(perfil)

# Mostrar los datos de clientes por cada cluster
print("\n" + "="*60)
print("DATOS DE CLIENTES POR CLUSTER")
print("="*60)

for cluster_id in sorted(df_kmeans['Cluster'].unique()):
    print(f"\n--- CLUSTER {cluster_id} ---")
    cluster_data = df_kmeans[df_kmeans['Cluster'] == cluster_id]
    print(f"Número de clientes: {len(cluster_data)}")
    print("\nPrimeros 10 clientes del cluster:")
    print(cluster_data.head(10).to_string(index=False))
    
    print(f"\nEstadísticas del Cluster {cluster_id}:")
    stats = cluster_data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].describe().round(2)
    print(stats)
    
    if 'Gender' in cluster_data.columns:
        gender_dist = cluster_data['Gender'].value_counts()
        print(f"\nDistribución por género:")
        print(f"Mujeres (0): {gender_dist.get(0, 0)}")
        print(f"Hombres (1): {gender_dist.get(1, 0)}")

# Guardar datos de cada cluster en archivos CSV separados
print("\n" + "="*60)
print("GUARDANDO DATOS EN ARCHIVOS CSV")
print("="*60)

for cluster_id in sorted(df_kmeans['Cluster'].unique()):
    cluster_data = df_kmeans[df_kmeans['Cluster'] == cluster_id]
    filename = f'cluster_{cluster_id}_clientes.csv'
    cluster_data.to_csv(filename, index=False)
    print(f"Cluster {cluster_id}: {len(cluster_data)} clientes guardados en '{filename}'")

# Resumen general
print(f"\nRESUMEN GENERAL:")
print(f"Total de clientes: {len(df_kmeans)}")
print(f"Número de clusters: {k_optimo}")
cluster_counts = df_kmeans['Cluster'].value_counts().sort_index()
for cluster_id, count in cluster_counts.items():
    percentage = (count / len(df_kmeans)) * 100
    print(f"Cluster {cluster_id}: {count} clientes ({percentage:.1f}%)")