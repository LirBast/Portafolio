### 2.- Gráficos de Dispersión y Correlación de Variables: Joinplot, Pairplot.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Datos de ejemplo

np.random.seed(42)

data=pd.DataFrame({ 'Ingresos':np.random.normal(50000,10000,200),
                  'Gastos':np.random.normal(30000,8000,200)})

## crear el joinplot

sns.jointplot(x='Ingresos',y='Gastos',data=data,kind='reg',color='blue')
plt.show()

## pairplot(): Matriz de gráficos de dispersión

sns.pairplot(data)
plt.show()