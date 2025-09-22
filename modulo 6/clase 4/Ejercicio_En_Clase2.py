import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor


X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 3*X**2+2*X+np.random.randn(100,1)*10
plt.scatter(X, y, color="red", s=10, label="Data points")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.2, random_state=42)
# Modelo Lineal
lin = LinearRegression()
lin.fit(X_train, y_train)
y_pred_lin = lin.predict(X_test)
mse_lin = mean_squared_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)

# Modelo Polinomio (Grado 2)
poli = PolynomialFeatures(degree=2)
X_train_poli= poli.fit_transform(X_train)
X_test_poli = poli.transform(X_test)
poli_reg = LinearRegression()
poli_reg.fit(X_train_poli, y_train)
y_pred_poli = poli_reg.predict(X_test_poli)
mse_poli = mean_squared_error(y_test, y_pred_poli)
r2_poli = r2_score(y_test, y_pred_poli)


# Modelo Arbol
tree = DecisionTreeRegressor(random_state=42)
tree.fit(X_train, y_train)
y_pred_tree = tree.predict(X_test)
mse_poli_tree = mean_squared_error(y_test, y_pred_tree)
r2_poli_tree = r2_score(y_test, y_pred_tree)

print("Lineal: MSE=%.2f, R2=%.3f" % (mse_lin, r2_lin))
print("Polinomial: MSE=%.2f, R2=%.3f" % (mse_poli, r2_poli))
print("Arbol: MSE=%.2f, R2=%.3f" % (mse_poli_tree, r2_poli_tree))