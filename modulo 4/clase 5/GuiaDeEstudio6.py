## GRILLAS DE GRÁFICOS: PAIRGRID Y FACETGRID

import seaborn as sns
import matplotlib.pyplot as plt


# Crear dataset del ejemplo

df=sns.load_dataset('iris')

print(df)

## crear la grilla con Pairgrid

g=sns.PairGrid(df,hue='species')

### especificar los tipos de grafico

g.map_diag(sns.histplot) ### Histograma en la diagonal
g.map_offdiag(sns.scatterplot) ## Diagrama de dispersion fuera de la diagonal
g.add_legend()

plt.show()

## Crear la grilla con Facegrid

g=sns.FacetGrid(df,col='species')

## Aplicar un  histograma a cada categoria

g.map(sns.histplot,'sepal_length',bins=10,color='blue')
plt.show()