from sklearn.model_selection import RepeatedKFold, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.svm import SVR
import numpy as np

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 3*X**2+2*X+np.random.randn(100,1)*10

cv = RepeatedKFold(n_splits=5, n_repeats=3, random_state=0)
scoring = 'neg_mean_squared_error'  # o 'r2'

models = {}

# 1) Lineal
models['Linear'] = Pipeline([
    ('scaler', StandardScaler(with_mean=True, with_std=True)),
    ('lin', LinearRegression())
])

# 2) Ridge (CV en alpha)
models['Ridge'] = Pipeline([
    ('scaler', StandardScaler()),
    ('ridge', RidgeCV(alphas=np.logspace(-4, 4, 50), cv=5))
])

# 3) LASSO (CV en alpha)
models['LASSO'] = Pipeline([
    ('scaler', StandardScaler()),
    ('lasso', LassoCV(alphas=None, cv=5, random_state=0, max_iter=10000))
])

# 4) Polynomial + Ridge (mejor que poli+OLS)
models['Poly+Ridge'] = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2, include_bias=False)),
    ('ridge', RidgeCV(alphas=np.logspace(-4, 4, 50), cv=5))
])

# 5) SVR RBF (búsqueda chica)
models['SVR_RBF'] = Pipeline([
    ('scaler', StandardScaler()),
    ('svr', SVR(kernel='rbf'))
])

param_grids = {
    'SVR_RBF': {'svr__C': [1, 10, 100], 'svr__epsilon': [0.01, 0.1, 0.5], 'svr__gamma': ['scale', 0.01, 0.1, 1.0]},
    # Puedes agregar grids para Poly degree si querés: {'poly__degree':[2,3]}
}

results = {}
for name, pipe in models.items():
    if name in param_grids:
        gs = GridSearchCV(pipe, param_grids[name], cv=cv, scoring=scoring, n_jobs=-1)
        gs.fit(X, y)
        scores = cross_val_score(gs.best_estimator_, X, y, cv=cv, scoring=scoring, n_jobs=-1)
        results[name] = (np.mean(scores), np.std(scores), gs.best_params_)
    else:
        scores = cross_val_score(pipe, X, y, cv=cv, scoring=scoring, n_jobs=-1)
        results[name] = (np.mean(scores), np.std(scores), None)

for name, (mean_score, std_score, best_params) in results.items():
    print(f"{name}: {scoring} CV = {mean_score:.4f} ± {std_score:.4f} | best_params={best_params}")