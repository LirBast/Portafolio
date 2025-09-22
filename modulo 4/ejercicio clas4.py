import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

### Horas de estudio(x) y Calificacaciones (y)

horas_de_estudio=np.array([1,2,4,5,6,8,9,10,12,15]).reshape(-1,1)
calificaciones=np.array([55,60,65,70,78,80,85,92,95,100])

print(horas_de_estudio)
print(calificaciones)

plt.figure(figsize=(8,6))
plt.scatter(horas_de_estudio,calificaciones,color='blue',label='Datos Reales')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Horas de estudio vs Calificaciones')
plt.grid(True)
plt.legend()
plt.show()


modelo=LinearRegression()
modelo.fit(horas_de_estudio,calificaciones)
print('Modelo Ajustado Exitosamente')

beta_0=modelo.intercept_
beta_1=modelo.coef_[0]

print(f'el valor de intercepto Beta 0: {beta_0:.2f}')
print(f'el valor de la pendiente Beta1: {beta_1:.2f}')

#### Aca vamos a hacer predicciones 


y_predi=modelo.predict(horas_de_estudio)
print(f'prediccion realizada {y_predi}')


plt.figure(figsize=(8,6))
plt.scatter(horas_de_estudio,calificaciones,color='blue',label='Datos Reales')
plt.scatter(horas_de_estudio,y_predi,color='red',label='Datos Reales')
plt.xlabel('X')
plt.ylabel('Y Prediction')
plt.title('Regresion Lienal Simple: Datos reales y linea de ajuste')
plt.grid(True)
plt.legend()
plt.show()

mse=mean_squared_error(calificaciones,y_predi)
print(f'Error cuadratico medio {mse:.2f}')



