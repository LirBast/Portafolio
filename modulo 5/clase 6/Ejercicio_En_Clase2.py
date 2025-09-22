import numpy as np
from scipy import stats

np.random.seed(100)

media = 108
desv = 10
tamano = 30

muestra = np.random.normal(loc=media, scale=desv, size=tamano)

print(muestra.round(2))

t_stat, p_valor = stats.ttest_1samp(muestra, media)

print('t-statistic:', t_stat)
print('p-valor:', p_valor)

if p_valor < 0.05:
    print(f'Se rechaza la hipótesis nula. La media de los tiempos de recuperación es significativamente diferente de {media}.')
else:
    print('No se rechaza la hipótesis nula. No hay evidencia suficiente para afirmar que la media sea diferente.')
