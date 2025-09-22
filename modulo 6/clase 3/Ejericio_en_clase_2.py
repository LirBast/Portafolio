
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler


data = {'Producto':['Camisa','Pantalon', None, 'Zapatos','Camisa'],
        'Color':['Rojo','Azul','Verde','rojo','ROJO'],
        'Tamaño':['S', 'M','L', None, 'S'],
        'Precio':[100, 200, 150, np.nan,150]}

df = pd.DataFrame(data)
print("Datos Crudos: \n", df)

df_limpio = df.dropna()
print(df_limpio)

df_limpio["Color"] = df_limpio["Color"].str.lower()
print(df_limpio)

le = LabelEncoder()
df_limpio["Tamaño_Encoded"] = le.fit_transform(df_limpio["Tamaño"])
print("Data Frame con Label Econder: \n", df_limpio)


ohe = OneHotEncoder()
color_encoded = ohe.fit_transform(df_limpio[["Color"]]).toarray()
print("One Hot Encoder para Color: \n", color_encoded)

min_max = MinMaxScaler()
df_limpio["Precio_Min_Max"] = min_max.fit_transform(df_limpio[["Precio"]])
print("Data Frame con Precio Minimo Maximo: \n", df_limpio)

ss = StandardScaler()
df_limpio["Precio_ss"] = ss.fit_transform(df_limpio[["Precio"]])
print(df_limpio[["Precio", "Precio_Min_Max", "Precio_ss"]])