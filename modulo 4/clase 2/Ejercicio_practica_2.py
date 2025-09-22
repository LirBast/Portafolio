import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {'ID':[1,2,3,4,5,6,7,8,9,10],
        'Nombre':['Ana', 'Juan', 'Luis', 'Marta','Pedro', 'Sofia', 'Carlos', 'Elena', 'Miguel', 'Paula'],
        'Edad':[25, 30, 28, 22, 35, 27, 29, 24, 31, 26],
        'Ingresos':[2500, 3200, 2800, 2200, 4100, 2900, 3100, 2700, 3300, 2600],
        'Genero':['Femenino', 'Masculino', 'Masculino', 'Femenino', 'Masculino','Femenino', 'Masculino','Femenino', 'Masculino','Femenino'],
        'Ciudad':['Lima', 'Bogota', 'Lima', 'Quito', 'Santiago', 'Lima', 'Buenos Aires', 'Quito', 'Santiago', 'Buenos Aires']}


df = pd.DataFrame(data)

print(df.to_string(index=False))
print('\n')

print(df.dtypes)

### 1. Definir Variables

## Con la funcion df.types tenemos una vision general de cada variable
### Id es una variable Cuantitativa discreta
## Nombre es una variable categorica nominales
### Edad es una variable cuantitativa discreta
## Ingresos es una variable cuantitativa continua
### Genero es una variable categorica nominales
## Ciudad es una variable catergorica nominales

# 2. Construcción de una Tabla de Frecuencia 

for col in ['Nombre', 'Genero', 'Ciudad']:
    print(f"Frecuencia de {col}:")
    print(df[col].value_counts())
    print()

for col in ['Edad', 'Ingresos']:
    print(f"Frecuencia de {col}:")
    print(df[col].value_counts())
    print()

# 3. Cálculo de Medidas de Tendencia Central 



promedio_ingresos = df['Ingresos'].mean()
print(f'El promedio de la columna edad es: {promedio_ingresos}')

mediana_ingresos = df['Ingresos'].median()
print(f'La mediana de la columna edad es: {mediana_ingresos}')

moda_ingresos = df['Ingresos'].mode()
print(f'La moda de la columna edad es: {moda_ingresos.values}')
print('\n')
## 4  Cálculo de Medidas de Dispersión

rango = df['Ingresos'].max() - df['Ingresos'].min()

varianza = df['Ingresos'].var()

desviacion_standar = df['Ingresos'].std()

print(f'El rango de la columna Ingresos es: {rango}')
print(f'La varianza de la columna Ingresos es: {varianza:.2f}')
print(f'La Desviacion estandar de la columna Ingresos es: {desviacion_standar:.2f}')
print('\n')

## 5. Visualización de Datos


### Histograma

plt.hist(df['Edad'], bins=5, edgecolor='black', color='#F54927')
plt.title('Histograma de Edad')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

### BoxPlot

plt.boxplot(x = df['Ingresos'])
plt.title('Boxplot de Ingresos')
plt.xlabel('Ingresos')
plt.grid(True)
plt.show()