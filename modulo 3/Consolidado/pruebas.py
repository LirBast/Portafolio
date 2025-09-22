import pandas as pd
import numpy as np

df=pd.read_csv('C:\\Users\\liroy\\OneDrive\\Escritorio\\bootcamp\\clases\\modulo 3\\consolidado final\\material complementario evaluacion final\\migracion.csv')

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

#C.- Identificar valores outliers


tabla_resumen=df.describe().round(2)
print(tabla_resumen)

Q1_Año=tabla_resumen.loc['25%', 'Año']
Q3_Año=tabla_resumen.loc['75%', 'Año']

print(f'El Q1 de Año es: {Q1_Año}')
print(f'El Q3 de Año es: {Q3_Año}')

Q1_Cantidad_Migrantes=tabla_resumen.loc['25%', 'Cantidad_Migrantes']
Q3_Cantidad_Migrantes=tabla_resumen.loc['75%', 'Cantidad_Migrantes']

print(f'El Q1 de Cantidad_Migrantes es : {Q1_Cantidad_Migrantes}')
print(f'El Q3 de Cantidad_Migrantes es : {Q3_Cantidad_Migrantes}')

Q1_PIB_Origen=tabla_resumen.loc['25%', 'PIB_Origen']
Q3_PIB_Origen=tabla_resumen.loc['75%', 'PIB_Origen']

print(f'El Q1 de PIB_Origen es : {Q1_PIB_Origen}')
print(f'El Q3 de PIB_Origen es : {Q3_PIB_Origen}')

Q1_PIB_Destino=tabla_resumen.loc['25%', 'PIB_Destino']
Q3_PIB_Destino=tabla_resumen.loc['75%', 'PIB_Destino']

print(f'El Q1 de PIB_Destino es : {Q1_PIB_Destino}')
print(f'El Q3 de PIB_Destino es : {Q3_PIB_Destino}')

Q1_IDH_Origen=tabla_resumen.loc['25%', 'IDH_Origen']
Q3_IDH_Origen=tabla_resumen.loc['75%', 'IDH_Origen']

print(f'El Q1 de PIB_Destino es : {Q1_IDH_Origen}')
print(f'El Q3 de PIB_Destino es : {Q3_IDH_Origen}')

Q1_IDH_Destino=tabla_resumen.loc['25%', 'IDH_Destino']
Q3_IDH_Destino=tabla_resumen.loc['75%', 'IDH_Destino']

print(f'El Q1 de IDH_Destino es : {Q1_IDH_Destino}')
print(f'El Q3 de IDH_Destino es : {Q3_IDH_Destino}')

print('\n')
iqr = tabla_resumen.loc['75%'] - tabla_resumen.loc['25%']
print(iqr.round(2))