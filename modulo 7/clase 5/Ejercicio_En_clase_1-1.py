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
print("Primeras 5 filas del DataFrame:")
print(df.head())

pca_2d = PCA(n_components=2)
pca_resultado_2d = pca_2d.fit_transform(digitos.data) #ajusta el modelo y lo transforma a esas dimensiones

df['PCA1_2D'] = pca_resultado_2d[:,0]
df['PCA2_2D'] = pca_resultado_2d[:,1]

print("\nDataFrame con componentes PCA 2D:")
print(df.head())

pca_3d = PCA(n_components=3)
pca_resultado_3d = pca_3d.fit_transform(digitos.data) #ajusta el modelo y lo transforma a esas dimensiones

df['PCA1_3D'] = pca_resultado_3d[:,0]
df['PCA2_3D'] = pca_resultado_3d[:,1]
df['PCA3_3D'] = pca_resultado_3d[:,2]

print("\nDataFrame con componentes PCA 3D:")
print(df.head())

plt.figure(figsize=(12,8))
sns.scatterplot(data=df, x='PCA1_2D', y='PCA2_2D', hue='Target', palette=sns.color_palette('hsv', 10), legend='full')
plt.title('Visualizacion de digitos con PCA 2D')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.grid(True)
plt.show()

# ===============================================
# 5) VISUALIZACIÓN 3D CON MEJORAS ANTI-SOLAPAMIENTO
# ===============================================

# Versión 1: Gráfico 3D mejorado con transparencia y marcadores pequeños
fig = plt.figure(figsize=(15,10))

# Subplot 1: Versión mejorada con transparencia y marcadores pequeños
ax1 = fig.add_subplot(221, projection='3d')
ax1.scatter3D(df['PCA1_3D'], df['PCA2_3D'], df['PCA3_3D'], 
              c=df['Target'], cmap='hsv', alpha=0.4, s=8)
ax1.set_xlabel('Componente Principal 1')
ax1.set_ylabel('Componente Principal 2')
ax1.set_zlabel('Componente Principal 3')
ax1.set_title('PCA 3D - Transparencia mejorada')
ax1.grid(True)

# Subplot 2: Con jitter leve para separar puntos solapados
ax2 = fig.add_subplot(222, projection='3d')
rng = np.random.default_rng(42)  # semilla fija para reproducibilidad
jitter_scale = 0.3
x_jitter = df['PCA1_3D'] + rng.normal(0, jitter_scale, len(df))
y_jitter = df['PCA2_3D'] + rng.normal(0, jitter_scale, len(df))
z_jitter = df['PCA3_3D'] + rng.normal(0, jitter_scale, len(df))
ax2.scatter3D(x_jitter, y_jitter, z_jitter, 
              c=df['Target'], cmap='hsv', alpha=0.5, s=6)
ax2.set_xlabel('Componente Principal 1')
ax2.set_ylabel('Componente Principal 2')
ax2.set_zlabel('Componente Principal 3')
ax2.set_title('PCA 3D - Con jitter anti-solapamiento')
ax2.grid(True)

# Subplot 3: Puntos únicos (sin duplicados exactos)
ax3 = fig.add_subplot(223, projection='3d')
df_unique = df.drop_duplicates(subset=['PCA1_3D','PCA2_3D','PCA3_3D'])
print(f"\nPuntos originales: {len(df)}, Puntos únicos: {len(df_unique)}")
ax3.scatter3D(df_unique['PCA1_3D'], df_unique['PCA2_3D'], df_unique['PCA3_3D'], 
              c=df_unique['Target'], cmap='hsv', alpha=0.6, s=12)
ax3.set_xlabel('Componente Principal 1')
ax3.set_ylabel('Componente Principal 2')
ax3.set_zlabel('Componente Principal 3')
ax3.set_title('PCA 3D - Solo puntos únicos')
ax3.grid(True)

# Subplot 4: Visualización por densidad
ax4 = fig.add_subplot(224, projection='3d')
# Calculamos densidad por bins 3D
bins = 25
coords = df[['PCA1_3D','PCA2_3D','PCA3_3D']].to_numpy()
H, edges = np.histogramdd(coords, bins=bins)

# Mapear cada punto a su bin para obtener densidad
bin_indices = []
for i in range(3):
    # Asegurar que los índices estén en rango válido
    indices = np.digitize(coords[:,i], edges[i]) - 1
    indices = np.clip(indices, 0, bins-1)
    bin_indices.append(indices)

density = H[bin_indices[0], bin_indices[1], bin_indices[2]]

# Graficar coloreando por densidad
sc = ax4.scatter3D(df['PCA1_3D'], df['PCA2_3D'], df['PCA3_3D'],
                   c=density, cmap='viridis', alpha=0.6, s=8)
ax4.set_xlabel('Componente Principal 1')
ax4.set_ylabel('Componente Principal 2')
ax4.set_zlabel('Componente Principal 3')
ax4.set_title('PCA 3D - Coloreado por densidad')
ax4.grid(True)

# Añadir colorbar para la densidad
plt.colorbar(sc, ax=ax4, shrink=0.5, label='Densidad (puntos por bin)')

plt.tight_layout()
plt.show()