# -----------------------------------------------
# Análisis Estadístico del Dataset de Precios de Vivienda en California
# Partes I a VI completadas
# -----------------------------------------------

import pandas as pd
import numpy as np
import kagglehub
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, t

# -----------------------------------------------
# Parte I: Carga y Exploración Exhaustiva
# -----------------------------------------------

# Descargar el dataset desde KaggleHub
path = kagglehub.dataset_download("camnugent/california-housing-prices")
print("Path to dataset files:", path)

archivos = os.listdir(path)
print("Archivos disponibles:", archivos)

# Ruta al archivo CSV
ruta_csv = os.path.join(path, 'housing.csv')

# Cargar los datos
df = pd.read_csv(ruta_csv)

# Exploración general
print(df.head())
print(df.info())
print(df.describe())

# Manejo de valores faltantes
print("Valores nulos en 'total_bedrooms':")
print(df['total_bedrooms'].isnull().value_counts())

# Rellenar valores faltantes con la mediana
df['total_bedrooms'].fillna(df['total_bedrooms'].median(), inplace=True)

# -----------------------------------------------
# Parte II: Teorema del Límite Central (TLC)
# -----------------------------------------------

# Variable de interés: median_house_value
precio_poblacion = df['median_house_value']
media_precio_poblacional = precio_poblacion.mean()
desv_estandar_precios = precio_poblacion.std()

print(f"Media poblacional: {media_precio_poblacional:.2f}")
print(f"Desviación estándar poblacional: {desv_estandar_precios:.2f}")

# Simulación de medias muestrales
tam_muestra_tlc = 50
n_muestra_tlc = 400

medias_muestrales = [
    np.mean(np.random.choice(precio_poblacion, size=tam_muestra_tlc, replace=True))
    for _ in range(n_muestra_tlc)
]

# Gráfico del TLC
plt.figure(figsize=(8, 6))
sns.histplot(medias_muestrales, bins=50, color="#D6A213", edgecolor="black", stat="density", label="Medias muestrales")
sns.kdeplot(medias_muestrales, color="#E71010A6", label="KDE real")
x = np.linspace(min(medias_muestrales), max(medias_muestrales), 100)
plt.plot(x, norm.pdf(x, loc=media_precio_poblacional, scale=desv_estandar_precios / np.sqrt(tam_muestra_tlc)),
         color="#3E8CCC", linestyle='--', linewidth=2, label="Normal teórica")
plt.title("Distribución de Medias Muestrales (TLC)")
plt.xlabel("Precio medio")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# -----------------------------------------------
# Parte III: Intervalos de Confianza con t de Student
# -----------------------------------------------

# Tamaño de la muestra para el IC
n = 100
np.random.seed(42)
muestra = np.random.choice(precio_poblacion, size=n, replace=True)

# Estadísticas muestrales
media_muestra = np.mean(muestra)
desv_estandar_muestral = np.std(muestra, ddof=1)
error_estandar = desv_estandar_muestral / np.sqrt(n)
df_grados = n - 1

# Niveles de confianza
confianzas = [0.95, 0.99]

for confianza in confianzas:
    t_critico = t.ppf(1 - (1 - confianza) / 2, df_grados)
    margen_error = t_critico * error_estandar
    limite_inferior = media_muestra - margen_error
    limite_superior = media_muestra + margen_error

    print(f"\nIntervalo de confianza al {int(confianza*100)}%:")
    print(f"Media muestral: {media_muestra:.2f}")
    print(f"Error estándar: {error_estandar:.2f}")
    print(f"t crítico: {t_critico:.3f}")
    print(f"Intervalo: ({limite_inferior:.2f}, {limite_superior:.2f})")

# -----------------------------------------------
# Parte IV: Inferencia para la Proporción (Cerca del Océano)
# -----------------------------------------------

# Calcular proporción de viviendas cerca del océano
proximas_mar = df['ocean_proximity'] == 'NEAR OCEAN'
n_total = len(df)
x_exito = proximas_mar.sum()
p_hat = x_exito / n_total

print(f"\nProporción muestral cerca del océano: {p_hat:.4f} ({x_exito} de {n_total})")

for confianza in confianzas:
    z = norm.ppf(1 - (1 - confianza) / 2)
    error = z * np.sqrt((p_hat * (1 - p_hat)) / n_total)
    li = p_hat - error
    ls = p_hat + error
    print(f"IC del {int(confianza*100)}% para proporción: ({li:.4f}, {ls:.4f})")

# -----------------------------------------------
# Parte V: Visualización con Seaborn
# -----------------------------------------------

plt.figure(figsize=(12, 6))

# Distribución del valor medio de las viviendas
plt.subplot(1, 2, 1)
sns.histplot(df['median_house_value'], kde=True, color='teal')
plt.title('Distribución del valor medio de viviendas')
plt.xlabel('Valor medio de la vivienda')
plt.ylabel('Frecuencia')

# Relación entre ingresos y valor de la vivienda
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='median_income', y='median_house_value', hue='ocean_proximity', palette='Set2', alpha=0.6)
plt.title('Ingreso medio vs Valor medio de vivienda')
plt.xlabel('Ingreso medio')
plt.ylabel('Valor medio de vivienda')
plt.tight_layout()
plt.show()

# -----------------------------------------------
# Parte VI: Cálculo del Tamaño Muestral Requerido
# -----------------------------------------------

# Supongamos:
confianza = 0.95
z = norm.ppf(1 - (1 - confianza) / 2)
margen_error_deseado = 5000  # Por ejemplo, queremos ±5.000 dólares de precisión

# Usar la desviación estándar poblacional estimada
n_requerido = (z * desv_estandar_precios / margen_error_deseado) ** 2
n_requerido = int(np.ceil(n_requerido))

print(f"\nTamaño muestral mínimo requerido (±${margen_error_deseado} con {int(confianza*100)}% de confianza): {n_requerido} viviendas")
