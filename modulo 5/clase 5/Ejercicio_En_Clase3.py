import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu_muestral = 50
desv_pobla = 10
tam_muestra = 36
lvl_confianza = 0.95 ## nivel de confianza

z_critic = norm.ppf(1 - (1 - lvl_confianza)/2) 

print(f'Valor critico z para {lvl_confianza * 100} % de confianza es: {z_critic:.2f}')

Error_estandar = desv_pobla/np.sqrt(tam_muestra)

print(f'El error estandar es: {Error_estandar:.2f}')

marge_error = z_critic * Error_estandar

print(marge_error)


lim_inf = mu_muestral - marge_error
lim_sup = mu_muestral + marge_error

print(f'El intervalo inferior de confianza con un {lvl_confianza * 100} % es {lim_inf:.2f}')
print(f'El intervalo superior de confianza con un {lvl_confianza * 100} % es {lim_sup:.2f}')