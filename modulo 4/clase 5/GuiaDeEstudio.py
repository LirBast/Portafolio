import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

## Datos simulados (Dos distribuciones normales)

data1=np.random.randn(1000)*1.5+2
data2=np.random.randn(1000)*1.0+2

### Histograma con comparacion de distribuciones

sns.histplot(data1,kde=True,color='blue',label='Grupo 1',bins=30)
sns.histplot(data2,kde=True,color='red',label='Grupo 2',bins=30)
plt.title('Comparacion de Distribucion')
plt.legend()
plt.show()

