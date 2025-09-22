import numpy as np
from scipy import stats
import math

Libros_prestados = [6, 4, 5, 7, 3, 6, 8, 4, 5, 6, 7, 5, 4, 6, 5, 7, 6, 4, 5, 8, 5, 6, 4, 7, 5, 6, 4, 5, 7, 6]

# # El nivel de significancia (α) es 0.05. Los estudiantes deben realizar una prueba de hipótesis para 
# # determinar si hay suficiente evidencia para rechazar la hipótesis nula. 

# 1. Formular las hipótesis (H0 y H1) (1 punto): 


### Hipotesis nula (h0): los estudiantes toman en promedio 5 libros por mes
### hipotesis alternativa(h1): la cantidad de libros que toman los estudiantes es diferente del promedio (5)

# 2 Calcular la media muestral (𝑿 ̅) y la desviación estándar muestral (s) (2 puntos):

tamano_muestra = len(Libros_prestados)

promedio_muestra = np.mean(Libros_prestados)

desviacion_estandar_muestral = np.std(Libros_prestados, ddof=1)


print(f'el tamaño de la muestra es: {tamano_muestra}')

print(f'el promedio de la muestra es: {promedio_muestra:.2f}')

print(f"Desviación estándar muestral: {desviacion_estandar_muestral:.4f}")



# 3. Calcular el estadístico de prueba (t) (2 puntos): 

promedio_historico = 5

t_stat = (promedio_muestra - promedio_historico ) / (desviacion_estandar_muestral / math.sqrt(tamano_muestra))

print(f'el estadistico de t es: {t_stat:.4f}')


# 4. Determinar el valor-p (2 puntos): 
# Usar tablas de distribución t o software (Python) para calcular el valor-p para una prueba bilateral. 

# Grados de libertad
df = tamano_muestra - 1

# p-valor bilateral
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

print(f"Grados de libertad: {df}")
print(f"Valor p: {p_value:.4f}")

# 5. Tomar una decisión basada en el valor-p y el nivel de significancia (α) (1 punto): 
# • Comparar el valor-p con α=0.05. 
# • Decidir si se rechaza o no se rechaza H0. 

# Analisis

# # Dado que el valor p obtenido (0.0299) es menor que el nivel de significancia establecido (α = 0.05), 
# # se rechaza la hipótesis nula. Esto significa que existe evidencia estadísticamente significativa para afirmar que
# # el número promedio de libros prestados por los estudiantes no es igual a 5, como lo indicaba el promedio histórico.

# # En otras palabras, los resultados sugieren que los estudiantes actualmente están tomando en promedio
# # una cantidad de libros diferente a 5 por mes, siendo la media observada en la muestra (5.53) ligeramente
# # mayor al histórico.