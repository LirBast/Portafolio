import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.array([50, 70, 90, 110, 130]).reshape(-1, 1)
y = np.array([150, 200, 250, 300, 350]) + np.random.normal(0, 20, 5)
plt.scatter(X, y, color="red", label="Datos Reales")
plt.xlabel("Tamaño (M2)")
plt.ylabel("Precio (USD$)")
plt.legend()
plt.show()

modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)
intercepto = modelo.intercept_
pendiente = modelo.coef_[0]
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Intercepto: {intercepto:.2f}")
print(f"Pendiente: {pendiente:.2f}")
print(f"MSE: {mse:.2f}")
print(f"R2: {r2:.3f}")