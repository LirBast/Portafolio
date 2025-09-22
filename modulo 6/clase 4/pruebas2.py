import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import Pipeline

# Datos
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 3*X**2 + 2*X + np.random.randn(100, 1)*10

plt.scatter(X, y, color="red", s=10, label="Datos")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Lineal
lin = LinearRegression()
lin.fit(X_train, y_train)
y_pred_lin = lin.predict(X_test)
mse_lin = mean_squared_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)

# Polinómico
poli = PolynomialFeatures(degree=2)
X_train_poli = poli.fit_transform(X_train)
X_test_poli = poli.fit_transform(X_test)
poli_reg = LinearRegression()
poli_reg.fit(X_train_poli, y_train)
y_pred_poli = poli_reg.predict(X_test_poli)
mse_poli = mean_squared_error(y_test, y_pred_poli)
r2_poli = r2_score(y_test, y_pred_poli)

# Árbol
tree = DecisionTreeRegressor(random_state=42)
tree.fit(X_train, y_train)
y_pred_tree = tree.predict(X_test)
mse_tree = mean_squared_error(y_test, y_pred_tree)
r2_tree = r2_score(y_test, y_pred_tree)

print("Lineal:    MSE=%.2f, R2=%.3f" % (mse_lin, r2_lin))
print("Polinomio: MSE=%.2f, R2=%.3f" % (mse_poli, r2_poli))
print("Árbol:     MSE=%.2f, R2=%.3f" % (mse_tree, r2_tree))

# Ridge y Lasso
ridge = Ridge(alpha=1.0)
score_ridge = cross_val_score(ridge, X_train_poli, y_train.ravel(), cv=5, scoring="neg_mean_squared_error")

lasso = Lasso(alpha=0.1, max_iter=10000)
score_lasso = cross_val_score(lasso, X_train_poli, y_train.ravel(), cv=5, scoring="neg_mean_squared_error")

print("Ridge MSE Promedio (Neg):", np.mean(score_ridge))
print("Lasso MSE Promedio (Neg):", np.mean(score_lasso))

# GridSearchCV
pipeline = Pipeline([
    ('Scaler', StandardScaler()),
    ('Ridge', Ridge())
])
param_grid = {'Ridge__alpha': [0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error')
grid.fit(X_train_poli, y_train.ravel())

print('Mejor alpha: ', grid.best_params_)
print('Mejor score (negado MSE): ', grid.best_score_)
