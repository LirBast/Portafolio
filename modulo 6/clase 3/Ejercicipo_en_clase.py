import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler, StandardScaler

data = {'Producto':['Camisa','Pantalon', None, 'Zapatos','Camisa','Camisa'],
        'Precio':[20,40,30,None,20,25],
        'Color':['Rojo','Azul','Verde','Azul','Rojo','Rojo']}

df = pd.DataFrame(data)

print(df)

df_sin_nulos = df.dropna()
print('\n')
print(df_sin_nulos)

df_limpio = df_sin_nulos.drop_duplicates()

print('\n')
print(df_limpio)

df_limpio= df_limpio.reset_index(drop = True)
print('\n')
print(df_limpio)

le = LabelEncoder()
df_limpio['Producto_Encode']=le.fit_transform(df_limpio['Producto'])
print('\n')
print(df_limpio)

print('\n')
print(f'Mapeo del LabelEncoder para Productos: {list(le.classes_)}')

print('\n')
df_encode = pd.get_dummies(df_limpio, columns = ['Color'], prefix = 'Color')
print(df_encode)