import numpy as np
from scipy.stats import norm

tam_muestra = 300
num_exito = 120
lvl_confianza = 0.95

prop_muestral = num_exito / tam_muestra  # p gorrito
print(f'La proporción muestral es de: {prop_muestral}')

z_crit = norm.ppf(1 - (1 - lvl_confianza) / 2)
print(f'El valor crítico z es: {z_crit:.2f}')

error_std = np.sqrt(prop_muestral * (1 - prop_muestral) / tam_muestra)
print(f'Error estándar: {error_std:.2f}')

marg_error = z_crit * error_std
print(f'Margen de error: {marg_error:.2f}')

lim_inf = prop_muestral - marg_error
lim_sup = prop_muestral + marg_error
print(f'El límite inferior del intervalo de confianza con {lvl_confianza * 100}% es: {lim_inf:.4f}')
print(f'El límite superior del intervalo de confianza con {lvl_confianza * 100}% es: {lim_sup:.4f}')