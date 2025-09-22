import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(45)
num_sim = 1000
medias_muestrales = []

for _ in range (num_sim):
    muestra = np.random.normal(loc = 1200, scale = 200, size = 500 )
    medias_muestrales.append(np.mean(muestra))

plt.figure(figsize=( 8, 6))
plt.hist(medias_muestrales, bins = 30, color = '#DDA0DD' , edgecolor = 'black', density = True, label = 'Distribucion Muestral' )
plt.legend()
ax = np.linspace(min(medias_muestrales), max(medias_muestrales) , 100)
plt.plot(ax, norm.pdf(ax , loc= 1200, scale=200/np.sqrt(500)), color = 'red' , label = 'Distribucion normal aproximada')
plt.title('Distribucion Normal de Ingresos')
plt.xlabel('Medias muestral')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.show()


