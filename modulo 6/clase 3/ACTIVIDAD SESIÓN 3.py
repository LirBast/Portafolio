import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from scipy.spatial.distance import cityblock, euclidean, minkowski


df = pd.read_csv(r'C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 6\clase 3\customer_data.csv')

# 1. Carga de datos (1 punto) 
# • Descarga el archivo customer_data.csv proporcionado en el material complementario. 
# • Carga el conjunto de datos utilizando Pandas. 
# • Muestra las primeras 5 filas del dataset. 


# Exploración inicial de los datos
print(df.head())       # Mostrar las primeras filas para ver la estructura
print('\n' + '='*80 + '\n')

# 2. Preprocesamiento de datos (3 puntos) 
# • Limpieza de datos: 
# o Verifica si hay valores nulos en el dataset y elimina las filas que los contengan. 



print(df.info())       # Información general: tipos de datos y valores nulos
print('\n' + '='*80 + '\n')
print(df.describe())   # Estadísticas descriptivas básicas
print('\n' + '='*80 + '\n')

# o Elimina columnas que no sean relevantes para el análisis (por ejemplo, columnas de 
# identificación).

df_limpio = df.drop(columns=['CustomerID'])
print('Data Frame limpio')
print(df_limpio)
print('\n' + '='*80 + '\n')
#  Codificación de variables categóricas: 
#  Aplica Label Encoding a la columna Gender (Género). 

# Label Encoding para Gender
labe_en = LabelEncoder()
df_limpio['Gender'] = labe_en.fit_transform(df_limpio['Gender'])

# o Aplica One-Hot Encoding a la columna City (Ciudad). 

df_limpio = pd.get_dummies(df_limpio, columns=['City'], drop_first=True)

# Escalamiento de datos: 
# o Aplica Min-Max Scaling a la columna Age (Edad). 

mm_scaler = MinMaxScaler()
df_limpio['Age'] = mm_scaler.fit_transform(df_limpio[['Age']])

# o Aplica Standard Scaling a la columna Income (Ingresos).
std_scaler = StandardScaler()
df_limpio['Income'] = std_scaler.fit_transform(df_limpio[['Income']])

print("Dataset después de los cambios:")
print(df_limpio)
print("\n" + "="*30 + "\n")

# 3. Implementación de técnicas de distancia (3 puntos) 
# • Calcula la Distancia Manhattan, Distancia Euclidiana y Distancia Minkowski (con p=3p=3) 
# entre los siguientes dos puntos: 
# o Punto A: [25, 50000] (Edad, Ingresos) 
# o Punto B: [30, 60000] (Edad, Ingresos)

# Definir los puntos
punto_A = [25, 50000]  # [Edad, Ingresos]
punto_B = [30, 60000]  # [Edad, Ingresos]


# 1. Distancia Manhattan (L1)
dist_manhattan = cityblock(punto_A, punto_B)
print(f"Distancia Manhattan (L1): {dist_manhattan}")

# 2. Distancia Euclidiana (L2)
dist_euclidiana = euclidean(punto_A, punto_B)
print(f"Distancia Euclidiana (L2): {dist_euclidiana:.2f}")

# 3. Distancia Minkowski con p=3
dist_minkowski = minkowski(punto_A, punto_B, p=3)
print(f"Distancia Minkowski (p=3): {dist_minkowski:.2f}")
