import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# 1 Análisis Exploratorio de Datos
df = pd.read_csv(r"C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 4\Consolidado\olimpicos.csv")


print(df.head())
print('\n')
print(df.info())
print('\n')
print(df.describe())

###  histograma del número de entrenamientos semanales.


### Histograma

plt.hist(df['Entrenamientos_Semanales'], bins=5, edgecolor='black', color='#150273')
plt.title('Histograma de Entrenamientos_Semanales')
plt.xlabel('Entrenamientos_Semanales')
plt.ylabel('Frecuencia')
plt.grid(True, linewidth = 2, alpha = 0.7)
plt.show()


# 2 Estadística Descriptiva 

print(df.info())
print('\n')
### la tabla nos muestra una forma general de las variables de cada columna
## Atleta es una variable cualtitativa nonimal
## edad es una variable cualitativa nominal
## altura es una variable cuantitativa continua
## peso es una vaiable cuantitativa continua
## deporte es una variable cualitativa nominal
## entrenamiento semanales es una variable cuantitativa discreta
## medallas es una variable cuantitatia discreta
## pais es una variable cualitativa nominal 

#### Calcula la media, mediana y moda de la cantidad de medallas obtenidas. 

print(df.describe())
print('\n')

medallas_obtenidas = df[['Medallas_Totales']]
print('\n')

# promedio de las medallas
print(f'El  promedio de las medallas obtenidas es: {medallas_obtenidas.mean()}')

## moda de la tabla
moda = medallas_obtenidas.mode()
if len(moda) == len(medallas_obtenidas):
    print('La tabla no tiene moda')
else:
    print(f'La moda es: {moda}')

### Mediana de la tabla 
print(f'La mediana de las medallas obtenidas es: {medallas_obtenidas.median().iloc[0]}')


#### Calcula la desviación estándar de la altura de los atletas. 

altura_de_los_atletas = df[['Altura_cm']]

print(altura_de_los_atletas)

desv_altura = altura_de_los_atletas.std()

print(f'La desviacion estandar de los atletras es: {desv_altura.iloc[0]:.2f} cms')

# Identifica valores atípicos en la columna de peso utilizando un boxplot.

print(df[['Peso_kg']])
print('\n')

q1 = df['Peso_kg'].quantile(0.25)
q3 = df['Peso_kg'].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
promedio = df['Peso_kg'].quantile(0.50)


print(f"Q1 (25%): {q1}")
print(f"Q3 (75%): {q3}")
print(f"IQR: {iqr}")
print(f"Límite inferior: {limite_inferior}")
print(f"Límite superior: {limite_superior}")

df_filtrado = df[(df['Peso_kg'] >= limite_inferior) & (df['Peso_kg'] <= limite_superior)]
print('\n')
print(df_filtrado)  
print('\n')
plt.boxplot(df['Peso_kg'])
plt.axhline(q1, linestyle='--', color = "#27F531")  ### Cuartil 25
plt.axhline(q3, linestyle='--', color = '#F54927')  ### cuartil 75
plt.axhline(limite_inferior, linestyle='--', color = "#4D27F5") ### limite inferior
plt.axhline(limite_superior, linestyle='--', color = "#0F0246") ### limite superior
plt.title('Boxplot de Peso_kg')
plt.xlabel('Peso_kg')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

#### al comprobarse con el modo IQR y el boxplot, no hay datos oulieres en la variable peso
### por lo que todos los datos estan dentro del rango

## 3 Análisis de Correlación 

### Calcula la correlación de Pearson entre entrenamientos semanales y medallas totales.

coef, p_valor = stats.pearsonr(df['Entrenamientos_Semanales'], df['Medallas_Totales'])

print(f'El coefciente de correlacion de Pearson: {coef:.2f}')
print(f'P_valor: {p_valor:.2f}')
print('\n')
### El coeficiente de correlacion de pearson arrojo un valor de 0.57, que al ser positivo me indica que a medida que se entrena mas la probabilidad de obtener una medalla aumenta
### Ahora, al tener un p valor de 0.18, que es mayor a 0.05, se puede decir que la correlacion anterior no es significativamente real, por lo que este resultado puede darse por el azar


# Crea un gráfico de dispersión (scatterplot) entre peso y medallas totales con Seaborn

sns.scatterplot(data=df, x='Peso_kg', y='Medallas_Totales', color='red', label='Relación Peso vs Medallas', marker='.')
plt.title('Gráfico de Dispersión: Peso vs Medallas')
plt.xlabel('Peso (kg)')
plt.ylabel('Medallas Totales')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

### el gráfico no muestra una relación clara entre ambas variables, ya que los puntos aparecen muy dispersos
### Se observa que tanto un atleta de bajo peso como otro de alto peso presentan muchas medallas, mientras que
### los valores intermedios se ven bastante parejos. Por ello, la relación es poco apreciable y parece casi nula a
### interpretación del patrón


# 4. Regresión Lineal 

X = df[[ 'Entrenamientos_Semanales']] 
Y = df['Medallas_Totales']

modelo = LinearRegression()
modelo.fit(X,Y)

beta_0 = modelo.intercept_
print(f'El valor del intercepto (es valor de Y cuando X =0 ): {beta_0:.2f}')
beta_1 = modelo.coef_[0]
print(f'El valor de la pendiente ( cuánto cambia Y por cada unidad de aumento en X): {beta_1:.2f}')
print('\n')

Y_pred = modelo.predict(X)

## El intercepto, al ser un valor de Y cuando X es cero, no nos da mucha información de inferencia sobre lo que
## puede pasar entre ambas variables, especialmente porque 'cero entrenamientos' está fuera del rango de
## nuestros datos observados y las medallas no pueden ser negativas. En cambio, la pendiente sí es clave: su
## valor positivo (2.15) nos permite decir que, a medida que aumentan los entrenamientos semanales, también
## aumenta la cantidad de medallas. Por lo tanto, el signo y valor de la pendiente son considerados a la hora de
## hacer un análisis superficial de la relación


## calculo de R^2

r2 = r2_score(Y, Y_pred)
print(f'Coeficiente de determinacion R^2: {r2:.2f}')
print('\n')

## Un R² de 0.32 (32%) indica un ajuste moderado y que la relación entre las variables estudiadas no está 100%
## explicada por los datos de cada una. Por lo tanto, no se puede ser categórico al afirmar que la cantidad de
## entrenamientos semanales generará un aumento de medallas; es probable que existan otras variables que
## convenga analizar para explicar mejor el resultado que se está buscando

sns.regplot(x ='Entrenamientos_Semanales', y ='Medallas_Totales' , data = df)
plt.title('Regresión Lineal: Entrenamientos vs Medallas')
plt.xlabel('Entrenamientos Semanales')
plt.ylabel('Medallas Totales')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 5 Visualización de Datos con Seaborn y Matplotlib

## matriz de correlacion

### para sacar la correlacion se tiene que filtrar la tabla ya que solo funciona con columnas numericas
correlacion = df.select_dtypes(include='number').corr()
print(correlacion)

sns.heatmap(correlacion, annot = True, cmap='Spectral', fmt = '.2f')
plt.title(' Matriz de correlacion')
plt.show()

### Crea un boxplot de la cantidad de medallas por disciplina deportiva

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Deporte', y='Medallas_Totales', color='#8ecae6')
plt.title('Boxplot de Medallas Totales por Disciplina Deportiva')
plt.xlabel('Disciplina Deportiva')
plt.ylabel('Medallas Totales')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()