import pandas as pd

# Ejemplo con tu DataFrame
df=pd.read_csv('C:\\Users\\liroy\\OneDrive\\Escritorio\\bootcamp\\proyecto\\modulo 3\\clase4\\ventas.csv')

print(df)
# Detectar filas duplicadas
dups = df.duplicated(keep=False)  # marca True todas las apariciones duplicadas

# Creamos un DataFrame con filas duplicadas
df_dups = df[dups].copy()

# Crear un identificador para cada fila (puedes usar el índice)
df_dups['index'] = df_dups.index

# Encontrar la primera aparición de cada grupo duplicado usando todas las columnas
first_occurrence = df_dups.drop_duplicates().reset_index()

# Ahora para cada fila duplicada, buscamos con qué fila se duplica
def fila_duplicada(row):
    # Buscar la primera fila igual que no sea la misma
    iguales = df_dups[(df_dups.drop('index', axis=1) == row.drop('index')).all(axis=1)]
    # Excluir la fila actual
    iguales = iguales[iguales['index'] != row['index']]
    if not iguales.empty:
        return iguales['index'].iloc[0]  # devuelve índice de la fila original con la que duplica
    else:
        return None

df_dups['fila_duplicada_de'] = df_dups.apply(fila_duplicada, axis=1)

print(df_dups[['index', 'fila_duplicada_de']])
