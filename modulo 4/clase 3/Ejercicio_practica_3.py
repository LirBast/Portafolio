import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


np.random.seed(42)


### 1. Creación de Datos Simulados


### el ejercicio plantea crear variables relacionadas
### Para el caso de usaremos que la presion arterial aumenta con la cantidad de minutos de ejercicio, tomando como base que 120 es la presion arterial normal


minutos_de_ejercicio = np.random.randint(0, 90, 50) ### 50 datos con minutos de ejercicio diarias entre 0 y 90 minutos de ejercicio


presion_arterial = 130 - 0.1 * minutos_de_ejercicio  ### la presion arterial disminuye en funcion de la cantidad de minutos de ejercicio


print(minutos_de_ejercicio)
print(presion_arterial)
print('\n')
df = pd.DataFrame({'Minutos_de_Ejercicio': minutos_de_ejercicio,'Presion_Arterial': presion_arterial})


print(df)
print('\n')
# 2. Construcción de una Tabla de Contingencia


### Crear una tabla de contingencia con datos categóricos (ejemplo: grupo de edad y tipo de dieta).


df = pd.DataFrame({'Grupo_de_edad': np.random.choice(['Niños_y_jovenes(0-14 años)', 'Adultos(15-64 años)', 'Adultos_mayores(65 años o mas)'], size = 15),
                   'Tipo_de_Dieta': np.random.choice(['omnívora', 'vegetariana', 'vegana', 'mediterrania', 'cetogenica'], size= 15)})


tabla_contingencia = pd.crosstab(df['Grupo_de_edad'],df['Tipo_de_Dieta'])


print(tabla_contingencia)


# 3  Visualización con Scatterplot (grafico de dispersion)


### se usaran las variables del primer ejercicio


plt.figure(figsize=(8, 5))
plt.scatter(minutos_de_ejercicio, presion_arterial, color = '#0A113E', alpha = 0.5)
plt.xlabel('Minutos De Ejercicio')
plt.ylabel('Presion Arterial')
plt.title('Relacion Entre Minutos de Ejercicio y Presion Arterial')
plt.grid(True)
plt.show()


# 4 Cálculo del Coeficiente de Correlación de Pearson


coef, p_valor = stats.pearsonr(minutos_de_ejercicio, presion_arterial)
print('\n')
print(f'El coeficiente de correlacion de Pearson es: {coef:.2f}')
print(f'El P valor es: {p_valor:.2f}')


# 5  Reflexión sobre Correlación vs. Causalidad



### despues del analisis se obtuvo que el coeficiente de correlacion de pearson es -1, lo que indica que tienen que correlacion negativa perfecta
#### lo que viene a reforzar que a medida aumentan los minutos de ejercicio, disminuye la presion arterial
### tambien el p valor nos arrojo un dato de cero app, lo que nos quiere decir que la posibilidad de que el resultado sea dado por el azar es practicamente nula
##  lo que hace que la relación sea estadísticamente significativa


### Luego del analisis de los datos tanto visual y numérico se puede apreciar una correlación enter los datos, pero como los ejercicios se hicieron con datos aleatorios y manejados
### es difícil explicar la causalidad de esto. No quiere decir que los datos muestren algo para afirmar de forma categórica que algo está dado por otro, hay un sin fin de variables que
### afectar el resultado obtenido, y este análisis no está viendo todo el contexto para afirmar algo tan categórico, por lo que siempre hay que tomar con pinzas los resultados.