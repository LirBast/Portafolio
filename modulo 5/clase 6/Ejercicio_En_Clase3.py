import numpy as np
from scipy import stats

# H0: Peso promedio de paquete es 500g (media poblacional = 500) n = 25 media_muestral = 495g desv_muestral = 10g
# H1: media poblacional =/ 500 (bilateral)
 
muestra = np.random.normal(495,10,25)
print(muestra.round(2))
 
t_stats, valor_p = stats.ttest_1samp(muestra, 500)
print("t-statistic:", t_stats)
print("p-valor:", valor_p)
 
if valor_p < 0.05:
    print("Se rechaza la hipótesis nula. La media de la muestra es significativamente diferente de 500.")
else:
    print("No se rechaza la hipótesis nula")
 
 