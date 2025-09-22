##  3.Gráficos de Regresiones: Regplot.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

# Datos de ejemplo

data=pd.DataFrame({ 'edad':np.random.randint(18,65,100),
                  'ingresos':np.random.normal(5000,12000,100)})


## crear el grafico de regresion

sns.regplot(x='edad',y='ingresos',data=data,color='green')
plt.title('Relacion lineal entre Edad e Ingresos')
plt.show