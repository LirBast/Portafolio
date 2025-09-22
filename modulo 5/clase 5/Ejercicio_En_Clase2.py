import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(45)

p_pobla = 0.4 # proporcion poblacional
muestra = 100
num_sim = 1000
prop_muestrales = []

for _ in range(num_sim):
    num_exitos = np.random.binomial(muestra, p_pobla, size = 1)
    prop_muestrales.append(num_exitos[0] / muestra)

plt.figure(figsize=( 8, 6))
plt.hist(prop_muestrales, bins = 30, color = '#1D53DE' , edgecolor = 'black', density = True, label = 'Distribucion Normal' )
plt.legend()
ax = np.linspace(min(prop_muestrales), max(prop_muestrales) , 100)
error_std = np.sqrt((p_pobla * (1 - p_pobla))/muestra)
plt.plot(ax, norm.pdf(ax , loc= p_pobla, scale=error_std), color = 'red' , label = 'Distribucion normal aproximada')
plt.title('Distribucion Normal de Proporciones')
plt.xlabel('Proporcion muestral')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.show()

