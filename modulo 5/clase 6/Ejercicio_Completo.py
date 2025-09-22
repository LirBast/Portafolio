# Actividad asignada:
 
# Asignación: Análisis Estadístico del Dataset de Precios de Vivienda en California

# Parte I: Carga y Exploración Exhaustiva
# Exportar el dataset en formato CSV
# Explorar el dataset de forma completa
# Eliminar o rellenar los valores vacíos (de existir)
# Parte II: Prueba del Teorema del Límite Central (TCL)
# Demostrar el Teorema del Límite Central con la variable que mide el valor medio de las viviendas. Analizar cómo se comporta la distribución de las medias muestrales.

 
# Dado que la distribución normal estándar no es conocida en un escenario real, utilizar la distribución t de Student para estimar el rango de valores del precio promedio real de las viviendas.
 
# Niveles de confianza requeridos: 95% y 99%
 
# Parte IV: Inferencia para la Proporción
# Muchas viviendas están próximas al océano.
 
# Estimar la proporción de viviendas que están cerca del mar y construir intervalos de confianza para esa proporción.
 
# Niveles de confianza requeridos: 95% y 99%
 
# Parte V: Visualización con Seaborn
# Utilizar gráficos conocidos para descubrir patrones y hallazgos interesantes en los datos.
 
# Parte VI: Cálculo del Tamaño Muestral Requerido (Mínimo)
# Determinar cuántas viviendas hay que usar para estimar el precio promedio.
# Calcular el tamaño muestral mínimo requerido
import pandas as pd
import numpy as np
import kagglehub
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm , ttest_1samp , t

# Descarga el dataset desde KaggleHub
path = kagglehub.dataset_download("camnugent/california-housing-prices")

print("Path to dataset files:", path)

archivos = os.listdir(path)
print("Archivos disponibles:", archivos)

# Ruta al archivo CSV
ruta_csv = os.path.join(path, 'housing.csv')

# Cargar el archivo en un DataFrame
df = pd.read_csv(ruta_csv)

# Mostrar las primeras filas
print(df.head())

print(df.info())

print(df.describe())

print(df['total_bedrooms'].isnull().value_counts())

precio_poblacion = df['median_house_value']
media_precio_poblacional = precio_poblacion.mean()
desv_estandar_precios = precio_poblacion.std()

print(f'el valor de la media poblacional es de: {media_precio_poblacional:.2f}' )
print(f'el valor de la desviacion estandar poblacional es de: {desv_estandar_precios:.2f}' )


tam_muestra_tlc = 50
n_muestra_tlc = 400

medias_muestrales = []

for _ in range(n_muestra_tlc):
    muestra_temporal = np.random.choice(precio_poblacion, size =tam_muestra_tlc, replace= True)
    media_muestra = muestra_temporal.mean()
    medias_muestrales.append(media_muestra)


plt.figure(figsize=(8,6))
sns.histplot(medias_muestrales, kde = False, bins= 50, color="#D6A213", edgecolor='black', stat = 'density', label = 'Distribuciones de Medias Muestrales', legend= True)
sns.kdeplot(medias_muestrales, color="#E71010A6")
x = np.linspace(min(medias_muestrales), max(medias_muestrales),100)
plt.plot(x , norm.pdf(x, loc=media_precio_poblacional, scale = desv_estandar_precios/np.sqrt(tam_muestra_tlc)), color="#3E8CCC", linestyle ='--',linewidth = 2, label = ' Distribucion normal teorica' )
plt.title(' Distribucion muestral de medias de precios')
plt.ylabel(' Media de los precios de las viviendas')
plt.grid(True, linestyle ='-', alpha = 0.6)
plt.show()

 
# Parte III: Cálculo de Intervalo de Confianza
# Calcular el intervalo de confianza para el verdadero precio promedio de las viviendas (utilizar una sola muestra grande).

