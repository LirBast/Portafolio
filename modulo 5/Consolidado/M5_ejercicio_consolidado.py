# EVALUACIÓN FINAL: DISEÑO Y ANÁLISIS DE UN EXPERIMENTO SOBRE EL 
# RENDIMIENTO ACADÉMICO 
# Imagina que trabajas en una institución educativa interesada en evaluar si un nuevo programa de 
# tutoría mejora el rendimiento académico de los estudiantes. Para ello, se selecciona una muestra de 
# 30 estudiantes, divididos en dos grupos: 
# • Grupo A (15 estudiantes): Recibe el programa de tutoría. 
# • Grupo B (15 estudiantes): No recibe el programa (grupo de control). 
# Los resultados del rendimiento académico se miden mediante un examen estándar, donde las 
# calificaciones oscilan entre 0 y 100 puntos. Los datos obtenidos son los siguientes:

# Grupo A (Tutoría): 85, 90, 78, 88, 92, 80, 86, 89, 84, 87, 91, 82, 83, 85, 88

# Grupo B (Control): 70, 72, 75, 78, 80, 68, 74, 76, 79, 77, 73, 71, 75, 78, 80 

# 1. Diseño del Experimento (1 puntos) 
# • Explica brevemente cómo se podría mejorar el diseño del experimento para reducir 
# posibles sesgos.

# Lo primero que se puede hacer es aumentar la cantidad de estudiantes en la muestra, ya que con tan
# pocos participantes el azar puede influir demasiado y afectar la aleatoriedad. En segundo lugar, es importante
# conocer el desempeño académico previo de los estudiantes antes de la asignación, porque puede
# darse el caso de que algunos alumnos ubicados en el grupo de control tengan ya un rendimiento
# sobresaliente, lo que distorsionaría la medida de comparación. Asimismo, también podría ocurrir la situación
# contraria: que un estudiante con una buena base académica entre al grupo con tutoría y obtenga una buena
# nota, pero no necesariamente gracias al programa, sino porque ya tenía condiciones favorables de antemano.
# Este tipo de casos dificultan aislar y medir con claridad el verdadero efecto de la tutoría.

# Otra mejora posible para fortalecer el experimento sería analizar cuidadosamente el procedimiento de
# selección de los grupos. El enunciado indica que se formaron dos grupos, pero no aclara cómo se realizó
# esa división. Si la asignación no fue completamente aleatoria y, por ejemplo, se hizo de manera intencional
# para reforzar la idea previa de que la tutoría funciona, existiría un sesgo serio en los resultados. De hecho, al
# observar que en el Grupo A la mayoría de los estudiantes presentan calificaciones muy altas, surge la duda de
# si la división fue realmente producto del azar.
# En conclusión, un mejor diseño debería utilizar un mayor número de estudiantes, comprobar el nivel
# base previo y asegurar un proceso de asignación aleatoria y transparente, de modo que cualquier
# diferencia en el rendimiento entre los grupos pueda atribuirse con mayor certeza al programa de tutoría.

# 2. Cálculo de Estadísticas Descriptivas (3 puntos) 
# • Calcula la media y la desviación estándar para ambos grupos. 
# • Representa los datos gráficamente (usando histogramas o diagramas de caja). 

import numpy as np
from scipy import stats
import math
import matplotlib.pyplot as plt

grupo_a_tuto = [85, 90, 78, 88, 92, 80, 86, 89, 84, 87, 91, 82, 83, 85, 88]
grupo_b_contr = [70, 72, 75, 78, 80, 68, 74, 76, 79, 77, 73, 71, 75, 78, 80]

print(grupo_a_tuto)
print(grupo_b_contr)

tamano_muestra = len(grupo_a_tuto)

promedio_muestra_a = np.mean(grupo_a_tuto)
promedio_muestra_b = np.mean(grupo_b_contr)

desviacion_estandar_muestral_a = np.std(grupo_a_tuto, ddof=1)
desviacion_estandar_muestral_b = np.std(grupo_b_contr, ddof=1)


print(f'el tamaño de cada muestra es: {tamano_muestra}')

print(f'el promedio del grupo A es: {promedio_muestra_a:.2f}')
print(f'el promedio del grupo B es: {promedio_muestra_b:.2f}')

print(f'Desviación estándar muestral del grupo A: {desviacion_estandar_muestral_a:.4f}')
print(f'Desviación estándar muestral del grupo B: {desviacion_estandar_muestral_b:.4f}')

# --- Histograma Grupo A ---
plt.figure(figsize = (8, 5))
plt.hist(grupo_a_tuto, bins = 6, color ='skyblue', edgecolor ='black')
plt.title('Histograma Grupo A (Tutoría)')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.grid(True, alpha=0.5)
plt.show()

# --- Histograma Grupo B ---
plt.figure(figsize = (8, 5))
plt.hist(grupo_b_contr, bins = 6, color = 'salmon', edgecolor = 'black')
plt.title('Histograma Grupo B (Control)')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.grid(True, alpha=0.5)
plt.show()

# --- Boxplot comparativo ---
plt.figure(figsize = (8, 5))
plt.boxplot([grupo_a_tuto, grupo_b_contr], labels = ['Tutoría', 'Control'])
plt.title('Diagrama de Caja por Grupo')
plt.ylabel('Calificación')
plt.grid(True, alpha = 0.5)
plt.show()

# 3. Prueba de Hipótesis (4 puntos) 

#  Plantea la hipótesis nula (H0) y alternativa (H1). 
# H0: No hay diferencia en el rendimiento académico entre los dos grupos. 
# H1: El grupo con tutoría tiene un mejor rendimiento académico. 

# • Realiza una prueba t para comparar las medias de ambos grupos. Usa un nivel de 
# significancia (α=0.05). 

# 3. Calcular el estadístico de prueba (t) (2 puntos): 

sp_squared = ((tamano_muestra - 1) * desviacion_estandar_muestral_a**2 + (tamano_muestra - 1) * desviacion_estandar_muestral_b**2) / (tamano_muestra + tamano_muestra - 2)

sp = math.sqrt(sp_squared)

print(f'Varianza combinada (sp²): {sp_squared:.4f}')
print(f'Desviación estándar pooled (sp): {sp:.4f}')

# Paso 2: Error estándar de la diferencia
Error_estandar_diff = sp * math.sqrt(1/tamano_muestra + 1/tamano_muestra)
print(f'Error estándar de la diferencia: {Error_estandar_diff:.4f}')

# Paso 3: Estadístico t
t_stat = (promedio_muestra_a - promedio_muestra_b) / Error_estandar_diff
print(f'Estadístico t: {t_stat:.4f}')

# Paso 4: Grados de libertad
df = tamano_muestra + tamano_muestra - 2
print(f'Grados de libertad: {df}')

# Paso 5: Valor crítico y p-value
t_critico = stats.t.ppf(0.95, df)  # Para α=0.05 una cola
p_value = 1 - stats.t.cdf(t_stat, df)

print(f'Valor crítico t(0.05, {df}): {t_critico:.4f}')
print(f'Valor p (una cola): {p_value:.8f}')

### • Interpreta el valor-p y decide si rechazas o no la hipótesis nula.

### Dado que el valor p obtenido es menor que el nivel de significancia establecido (α = 0.05), se rechaza la
### hipótesis nula (H0). En consecuencia, se acepta la hipótesis alternativa (H1), lo que indica que el programa de
### tutoría tiene un efecto positivo y significativo en el rendimiento académico de los estudiantes. Esto nos
### permite afirmar con evidencia estadística que la tutoría mejora las calificaciones en comparación con el grupo de control.


# 4. Intervalo de Confianza (2 puntos) 
# • Calcula un intervalo de confianza del 95% para la diferencia de medias entre los dos 
# grupos. 
# • Interpreta el resultado.

media_diff = promedio_muestra_a - promedio_muestra_b
t_critico_95 = stats.t.ppf(1 - 0.025, df)  # dos colas para 95%

ic_inf = media_diff - t_critico_95 * Error_estandar_diff
ic_sup = media_diff + t_critico_95 * Error_estandar_diff

print(f'Diferencia de medias observada: {media_diff:.2f}')
print(f'Intervalo de confianza 95%: ({ic_inf:.2f}, {ic_sup:.2f})')

### Los resultados del análisis estadístico permiten concluir que el programa de tutoría tiene un efecto positivo y
### significativo en el rendimiento académico de los estudiantes. La prueba t muestra un valor p
### considerablemente menor al nivel de significancia (α = 0.05), lo que lleva a rechazar la hipótesis nula y
### aceptar la hipótesis alternativa.

### Además, el intervalo de confianza al 95% para la diferencia de medias (aproximadamente entre 7.9 y 13.7
### puntos) confirma que la mejora observada es consistente y estadísticamente relevante. Esto implica que, en
### promedio, los estudiantes que participaron en el programa obtuvieron entre 8 y 14 puntos más que aquellos del grupo de control.
