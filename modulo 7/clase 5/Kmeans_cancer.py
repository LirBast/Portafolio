import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns

import kagglehub

# Descargar la última versión del dataset
path = kagglehub.dataset_download("uciml/breast-cancer-wisconsin-data")

print("Path to dataset files:", path)
print("Files in dataset folder:", os.listdir(path))

# Ajustar el nombre del archivo si es necesario
dataset_path = os.path.join(path, 'data.csv')  # Cambia 'data.csv' si es necesario

df = pd.read_csv(dataset_path)

print(df.head())

# Crear columna numérica para diagnóstico
df['Diagnosis_num'] = df['diagnosis'].map({'B': 0, 'M': 1})

X = df.drop(columns=['id', 'diagnosis', 'Unnamed: 32', 'Diagnosis_num'])

ss = StandardScaler()
X_scaled = ss.fit_transform(X)

inertia = []
ks = range(2, 11)

for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(list(ks), inertia, marker='o')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.grid(True)
plt.show()

k_optimal = 2

km = KMeans(n_clusters=k_optimal, init='k-means++', n_init=10, random_state=42)
clusters = km.fit_predict(X_scaled)
df['Clusters'] = clusters

plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='radius_mean', y='perimeter_mean', hue='Clusters', palette='viridis', s=100)
plt.title('Breast Cancer Tumor Clusters (K=2)')
plt.xlabel('Radius Mean')
plt.ylabel('Perimeter Mean')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()

cluster_resumen = df.groupby('Clusters')[['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean']].mean()
print(cluster_resumen)

tabla_contingencia = pd.crosstab(df['Clusters'], df['Diagnosis_num'])
print(tabla_contingencia)