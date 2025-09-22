
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

df_swap=df.swaplevel()
print(df_swap)
print('\n')
df_stack=df.stack()
print(df_stack)
print('\n')
df_unstack=df.unstack()
print(df_unstack)
print('\n')


df_group1=df.groupby('Materia')['Calificacion'].agg(total='sum',Promedio='mean',Maximo='max',Minimo='min')
print('Tabla Resumen')
print(df_group1)