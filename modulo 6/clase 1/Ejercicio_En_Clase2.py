import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


X = np.array([60,80,100,120]).reshape(-1 , 1) ## convierte la lista en una columna
y = np.array([180000, 220000 , 260000, 300000])


modelo = LinearRegression()
modelo.fit(X,y)

print(f'Intercepto: {modelo.intercept_:.0f}')
print(f'Pendiente: {modelo.coef_[0]:.0f}')

print(f'Prediccion para 90 m2: ${modelo.predict([[90]])[0]:.0f}')  


tam = np.linspace(50 , 130 , 100)

precio_predicho = 60000 + 2000*tam

plt.scatter(X , y , color='blue', label = "Datos Reales")
plt.plot(tam, precio_predicho , color = 'red' , linestyle = '--' , label = 'Prediccion'  )
plt.scatter(120 , 300000, color = 'green', label = 'Prediccion para 120 m2')
plt.xlabel('Tamaño m2')
plt.ylabel('Precio')
plt.legend()
plt.grid(True)
plt.show()