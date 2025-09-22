import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gamma
import seaborn as sns
 
np.random.seed(42)
 
#Parametros poblacion sesgada
mu = 150
sigma = 20
 
#Para una distribucion GAMMA la media en gamma E[X] = alpha * beta, Var[X] = alpha * beta**2
# alpha = (media_poblacional / sigma_poblacional)**2
# beta = ((sigma_poblacional)**2)/meedia_poblacional
 
alpha = (mu/sigma)**2
beta = (sigma**2)/mu
 
poblacion_sesgada = gamma.rvs(a=alpha,scale=beta,size = 100000) #el metodo genera numeros aleatorios segun los parametros especificados a=forma distribucion sclae = el parametro de la escala
#rvs: Random variates Sampling, Generación de Variables Aleatorias
 
#Graficar la distribucion de la poblacion sesgada
plt.figure(figsize=(14,8))
plt.subplot(1,2,1)
sns.histplot(poblacion_sesgada, kde=True , color='pink', bins=50)
plt.title(f'Distribución poblacional (sesgada a la derecha) media = {np.mean(poblacion_sesgada):.1f} gr, sigma = {np.std(poblacion_sesgada):.1f} gr')
plt.xlabel('Peso manzana (gr)')
plt.ylabel('Frecuencia')
plt.axvline(mu, color='brown', linestyle='--', label='Media poblacional')
plt.legend()
 
#simular la distribucion muestral de la media n=30
numero_muestra = 5000
tam_muestra_tlc = 30
media_muestral_tlc = []
for _ in range(numero_muestra):
  muestra = np.random.choice(poblacion_sesgada, tam_muestra_tlc, replace=True)
  media_muestral_tlc.append(np.mean(muestra))
 
#Graficar la distribucion muestral de la media
plt.subplot(1,2,2)
sns.histplot(media_muestral_tlc, kde=True, color='purple', bins=30)
plt.title(f'Distribución muestral de la media (n={tam_muestra_tlc})')
plt.xlabel('Media muestral')
plt.ylabel('Frecuencia')
plt.axvline(mu, color='brown', linestyle='--', label='Media poblacional')
plt.legend()
plt.tight_layout() #acomodar automaticamente de los parametros en las figuras opt espacio
plt.show()
 
print(f'Media de la poblacion simulada = {np.mean(poblacion_sesgada):.2f} gr, desviacion estandar de la poblacion simulada = {np.std(poblacion_sesgada):.2f} gr')
print(f'La media de las medias muestrales (empirica) = {np.mean(media_muestral_tlc):.2f} gr')
print(f'Error estandar de las medias muestrales (empirico) = {np.std(media_muestral_tlc):.2f} gr')
print(f'Error estandar teorico de las medias muestrales (empirico) = {sigma/np.sqrt(tam_muestra_tlc):.2f} gr')