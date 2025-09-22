import numpy as np
import matplotlib.pyplot as plt

# Parámetros poblacionales
mu_poblacional = 150
sigma_poblacional = 20

# Observaciones simuladas (población)
observaciones_manzanas = np.random.normal(loc=mu_poblacional, scale=sigma_poblacional, size=1000)

# Lista para acumular medias
medias_acumuladas = []

suma = 0
contador = 0

# Recorrer las observaciones y acumular la media paso a paso
for i in range(len(observaciones_manzanas)):
    suma += observaciones_manzanas[i]
    contador += 1
    medias_acumuladas.append(suma / contador)

# Gráfico
plt.figure(figsize=(12, 7))
plt.plot(medias_acumuladas, label='Media acumulada del peso de manzanas')
plt.axhline(mu_poblacional, color='red', linestyle='--', label=f'Media poblacional ({mu_poblacional} gr)')
plt.xscale('log')  # Escala logarítmica en el eje x
plt.title('Ley de los Grandes Números: Peso de Manzanas (Escala Logarítmica)')
plt.xlabel('Número de manzanas muestreadas')
plt.ylabel('Media del peso (gr)')
plt.grid(True)
plt.legend()
plt.show()

# Medias para muestras específicas
print(f'Media con n=10: {np.mean(observaciones_manzanas[:10]):.2f} gr')
print(f'Media con n=100: {np.mean(observaciones_manzanas[:100]):.2f} gr')
print(f'Media con n=1000: {np.mean(observaciones_manzanas[:1000]):.2f} gr')
print(f'Media con n=1000: {np.mean(observaciones_manzanas[:10000]):.2f} gr')
