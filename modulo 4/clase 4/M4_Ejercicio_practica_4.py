import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error


# 1 Creación de Datos Simulados (temperatura ambiente y consumo de energía)

## x sera la temperatura ambiente

X = np.array([30,29,28,23,19,16,15,17,19,23,26,29]).reshape(-1, 1)

## y sera el consumo en kWh promedio de una familia durante un año

Y = np.array([600, 600, 650, 700, 800, 900, 900, 800, 700, 650, 600, 600])


# 2 Implementación del Modelo de Regresión Lineal

modelo = LinearRegression()
modelo.fit(X, Y)

### coeficientes

beta_0 = modelo.intercept_
beta_1 = modelo.coef_[0]

print(f'El intecepto es: {beta_0:.2f}')
print(f'el valor de la pendiente es: {beta_1:.2f}')

# 3 Predicción de Valores con el Modelo (Primero 5 numeros)

Y_pred = modelo.predict(X)

Y_pred_columna = Y_pred.reshape(-1, 1)

print(Y_pred_columna[:5])
print('\n')
# 4 Evaluación del Modelo


mse = mean_squared_error(Y, Y_pred)
print(f'Error cuadratico medio (MSE): {mse:.2f}')
print('\n')

mae = mean_absolute_error(Y, Y_pred)
print(f'Error absoluto medio (MAE): {mae:.2f}')


### El error cuadrático medio (MSE) me dio un valor de 1738,87. Esto indica que, en promedio, el cuadrado de la diferencia entre los valores reales y los predichos es alto.
### El MSE es sensible a los errores grandes (outliers), ya que al elevar las diferencias al cuadrado, penaliza mucho más los errores grandes que los pequeños.
### Por eso, un MSE elevado puede indicar que hay algunas predicciones que se alejan bastante de los valores reales.

### El MAE es más intuitivo porque está en las mismas unidades que el consumo (kWh).
### En este caso, el MAE es de 34,98 kWh, lo que implica que, en promedio, los valores predichos por el modelo se desvían 34,98 kWh de los datos reales.