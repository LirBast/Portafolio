import numpy as np
from scipy.stats import t

# Datos
media_muestral = 50
desv_muestral = 10
tam_muestra = 20
lvl_confianza = 0.95

# Grados de libertad
grado_libertad = tam_muestra - 1

# Valor crítico t
crit_t = t.ppf(1 - (1 - lvl_confianza) / 2, grado_libertad)
print(f'Valor crítico t para {lvl_confianza * 100}% de confianza: {crit_t:.2f}, y {grado_libertad:.2f} grados de libertad')

# Error estándar
error_std = desv_muestral / np.sqrt(tam_muestra)
print(f'Error estándar: {error_std:.2f}')

# Margen de error
marg_error = crit_t * error_std
print(f'Margen de error: {marg_error:.2f}')

# Intervalo de confianza
lim_inf = media_muestral - marg_error
lim_sup = media_muestral + marg_error

print(f'El límite inferior del intervalo de confianza con {lvl_confianza * 100}% es: {lim_inf:.2f}')
print(f'El límite superior del intervalo de confianza con {lvl_confianza * 100}% es: {lim_sup:.2f}')
