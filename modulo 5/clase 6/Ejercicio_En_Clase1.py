import numpy as np
from scipy import stats

tiempos_recuperacion = np.array([3,4,5,4,3,4,5,3,5,4])

tiempo_promedio_pb = 5  ### Dias de recuperacion del medicamento actual

### vamos a comparar la media de los datos con la media poblacional

# Hipótesis:
# H0: La media de recuperación con el nuevo medicamento es igual a 5 días
# H1: La media de recuperación con el nuevo medicamento es distinta de 5 días (prueba bilateral)

t_stat, p_valor = stats.ttest_1samp(tiempos_recuperacion, tiempo_promedio_pb)

print('t-stsatics:', t_stat)
print('p-valor:', p_valor)

if p_valor < 0.05:
    print('Se recha la hipotesis nula. La media de los tiempos de recuperacion es significativamente diferente de 5')
else:
    print('No se rechaza la hipotesis nula. No hay evidencia suficiente.')