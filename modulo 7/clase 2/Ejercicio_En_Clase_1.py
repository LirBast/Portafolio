from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

X = np.random.rand(100, 2)*10

k_promedio = KMeans(n_clusters = 5, random_state = 0)

## para normaliar generalemnente aplicamos el .fit

k_promedio.fit(X)

etiquetas = k_promedio.labels_
centroides = k_promedio.cluster_centers_

plt.scatter(X[:,0], ### corodenadas en el eje X
            X[:,1], ### coordenadas en el eje Y
            c = etiquetas, ### Etiquetas de las coordenadas
            cmap = 'viridis')  ### El mapa de colores 
plt.title('Segmentación de clientes con K-Means')
plt.xlabel('Gasto mensual $USD')
plt.ylabel('Frecuencia de compra')
plt.legend()
plt.show()