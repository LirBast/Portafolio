# 1.- Cargar el archivo CSV en un DataFrame

import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("mkechinov/ecommerce-purchase-history-from-electronics-store")

print("Path to dataset files:",path)
archivos=os.listdir(path)
print("Archivos disponibles:",archivos)

Datos=os.path.join(path,"kz.csv")

df=pd.read_csv(Datos)


# 2.- Mostrar las primeras 5 filas del archivo

print(df.head())
('\n')
# 3.- Extraer solo las columnas "Producto" y "Precio" 

print(df[['product_id','price']])
print('\n')
# 4.- Filtrar los productos cuyo precio sea mayor a 50

Precio_mayor_50=df[df['price']>50]
print(Precio_mayor_50[['product_id','category_id','price']])
print('\n')

# 5.- Guardar el DataFrame filtrado en un nuevo archivo CSV

df_filtrado=df[['product_id','category_id','price']]

df_filtrado.to_csv("productos_precios.csv", index=False)

print("Archivo 'productos_precios.csv' guardado exitosamente.")