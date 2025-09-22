import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

mu_poblacional=150
desv_poblacional=20
n_muestras=1000
tamano_muestra=25

medias_muestrales=[]

for _ in range(n_muestras):
    muestra_segada = np.random.gamma(shape=(mu_poblacional/desv_poblacional)**2, scale=desv_poblacional**2/mu_poblacional,size=tamano_muestra)
    media_muestra = np.mean(muestra_segada)
    medias_muestrales.append(np.mean(muestra_segada))

plt.figure(figsize=(10, 6))
sns.histplot(medias_muestrales, kde=True , color='green', bins=30)
plt.axvline(mu_poblacional, color='red',linestyle='dashed', linewidth=2,label='media poblacional')
plt.xlabel('Medias muestrales')
plt.ylabel('Frecuencias')
plt.title('Distribución de las medias muestrales')
plt.legend()
plt.grid(True, axis='y', alpha=0.75)
plt.show()

