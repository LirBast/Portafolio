import pandas as pd

df=pd.read_csv('C:\\Users\\liroy\\OneDrive\\Escritorio\\bootcamp\\proyecto\\modulo 3\\clase4\\ventas.csv')


# 1.- Cargar el archivo CSV y visualizar la información
print(df)
print('\n')

# 2. Identificar y manejar valores perdidos 

print(df.isnull())  ## para identificar y visualizar toda la tabla los valores perdidos
print('\n')
print(df.isnull().sum()) ## para contar los valores perdidos en cada columna
print('\n')

## Luego de analisis de la tabla los valores perdidos son 3. Los 2 primeros pertenecen a categoria
## que son variables categoricas nominales. El tercer valor se encuentra en la columna de precio, que es un
## una variable cuantitativa continua.

## Ya sabiendo de que tipo de variables con los valores perdidos se pueden hacer los arreglos correspondientes.

## En este caso dado que la tabla es tan pequeña puede afectar el analisis eliminar esas filas, por lo que se aplica la opcion
## reemplazar con 'Desconocido'

df['Categoría'].fillna('Desconocido',inplace=True)

## En el caso del precio se recomienda rellenar con la media o la mediana de la categoria

df['Precio'].fillna(df['Precio'].mean(),inplace=True)

### En un analisi mas profundo con correlacion de datos, se podria hacer el reemplazo de la variable tomando en
## cuenta la categoria o subgrupo que pertenece dentro de la tabla, en este caso podria hacerse el promedio de solo
## la categoria moda para reemplazar el valor

print(df)

print(df.isnull().sum())

# 3.- Detectar y eliminar registros duplicados

print(df.duplicated())   ### esto me indica las filas que son duplicdas
print(df[df.duplicated()]) ### me indica que filas son las duplicadas con toda su informacion

### al indentificar las filas duplicadas dado el caso se puede:
## 1) Eliminar
## 2) mantenerlos, si despues de analisis si comprubea que es un comprar recurrente de un cliente
## 3) Investigar porque hay duplicados, analizando el porque de su existencia
## 4) Fusionar o agregar, puede darse el caso de que sea otra compra del mismo usuario
## 5) Corregir manualmente, se puede corregir a mano despues de analisi, dado el tamaño del dataset

##### Para este caso, se eliminan esas filas

# df_sin_duplicados=df.drop_duplicates()   ### esta es la forma general de eliminar duplicados
df_sin_duplicados=df.drop_duplicates()
print(df_sin_duplicados)

# 4.- Detectar y manejar outliers en la columna "Cantidad"

### Para detectar los outliers hay que calcular los quartiles q1 y q3, para luego calcular el IQR

q1=df_sin_duplicados['Cantidad'].quantile(0.25) #Primer quartil
q3=df_sin_duplicados['Cantidad'].quantile(0.75) # tercer quatil

IQR=q3-q1

print(f'El cuartil 1 es: {q1}')
print(f'El cuartil 3 es: {q3}')
print(f'El valor del IQR es: {q3-q1}')

df_filtrado=df_sin_duplicados[(df_sin_duplicados['Cantidad'] >= q1 - 1.5 * IQR) & (df_sin_duplicados['Cantidad'] <= q3 + 1.5 * IQR)]

print(df_sin_duplicados['Cantidad'])
print('\n')
print(df_filtrado['Cantidad'])