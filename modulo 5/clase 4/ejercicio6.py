import numpy as np
import matplotlib.pyplot as plt

## parametros poblacionales

mu = 150
sigma = 20

n_simulaciones = 10000
medias_observaciones = []
suma = 0
contador = 0
observaciones = np.random.normal(loc= mu, scale = sigma, size = n_simulaciones)
for i in range(n_simulaciones):
    suma += observaciones[i] 
    contador += 1
    medias_observaciones.append(suma / contador)

plt.figure(figsize=(12, 8))
plt.plot(medias_observaciones, label='Media acumulada del peso de manzanas')
plt.axhline(mu, color='purple', linestyle='--', label=f'Media poblacional ({mu} gr)')
plt.xscale('log')  # Escala logarítmica en el eje X
plt.title('Ley de los Grandes Números aplicada al peso de manzanas')
plt.xlabel('Número de observaciones (escala logarítmica)')
plt.ylabel('Media muestral acumulativa')
plt.grid(True)
plt.legend()
plt.show()