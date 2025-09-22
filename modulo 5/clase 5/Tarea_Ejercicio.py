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

print(df.head())