import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 2. Creación del conjunto de datos (2 puntos) 

data = {'Edad':[10,23,33,51,32,12,20,34],
        'Ingreso':[1000000,500000,800000,760000,2000000,556000,980000,550000],
        'Años_Educacion':[6,0,4,5,9,10,1,4],
        'Horas_Sueñó':[5,9,4,5,6,10,7,8]}

df = pd.DataFrame(data)

print(df)

# 3. Cálculo de la matriz de correlación 

correlacion = df.corr()
print(correlacion)

# 4. Generación del heatmap

plt.figure(figsize=(10, 8))
sns.heatmap(correlacion, annot=True, cmap = 'coolwarm',linecolor='black', linewidths=0.5)
plt.title('Matriz de correlacion')
plt.show()


# Edad y Horas_Sueñó: -0.417 (correlación negativa moderada)
# Ingreso y Años_Educacion: 0.414 (correlación positiva moderada)
# Ingreso y Horas_Sueñó: -0.404 (correlación negativa moderada)

## como la muestra es pequeña no se puede hacer un analisis tan extenso, solo analizar que como se relacion ciertas variables
## las mas cercanas a 1 positivo muestran relacion de correlacion positiva, lo que indica que si una aumenta la otra tambien lo hace, 
## y en el caso de ser negativa nos indica que si una aumenta la otra disminuye, como en el caso de la edad y las horas de sueño que es -0.417