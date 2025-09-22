# ===============================================
# VISUALIZACIÓN DEL DATASET LOAD_DIGITS
# ===============================================

import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from mpl_toolkits.mplot3d import Axes3D
 
# ===============================================
# 1) CARGA DEL DATASET DE DÍGITOS
# ===============================================
# Cargamos el dataset de dígitos manuscritos (8x8 píxeles)
# Contiene 1797 imágenes de dígitos del 0 al 9
digitos = load_digits()

# ===============================================
# 2) CONFIGURACIÓN DE LA GRILLA DE SUBPLOTS
# ===============================================
# Creamos una grilla de 10x10 subplots (100 imágenes en total)
# figsize=(8,8): tamaño de la figura completa en pulgadas
# subplot_kw: configuración aplicada a cada subplot individual
#   - xticks=[], yticks=[]: elimina las marcas de los ejes
# gridspec_kw: configuración del espaciado entre subplots
#   - hspace=0.1: espacio vertical entre filas
#   - wspace=0.1: espacio horizontal entre columnas
figura, axes = plt.subplots (10,10, figsize=(8,8),subplot_kw={'xticks':[],'yticks':[]}, gridspec_kw=dict(hspace=0.1,wspace=0.1))

# ===============================================
# 3) ITERACIÓN Y VISUALIZACIÓN DE CADA DÍGITO
# ===============================================
# axes.flat convierte la matriz 10x10 de axes en un array 1D para iterar fácilmente
# enumerate() nos da tanto el índice (i) como el objeto axis (ax)
for i, ax in enumerate(axes.flat):
  # Mostramos la imagen del dígito i-ésimo
  # digitos.images[i]: matriz 8x8 con valores de intensidad de píxeles
  # cmap='binary': mapa de colores blanco y negro
  # interpolation='nearest': no suaviza los píxeles (mantiene aspecto pixelado)
  ax.imshow(digitos.images[i], cmap='binary', interpolation='nearest')
  
  # Añadimos texto con la etiqueta verdadera del dígito
  # (0.05, 0.05): posición en coordenadas relativas del subplot (esquina inferior izquierda)
  # str(digitos.target[i]): convierte la etiqueta numérica a string
  # transform=ax.transAxes: usa coordenadas del sistema de ejes (0-1) en lugar de datos
  # color='green': color del texto
  ax.text(0.05,0.05,str(digitos.target[i]), transform=ax.transAxes, color='green')

# ===============================================
# 4) MOSTRAR LA FIGURA COMPLETA
# ===============================================
# Renderiza y muestra la figura con todas las imágenes
plt.show()

print(f'forma de los datos (muestra, caracteristicas): {digitos.data.shape}') #1797 imagenes, 64 pixeles
print(f'forma de las etiquetas(muestra): {digitos.target.shape}') #1797 etiquetas

df = pd.DataFrame(digitos.data)
df['Target'] = digitos.target
df.head()

pca_2d = PCA(n_components=2)
pca_resultado_2d = pca_2d.fit_transform(digitos.data) #ajusta el modelo y lo transforma a esas dimensiones

df['PCA1_2D'] = pca_resultado_2d[:,0]
df['PCA2_2D'] = pca_resultado_2d[:,1]

df.head()

pca_3d = PCA(n_components=3)
pca_resultado_3d = pca_3d.fit_transform(digitos.data) #ajusta el modelo y lo transforma a esas dimensiones

df['PCA1_3D'] = pca_resultado_3d[:,0]
df['PCA2_3D'] = pca_resultado_3d[:,1]
df['PCA3_3D'] = pca_resultado_3d[:,2]

df.head()

plt.figure(figsize=(12,8))
sns.scatterplot(data=df, x='PCA1_2D', y='PCA2_2D', hue='Target', palette=sns.color_palette('hsv', 10), legend='full')
plt.title('Visualizacion de digitos con PCA 2D')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.grid(True)
plt.show()

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(df['PCA1_3D'], df['PCA2_3D'], df['PCA3_3D'], c=df['Target'], cmap='hsv', alpha=0.7)
ax.set_xlabel('Componente Principal 1')
ax.set_ylabel('Componente Principal 2')
ax.set_zlabel('Componente Principal 3')
ax.set_title('Visualizacion de digitos con PCA 3D')
plt.grid(True)
plt.show()

tsne = TSNE(n_components=2, random_state=42, perplexity=30, max_iter=300) #perplexity es una aproximacion del numero de vecinos mas cercanos
tsne_resultado_2d = tsne.fit_transform(digitos.data)
df['TSNE1_2D'] = tsne_resultado_2d[:,0]
df['TSNE2_2D'] = tsne_resultado_2d[:,1]
df.head()

plt.figure(figsize=(12,8))
sns.scatterplot(data=df, x='TSNE1_2D', y='TSNE2_2D', hue='Target', palette=sns.color_palette('hsv', 10), legend='full')
plt.title('Visualizacion de digitos con TSNE 2D')
plt.xlabel('Componente TSNE 1')
plt.ylabel('Componente TSNE 2')
plt.grid(True)
plt.show()