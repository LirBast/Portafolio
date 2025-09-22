import pandas as pd
import numpy as np
import kagglehub
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, ttest_1samp, t

# Descarga el dataset desde KaggleHub
path = kagglehub.dataset_download("camnugent/california-housing-prices")

print("Path to dataset files:", path)

archivos = os.listdir(path)
print("Archivos disponibles:", archivos)

# Ruta al archivo CSV
ruta_csv = os.path.join(path, 'housing.csv')

# Cargar el archivo en un DataFrame
df = pd.read_csv(ruta_csv)

df_limpio = df.dropna(subset=['median_house_value'])

# Trabajar con la columna como Serie para evitar errores
muestra_de_precios = df_limpio['median_house_value']

media_muestral = muestra_de_precios.mean()
desv_muestral = muestra_de_precios.std()
tam_muestral_precios = len(muestra_de_precios)
lvl_confianza = 0.95

print(f'La media muestral es {media_muestral:.2f}')

grado_libertad = tam_muestral_precios - 1

t_critico = t.ppf(1 - (1 - lvl_confianza) / 2, df=grado_libertad)

error_std_media = desv_muestral / np.sqrt(tam_muestral_precios)

margen_error = t_critico * error_std_media

lim_inferior = media_muestral - margen_error
lim_superior = media_muestral + margen_error

print(f'Media muestral: {media_muestral:.2f}')
print(f'Desviación estándar muestral: {desv_muestral:.2f}')
print(f'Tamaño de la muestra: {tam_muestral_precios}')
print(f'Grados de libertad: {grado_libertad}')
print(f'Nivel de confianza: {lvl_confianza*100:.1f}%')
print(f'Valor crítico t: {t_critico:.4f}')
print(f'Error estándar de la media: {error_std_media:.2f}')
print(f'Margen de error: {margen_error:.2f}')
print(f'Intervalo de confianza: [{lim_inferior:.2f}, {lim_superior:.2f}]')
