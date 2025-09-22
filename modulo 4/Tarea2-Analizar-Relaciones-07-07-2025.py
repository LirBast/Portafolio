import pandas as pd

df = pd.read_csv(r"C:\Users\liroy\OneDrive\Escritorio\bootcamp\clases\modulo 4\clase 3\ai_job_dataset.csv")
print(df.head(5))
print('\n')

print(df.shape)               # esto entrega la cantidad de filas y columnas. Para las filas no se cuentan los indices de las columnas
print('\n')
print(df.columns)             # Esto me entrega los nombres de las columnas.
print('\n')
print(df.info())              # Esto me entrega los tipos de datos y los nulos
print('\n')

print(df.isnull().sum())     # esto me indica la suma de todos los nulos de todas las columnas del dataframe
print('\n')

print(df.duplicated().sum())
print('\n')
#### Despues de analizar que el dataFrame no tiene datos nulos pasamaos a las estadisticas descriptivas

print(df.describe())   ## este metodo me entrega todas las estadisiticas pero solo de las columnas que tienen valores numericos
print('\n')
print(df.describe(include='all')) ### al incluir dentro del metodo include=all me entrega las estadisiticas de todos los datos de la tabla, sean numericos o no

## ambas funciones de 'describe' me entregan valores flotantes 

print('\n')

