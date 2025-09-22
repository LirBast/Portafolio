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

df2=pd.DataFrame(data)
df2.loc[3,'Precio']=np.nan
df2.loc[10,'Ventas']=np.nan
df2.loc[15,'Region']=np.nan


print(df2)
print('--------------------------')
print('Eliminar valores nulos')
# print(df.dropna())  #Elimina las filas con valores nulos
print(df2.dropna(axis=1)) #Elimina las columnas con valores nulos
print("------------------------------------------")
print('La mediana de Precio')
mediaPrecio=df2['Precio'].median()
print(mediaPrecio)
df2['Precio'].fillna(mediaPrecio, inplace=True)
print(df2)

media_ventas=df2['Ventas'].median()
print(media_ventas)
df2['Ventas'].fillna(media_ventas, inplace=True)
print(df2)