## Gráficos de Variables Categóricas: Barplot, Countplot, Boxplot Y Violinplot.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Datos de ejemplo

datos=pd.DataFrame({ 'categoria':['A','B','C','A','B','C','A','B','C'],
                  'valor':[10,15,7,12,18,9,14,20,11]})

## Crear el barplot

sns.barplot(x='categoria',y='valor',data=datos,palette='Blues')
plt.title('Promedio de valor por categoria')
plt.show()

### countplot(): Conteo de observaciones por categoría

sns.countplot(x='categoria',data=datos,palette='pastel')
plt.title('Distribucion de Observaciones por categoria')
plt.show()

#### boxplot(): Distribución de una variable numérica por categorías

sns.boxplot(x='categoria',y='valor',data=datos,palette='Set2')
plt.title('Distribucion de valores por categoria')
plt.show()

##### violinplot(): Combinación de boxplot() y estimación de densidad

sns.boxplot(x='categoria',y='valor',data=datos,palette='muted')
plt.title('Distribucion y Densidad de valores por categoria')
plt.show()