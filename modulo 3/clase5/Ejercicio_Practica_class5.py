
import pandas as pd

data={'Estudiante':['Juan','Juan','Maria','Maria'],
      'Materia':['Matematicas','Historia','Matematicas','Historia'],
      'Calificacion':[6.5,5.8,4.2,6.0]}

df=pd.DataFrame(data)

# 1.-Crear un DataFrame con Indexación Jerárquica
df.set_index(['Estudiante','Materia'], inplace=True)
print(df)
print('\n')
### Generalmente las columnas de datos numericos no quedan como indice

# 1.1 Otros metodos de multiindex

# df_swap=df.swaplevel()
# print(df_swap)

# df_stack=df.stack()
# print(df_stack)

# df_unstack=df.unstack()
# print(df_unstack)

## 2.- Acceder a datos con Indexación Jerárquica
## • Consulta la clasificación de María en Historia.

print(f"la calificaicon de maria en Historia es : {df.loc[('Maria','Historia'),:].values[0]}")

## 3. Agrupar y Agregar Datos con groupby (2 puntos)
#   Agrupa el DataFrame por "Materia" y calcula:
#   El promedio de calificaciones por materia.
#   La calificación más alta por materia.

df_group=df.groupby('Materia')['Calificacion'].mean()
print('Promedio por materiaa')
print(df_group)

### la calificacion mas alta por materia

print('\n')
df_group1=df.groupby('Materia')['Calificacion'].agg(total='sum',Promedio='mean',Maximo='max',Minimo='min')
print('Tabla Resumen')
print(df_group1)
print('\n')

# 4. Pivoteo de DataFrame

df_pivot=df.pivot_table(index='Estudiante',columns='Materia',values='Calificacion')
df_pivot.columns.name = None  ### Esto quita el nombre del indice de columnas
print(df_pivot)
print('\n')
# 5.- Despivoteo de DataFrame con melt (1 punto)

df_pivot=df_pivot.reset_index()
df_melted=df_pivot.melt(id_vars=['Estudiante'], var_name='Materia',value_name='Calificacion')

print(df_melted)

## 6.- Concatenación y Merge de DataFrames

data1={'ID_Estudiante':[1,2,3],
       'Etudiante':['Ana','Pedro','Juan'],
       'Carrera':['Ingenieria','Medicina','Derecho']}
data2={'ID_Estudiante': [1, 2, 4],
                    'Materia': ['Matemáticas', 'Biología', 'Historia'],\
                    'Calificación': [90, 85, 88]}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

print(df1)
print('\n')
print(df2)

### concatenar los 2 Data Frame

df_concat = pd.concat([df1,df2],axis=0,ignore_index=True)  ## para concatenar filas el axis=0 y para concatenar columnas axis=0

print(df_concat)

### Merge ambos dataFrame

df_merged=pd.merge(df1,df2,on=['ID_Estudiante'],how='outer')  ### el how
print(df_merged)