import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.DataFrame({'id':range(1,21),
                     'Producto':np.random.choice(['camiseta','pantalon','zapastos','gorras','Calcetines'],20),
                     'Precio':np.round(np.random.uniform(10,100,20)),
                     'Ventas':np.random.randint(1,50,20),
                     'Region':np.random.choice(['norte','Sur','Este','Oeste'],20),
                     'Descuento':np.random.choice([True,False],20),
                     'Calificacion_Cliente':np.random.randint(1,6,20)
                     })

df=pd.DataFrame(data)

# print(data)
# print('---------------------------------------------------------------------------')
# print(df)

df.loc[3,'Precio']=np.nan
df.loc[10,'Ventas']=np.nan
df.loc[15,'Region']=np.nan

print(df.head(5))

print('informacion del data frame')
print(df.info(),'\n')
print('--------------------------')
print('saber cuales son los nulos')
print(df.isnull(),"\n")
print('--------------------------')
print('\sumar la cantidad de nulos')
print(df.isnull().sum(),'\n')
print('Estadisticas descriptivas')
print(df.describe())
# dftemporal=df.drop(columns=['id'])   #permite quitar una columna, que se indica dentro de los corchetes
# print(dftemporal.describe())