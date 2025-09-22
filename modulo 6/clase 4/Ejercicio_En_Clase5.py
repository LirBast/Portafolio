from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

np.random.seed(42)

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 3 * X**2 + 2 * X - X**3 + np.random.randn(100, 1) * 10
y = y.ravel()

poly = PolynomialFeatures(degree=5, include_bias=False)
X_poly = poly.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

ridge = Ridge()
param_grid ={'alpha': [0.001, 0.01, 0.1, 1, 10, 100]}
ridge_search = GridSearchCV(ridge, param_grid, cv=5, scoring='neg_mean_squared_error')
ridge_search.fit(X_train, y_train)

print('Mejor Alpha {ridge}:', ridge_search.best_params_['alpha'])
best_ridge = ridge_search.best_estimator_

lasso = Lasso(max_iter=1000)
param_grid_lasso = {'alpha': [0.0001, 0.001, 0.01, 0.1, 1]}
lasso_search = GridSearchCV(lasso, param_grid_lasso, cv=5, scoring='neg_mean_squared_error')
lasso_search.fit(X_train, y_train)

print('Mejor Alpha {lasso}:', lasso_search.best_params_['alpha'])
best_lasso = lasso_search.best_estimator_

y_pred_ridge = best_ridge.predict(X_test)
y_pred_lasso = best_lasso.predict(X_test)

for name, y_pred in [('Ridge', y_pred_ridge), ('Lasso', y_pred_lasso)]:
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'{name} MSE: {mse:.2f}')
    print(f'{name} R2: {r2:.2f}')