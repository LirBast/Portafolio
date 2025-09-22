import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
import math

np.random.seed(42)

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 3 * X**2 + 2*X + np.random.randn(100, 1) * 10
y = y.ravel()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Regresion lineal con Pipeline
lin_pipe = Pipeline([('scaler', StandardScaler()), ('lr',LinearRegression())])

lin_pipe.fit(X_train, y_train)

y_ped_lin = lin_pipe.predict(X_test)

mse_lin  = mean_squared_error(y_test, y_ped_lin)
rmse_lin = math.sqrt(mse_lin)
r2_lin   = r2_score(y_test, y_ped_lin)
mae_lin  = mean_absolute_error(y_test, y_ped_lin)

print(f" mse_lin : {mse_lin}")
print(f"rmse_lin : {rmse_lin}")
print(f"  r2_lin : {r2_lin}")
print(f" mae_lin : {mae_lin}")

# Regresion polinomica grado 2
poly2_pipe = Pipeline([('poly', PolynomialFeatures(degree=2, include_bias=False)), ('scaler', StandardScaler()), ('lr',LinearRegression())])
poly2_pipe.fit(X_train, y_train)
y_ped_poly2 = poly2_pipe.predict(X_test)


# Regresion polinomica grado 3
poly3_pipe = Pipeline([('poly', PolynomialFeatures(degree=3, include_bias=False)), ('scaler', StandardScaler()), ('lr',LinearRegression())])
poly3_pipe.fit(X_train, y_train)
y_ped_poly3 = poly3_pipe.predict(X_test)

def calcular_metricas(y_true, y_pred):

  mse = mean_squared_error(y_true, y_pred)

  return {
      "mse": mse,
      "rmse": math.sqrt(mse),
      "r2": r2_score(y_true, y_pred),
      "mae": mean_absolute_error(y_true, y_pred)
    }

metricas_poly2 = calcular_metricas(y_test, y_ped_poly2)
metricas_poly3 = calcular_metricas(y_test, y_ped_poly3)

print(f"Metricas polinomio grado 2: {metricas_poly2}")
print('\n')
print(f"Metricas polinomio grado 3: {metricas_poly3}")
print('\n')
### árbol de decisión (regresión)

depths = [1, 3, 5, 10]

tree_models = {}
tree_metrics = {}

for depth in depths:
    modelo_tree = DecisionTreeRegressor(max_depth=depth, random_state=42)
    modelo_tree.fit(X_train, y_train)
    y_pred = modelo_tree.predict(X_test)
    tree_models[depth] = modelo_tree
    tree_metrics[depth] = calcular_metricas(y_test, y_pred)

print(tree_metrics)

# Ridge regularizacion L2

ridge_pipe = Pipeline([('scaler', StandardScaler()), ('ridge', Ridge())])
ridge_param_grid ={'ridge__alpha': [0.01, 0.1, 1, 10, 100]}
ridge_search = GridSearchCV(ridge_pipe, ridge_param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
ridge_search.fit(X_train, y_train)

best_ridge = ridge_search.best_estimator_
alpha_ridge = ridge_search.best_params_['ridge__alpha']

y_pred_ridge = best_ridge.predict(X_test)

metricas_ridge = calcular_metricas(y_test, y_pred_ridge)

print(f"Mejor alpha Ridge: {alpha_ridge}")
print(f"Metricas Ridge: {metricas_ridge}")
print('\n')

# Lasso regularizacion L1

lasso_pipe = Pipeline([('scaler', StandardScaler()), ('lasso', Lasso())])
lasso_param_grid ={'lasso__alpha': [0.01, 0.1, 1, 10, 100]}
lasso_search = GridSearchCV(lasso_pipe, lasso_param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
lasso_search.fit(X_train, y_train)

best_lasso = lasso_search.best_estimator_
alpha_lasso = lasso_search.best_params_['lasso__alpha']

y_pred_lasso = best_lasso.predict(X_test)

metricas_lasso = calcular_metricas(y_test, y_pred_lasso)

print(f"Mejor alpha Lasso: {alpha_lasso}")
print(f"Metricas Lasso: {metricas_lasso}")
print('\n')

# Resumen comparativo de todos los modelos
print("=== RESUMEN COMPARATIVO ===")
print(f"Linear Regression - R²: {r2_lin:.4f}, RMSE: {rmse_lin:.4f}")
print(f"Polynomial Degree 2 - R²: {metricas_poly2['r2']:.4f}, RMSE: {metricas_poly2['rmse']:.4f}")
print(f"Polynomial Degree 3 - R²: {metricas_poly3['r2']:.4f}, RMSE: {metricas_poly3['rmse']:.4f}")
print(f"Ridge (α={alpha_ridge}) - R²: {metricas_ridge['r2']:.4f}, RMSE: {metricas_ridge['rmse']:.4f}")
print(f"Lasso (α={alpha_lasso}) - R²: {metricas_lasso['r2']:.4f}, RMSE: {metricas_lasso['rmse']:.4f}")

# Mejor modelo de árbol de decisión
best_tree_depth = max(tree_metrics.keys(), key=lambda k: tree_metrics[k]['r2'])
print(f"Best Decision Tree (depth={best_tree_depth}) - R²: {tree_metrics[best_tree_depth]['r2']:.4f}, RMSE: {tree_metrics[best_tree_depth]['rmse']:.4f}")