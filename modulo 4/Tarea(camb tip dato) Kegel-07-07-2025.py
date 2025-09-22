import pandas as pd

df = pd.read_csv(r"C:\Users\liroy\OneDrive\Escritorio\bootcamp\clases\modulo 4\clase 3\ai_job_dataset.csv")
print(df.head(5))


# Me entrega todos los tipos de todas las columnas que integran el dataset
print(df.dtypes)

## Si quiero solo una columna tengo que darle espeficicamente cual deseo llamar
print('\n')

print(df['salary_usd'].dtypes)  ## Esto me entrega el tipo que tiene salario, es esta ocasion me dice que es un int (entero)
print('\n')
print(df['salary_usd']) # aca estoy imprimiendo la nueva columna que es salario pero tipo flotante
print('\n')

## Ahora tengo que saber cual es la posicion de la columna salario, se usa la get.loc para saber en cual posicion esta, y se crea un variable

posicion_salario_usd=df.columns.get_loc('salary_usd')

print(posicion_salario_usd)

print('\n')

df.insert(posicion_salario_usd+1,'salary_usd_float',df['salary_usd'].astype(float))

print(df.head())
print('\n')

print(df['employee_residence'].value_counts())

