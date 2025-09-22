import pandas as pd
import numpy as np

df=pd.read_csv('C:\\Users\\liroy\\OneDrive\\Escritorio\\bootcamp\\clases\\modulo 3\\consolidado final\\material complementario evaluacion final\\migracion.csv')
print('\n')
print(df)
print('\n')

# 1.Limpieza y Transformación de Datos

# A.- Valores nulos
print('Valores nulos')
print(df.isnull())  ## para identificar y visualizar toda la tabla los valores perdidos
print('\n')
print(df.isnull().sum()) ## para contar los valores perdidos en cada columna
print('\n')

### Luego del estudio se analizo que no hay valores nulos

## B. Valores duplicados
print('Valores duplicados')
print(df.duplicated())
print('\n')
print(df[df.duplicated()])


### tampoco se encontraron valores duplicados en la tabla

# tabla_resumen=df.describe().round(2)
# print(tabla_resumen)

# Q1_Año=tabla_resumen.loc['25%', 'Año']
# Q3_Año=tabla_resumen.loc['75%', 'Año']

# print(f'El Q1 de Año es: {Q1_Año}')
# print(f'El Q3 de Año es: {Q3_Año}')

# Q1_Cantidad_Migrantes=tabla_resumen.loc['25%', 'Cantidad_Migrantes']
# Q3_Cantidad_Migrantes=tabla_resumen.loc['75%', 'Cantidad_Migrantes']

# print(f'El Q1 de Cantidad_Migrantes es : {Q1_Cantidad_Migrantes}')
# print(f'El Q3 de Cantidad_Migrantes es : {Q3_Cantidad_Migrantes}')

# Q1_PIB_Origen=tabla_resumen.loc['25%', 'PIB_Origen']
# Q3_PIB_Origen=tabla_resumen.loc['75%', 'PIB_Origen']

# print(f'El Q1 de PIB_Origen es : {Q1_PIB_Origen}')
# print(f'El Q3 de PIB_Origen es : {Q3_PIB_Origen}')

# Q1_PIB_Destino=tabla_resumen.loc['25%', 'PIB_Destino']
# Q3_PIB_Destino=tabla_resumen.loc['75%', 'PIB_Destino']

# print(f'El Q1 de PIB_Destino es : {Q1_PIB_Destino}')
# print(f'El Q3 de PIB_Destino es : {Q3_PIB_Destino}')

# Q1_IDH_Origen=tabla_resumen.loc['25%', 'IDH_Origen']
# Q3_IDH_Origen=tabla_resumen.loc['75%', 'IDH_Origen']

# print(f'El Q1 de PIB_Destino es : {Q1_IDH_Origen}')
# print(f'El Q3 de PIB_Destino es : {Q3_IDH_Origen}')

# Q1_IDH_Destino=tabla_resumen.loc['25%', 'IDH_Destino']
# Q3_IDH_Destino=tabla_resumen.loc['75%', 'IDH_Destino']

# print(f'El Q1 de IDH_Destino es : {Q1_IDH_Destino}')
# print(f'El Q3 de IDH_Destino es : {Q3_IDH_Destino}')

# print('\n')
# iqr = tabla_resumen.loc['75%'] - tabla_resumen.loc['25%']
# print(iqr.round(2))


tabla_outliers = df.describe().loc[['25%','75%']].round(2)
tabla_outliers = tabla_outliers.rename(index={'25%':'Q1','75%':'Q3'})
tabla_outliers.loc['IQR (Q3-Q1)'] = tabla_outliers.loc['Q3']-tabla_outliers.loc['Q1']
tabla_outliers.loc['Limite Inferior'] = tabla_outliers.loc['Q1'] - 1.5 * tabla_outliers.loc['IQR (Q3-Q1)']
tabla_outliers.loc['Limite Superior'] = tabla_outliers.loc['Q3'] + 1.5 * tabla_outliers.loc['IQR (Q3-Q1)']


## Se transpone la tabla para hacer más amigable la visualización de los límites por columna
### si ve el resultado del for se puede ver en todas las columnas que visualmnente es mas amiglabe de comprobar los resultados
tabla_outliers_2=tabla_outliers.T
print(tabla_outliers_2)
print('\n')
# print(tabla_outliers)
# print('\n')
### el for lo que hace es recorrer todas las columnas para comparar los limites y posteriormente ver si hay outliers en la tabla

for columna in tabla_outliers:
    limite_inferior = tabla_outliers.loc['Limite Inferior', columna]
    limite_superior = tabla_outliers.loc['Limite Superior', columna]
    outliers_col = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
    if len(outliers_col) > 0:
        print('\n')
        print(f"Outliers detectados en la columna '{columna}':")
        print('\n')
        print('------------------------------------------------ OUTLIERS ---------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------------------------')
        print(outliers_col)

### Dado lo que dice el ejercicio se filtra el outlier detectado. Se elimina la fila 5

df_sin_outlier = df.drop(index=5)
df_sin_outlier = df_sin_outlier.reset_index(drop=True)
print('\n')
print('------------------------------------------------ DATA FRAME SIN OUTLIERS ------------------------------------------------')
print('-------------------------------------------------------------------------------------------------------------------------')
print(df_sin_outlier)
print('\n')
# Reemplaza los valores de la columna "Razon_Migracion" usando mapeo de valores (ejemplo: "Económica" → "Trabajo", "Conflicto" → "Guerra").

df_sin_outlier['Razon_Migracion'] = df_sin_outlier['Razon_Migracion'].replace({'Económica':'Trabajo','Conflicto':'Guerra'})

print(df_sin_outlier)
print('\n')

# 2. Análisis Exploratorio

## Muestra las 5 primeras filas del dataset

print(df.head(5))
print('\n')

## Obtén información general del dataset con .info() y .describe().

print(df.info())
print('\n')
print(df.describe())
print('\n')

### Calcula estadísticas clave


total_migrantes = df['Cantidad_Migrantes'].sum()
promedio_migrantes = df['Cantidad_Migrantes'].mean()
mediana_migrantes = df['Cantidad_Migrantes'].median()
promedio_PIB_Origen = df['PIB_Origen'].mean()
promedio_PIB_Destino = df['PIB_Destino'].mean()
conteo_de_valores_razon = df['Razon_Migracion'].value_counts()

print(f'la cantidad de migrantes es :{total_migrantes:,}')
print(f'el promedio de los migrantes es :{promedio_migrantes:,}')
print(f'la mediana de los migrantes es :{mediana_migrantes:,}')
print(f'el promedio del PIB Origen es :{promedio_PIB_Origen:,}')
print(f'el promedio del PIB Destino es :{promedio_PIB_Destino:,}')
print(conteo_de_valores_razon)
print('\n')

# 3.Agrupamiento y Sumarización de Datos

### Agrupa los datos por "Razon_Migracion" y calcula la suma total de migrantes para cada categoría.

df_agrupado = df.groupby('Razon_Migracion')['Cantidad_Migrantes'].sum()
conflicto_migrantes = df_agrupado['Conflicto']
economico_migrantes = df_agrupado['Económica']
educativa_migrantes = df_agrupado['Educativa']
print(df_agrupado)
print('\n')
print(f'La cantidad de personas que migro por temas conflictivos son: {conflicto_migrantes}')
print(f'La cantidad de personas que migro por temas economicos son: {economico_migrantes}')
print(f'La cantidad de personas que migro por temas educativos son: {educativa_migrantes}')
print('\n')

## Obtén la media del IDH de los países de origen por cada tipo de migración.

df_agrupado2 = df.groupby('Pais_Origen')['IDH_Origen'].mean()
print(df_agrupado2)
print('\n')
for pais, idh in df_agrupado2.items():
    print(f'El promedio del Indice de Desarrollo Humano de {pais} es: {idh:.2f}')

## Ordena el DataFrame de mayor a menor cantidad de migrantes.

df_ordenado = df.sort_values(by='Cantidad_Migrantes',ascending=False)
print('\n')
print(df_ordenado)


## 4. Filtros y Selección de Datos

## Filtra y muestra solo las migraciones por conflicto.
print('\n')
print('-------------------------------------- solo la Cantidad de Migrantes por conflicto --------------------------------------')
print('-------------------------------------------------------------------------------------------------------------------------')
df_conflicto = df[df['Razon_Migracion'] == 'Conflicto']
print(df_conflicto)
print('\n')
## Selecciona y muestra las filas donde el IDH del país de destino sea mayor a 0.90.

df_IDH_Destino = df[df['IDH_Destino'] > 0.90]
print('-------------------------------------- Paises que tienen un IDH mayor a 0.90 -----------------------------------------')
print('----------------------------------------------------------------------------------------------------------------------')
print(df_IDH_Destino)
print('\n')


## Crea una nueva columna "Diferencia_IDH" que calcule la diferencia de IDH entre país de origen y destino.

df['Diferencia_IDH'] = df['IDH_Origen'] - df['IDH_Destino']
print(df)
print('\n')
### 5. Exportación de Datos

## Guarda el DataFrame final en un nuevo archivo CSV llamado "Migracion_Limpio.csv", sin el índice.

print('------------------------------------------------ DATA FRAME SIN OUTLIERS ------------------------------------------------')
print('-------------------------------------------------------------------------------------------------------------------------')
print(df_sin_outlier)

df_sin_outlier.to_csv('Migracion_Limpio2.csv', index=False)