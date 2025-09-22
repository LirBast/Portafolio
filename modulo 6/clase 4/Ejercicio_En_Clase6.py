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
y_pred_lin = lin_pipe.predict(X_test)

mse_lin  = mean_squared_error(y_test, y_pred_lin)
rmse_lin = math.sqrt(mse_lin)
r2_lin   = r2_score(y_test, y_pred_lin)
mae_lin  = mean_absolute_error(y_test, y_pred_lin)

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
print(f"Metricas polinomio grado 3: {metricas_poly3}")

depths = [1, 3, 5, 10]
tree_models = {}
tree_metrics = {}

for depth in depths:
    modelo_tree = DecisionTreeRegressor(max_depth=depth, random_state=42)
    modelo_tree.fit(X_train, y_train)
    y_pred = modelo_tree.predict(X_test)
    tree_models[depth] = modelo_tree
    tree_metrics[depth] = calcular_metricas(y_test, y_pred)

for d, m in tree_metrics.items():
    print(f"  - Profundidad {d}: {m}")

# Ridge regularizacion L2
ridge_pipe = Pipeline([('scaler', StandardScaler()), ('ridge', Ridge())])
ridge_param_grid ={'ridge__alpha': [0.01, 0.1, 1, 10, 100]}
ridge_search = GridSearchCV(ridge_pipe, ridge_param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
ridge_search.fit(X_train, y_train)

best_ridge = ridge_search.best_estimator_
alpha_ridge = ridge_search.best_params_['ridge__alpha']

y_pred_ridge = best_ridge.predict(X_test)
metricas_ridge = calcular_metricas(y_test, y_pred_ridge)

# Lasso regularizacion L1
lasso_pipe = Pipeline([('scaler', StandardScaler()), ('lasso', Lasso())])
lasso_param_grid ={'lasso__alpha': [0.0001, 0.001, 0.01, 0.1, 1]}
lasso_search = GridSearchCV(lasso_pipe, lasso_param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
lasso_search.fit(X_train, y_train)

best_lasso = lasso_search.best_estimator_
alpha_lasso = lasso_search.best_params_['lasso__alpha']

y_pred_lasso = best_lasso.predict(X_test)
metricas_lasso = calcular_metricas(y_test, y_pred_lasso)

rows = []
rows.append(('Linear', ) + tuple([metrics:=calcular_metricas(y_test, y_pred_lin)[k] for k in ['mse', 'rmse', 'r2', 'mae']]))
rows.append(('Poly2', metricas_poly2['mse'], metricas_poly2['rmse'], metricas_poly2['r2'], metricas_poly2['mae']))
rows.append(('Poly3', metricas_poly3['mse'], metricas_poly3['rmse'], metricas_poly3['r2'], metricas_poly3['mae']))

for depth in depths:
  m = tree_metrics[depth]
  rows.append((f'Tree_{depth}', m['mse'], m['rmse'], m['r2'], m['mae']))

rows.append((f'Ridge (alpha={alpha_ridge})', metricas_ridge['mse'], metricas_ridge['rmse'], metricas_ridge['r2'], metricas_ridge['mae']))
rows.append((f'Lasso (alpha={alpha_lasso})', metricas_lasso['mse'], metricas_lasso['rmse'], metricas_lasso['r2'], metricas_lasso['mae']))

df_metricas = pd.DataFrame(rows, columns=['modelo','MSE', 'RMSE', 'R2', 'MAE']).sort_values(by ='MSE').reset_index(drop = True)
print(df_metricas)
print('\n')
print(df_metricas.round(4))

# Mejor modelo por R²
mejor_r2 = df_metricas.sort_values('R2', ascending=False).iloc[0]
print(f"\nMejor modelo por R²: {mejor_r2['modelo']} con R² = {mejor_r2['R2']:.4f}")

# Mejor modelo por MSE (menor es mejor)
mejor_mse = df_metricas.iloc[0]
print(f"Mejor modelo por MSE: {mejor_mse['modelo']} con MSE = {mejor_mse['MSE']:.4f}")

# Gráficos corregidos
plt.figure(figsize=(6, 5))
plt.scatter(y_test, y_pred_lin, s=20)
mn = min(y_test.min(), y_pred_lin.min())
mx = max(y_test.max(), y_pred_lin.max())
plt.plot([mn, mx], [mn, mx], color='red')
plt.xlabel('Valores reales: y_test')
plt.ylabel('Valores predichos: y_pred_lin')
plt.title('y_test vs y_pred_lin - Regresion lineal')
plt.grid(True)

plt.figure(figsize=(6, 5))
plt.scatter(y_test, y_ped_poly2, s=20)
mn = min(y_test.min(), y_ped_poly2.min())
mx = max(y_test.max(), y_ped_poly2.max())
plt.plot([mn, mx], [mn, mx], color='red')
plt.xlabel('Valores reales: y_test')
plt.ylabel('Valores predichos: y_ped_poly2')
plt.title('y_test vs y_ped_poly2 - Poly2')
plt.grid(True)

plt.figure(figsize=(6, 5))
plt.scatter(y_test, y_ped_poly3, s=20)
mn = min(y_test.min(), y_ped_poly3.min())
mx = max(y_test.max(), y_ped_poly3.max())
plt.plot([mn, mx], [mn, mx], color='red')
plt.xlabel('Valores reales: y_test')
plt.ylabel('Valores predichos: y_ped_poly3')
plt.title('y_test vs y_ped_poly3 - Poly3')
plt.grid(True)

plt.figure(figsize=(6, 5))
plt.scatter(y_test, y_pred_ridge, s=20)
mn = min(y_test.min(), y_pred_ridge.min())
mx = max(y_test.max(), y_pred_ridge.max())
plt.plot([mn, mx], [mn, mx], color='red')
plt.xlabel('Valores reales: y_test')
plt.ylabel('Valores predichos: y_pred_ridge')
plt.title(f'y_test vs y_pred_ridge - Ridge (alpha={alpha_ridge})')
plt.grid(True)

plt.figure(figsize=(6, 5))
plt.scatter(y_test, y_pred_lasso, s=20)
mn = min(y_test.min(), y_pred_lasso.min())
mx = max(y_test.max(), y_pred_lasso.max())
plt.plot([mn, mx], [mn, mx], color='red')
plt.xlabel('Valores reales: y_test')
plt.ylabel('Valores predichos: y_pred_lasso')
plt.title(f'y_test vs y_pred_lasso - Lasso (alpha={alpha_lasso})')
plt.grid(True)

plt.show()

# Mejor árbol de decisión por R² y gráfico
best_tree_depth = max(tree_metrics.keys(), key=lambda d: tree_metrics[d]['r2'])
y_pred_tree_best = tree_models[best_tree_depth].predict(X_test)
print(f"Mejor árbol por R²: profundidad={best_tree_depth} -> {tree_metrics[best_tree_depth]}")

plt.figure(figsize=(6, 5))
plt.scatter(y_test, y_pred_tree_best, s=20)
mn = min(y_test.min(), y_pred_tree_best.min())
mx = max(y_test.max(), y_pred_tree_best.max())
plt.plot([mn, mx], [mn, mx], color='red')
plt.xlabel('Valores reales: y_test')
plt.ylabel('Valores predichos: y_pred_tree_best')
plt.title(f'y_test vs y_pred_tree_best - DecisionTree (depth={best_tree_depth})')
plt.grid(True)