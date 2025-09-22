import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

np.random.seed(0)

data = np.random.rand(100, 4) * 100
columnas = ['Gasto anual', 'Frecuencia visita', 'Edad', 'Promedio de sesion']

df = pd.DataFrame(data, columns=columnas)
data_escalada = StandardScaler()

df_escalado = data_escalada.fit_transform(df)
pca = PCA(n_components=2)

componentes_pca = pca.fit_transform(df_escalado)
df_pca = pd.DataFrame(data=componentes_pca, columns=['CP1', 'CP2'])

print(df_pca.head(),'\n')
print('Esta es la varianza explicada por componente:')
print(pca.explained_variance_ratio_)
print('Esta es la varianza total explicada:\n')
print(np.sum(pca.explained_variance_ratio_))

tsne = TSNE(n_components=2, random_state=42)
df_tsne = tsne.fit_transform(df_escalado)

plt.scatter(df_tsne[:,0],df_tsne[:,1],color='blue')
plt.title('Visualizacion con TSNE')
plt.show()

