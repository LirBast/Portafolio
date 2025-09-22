### Gráficos de Matrices: Heatmap

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Crear un DataFrame con datos aleatorios

np.random.seed(42)

dattos=pd.DataFrame(np.random.rand(6,6),
                    columns=['A','B','C','D','E','F'])

# ## Crear el heatmap

sns.heatmap(dattos,cmap='coolwarm',annot=True,fmt='.2f',linewidths=0.5)
plt.title('Mapa de calor de Datos aleatorios')
plt.show()

### Uso en Matrices de Correlación

df=pd.DataFrame({'Ventas':[200,220,250,270,300,320],
                 'Publicidad':[20,25,28,30,35,40],
                 'Satisfaccion':[3.5,4.0,4.2,4.5,4.8,5.0]})

### calcular la matriz de correlacion

correlacion_matrix=df.corr()

#### Crea el heatmap de la matriz de correlacion

sns.heatmap(correlacion_matrix,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5)
plt.title('Mapa de calor de Correlaciones')
plt.show()