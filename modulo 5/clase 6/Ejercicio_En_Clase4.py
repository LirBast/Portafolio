import numpy as np
from scipy import stats
from statsmodels.stats.power import TTestIndPower

# Parámetros
alfa = 0.05       # Nivel de significancia (error tipo I)
power = 0.8        # Potencia deseada (1 - error tipo II)
tam_efecto = 0.5   # Tamaño del efecto (Cohen's d)

# Inicializar clase para prueba t de dos muestras independientes
analisis = TTestIndPower()

# Calcular tamaño de muestra por grupo
n_muestra = analisis.solve_power(effect_size=tam_efecto, power=power, alpha=alfa)

print(f"Tamaño de muestra necesario por grupo: {n_muestra}")
