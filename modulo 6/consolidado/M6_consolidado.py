import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures, label_binarize
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc, mean_squared_error, mean_absolute_error, r2_score
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.linear_model import Ridge, Lasso


# 1. Carga y exploración de datos
df = pd.read_csv(r'C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 6\consolidado\cambio_climatico_agricultura.csv')

# Exploración inicial
print(df.head())       
print(df.shape)
print('\n' + '='*80 + '\n')
print(df.info())
print('\n' + '='*80 + '\n')
print(df.describe())
print('\n' + '='*80 + '\n')
print('Cantidad de datos nulos')
print(df.isnull().sum())
print('\n' + '='*80 + '\n')


ohe = OneHotEncoder()
pais_encoded = ohe.fit_transform(df[['País']]).toarray()
pais_df = pd.DataFrame(pais_encoded, columns=ohe.get_feature_names_out(['País']))
df = pd.concat([df, pais_df], axis=1)

X = df.drop(['País', 'Producción_alimentos'], axis=1)
y = df['Producción_alimentos']

print(df)
print(df.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Regresión Lineal
model = LinearRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

print('Resultados Regresión Lineal:')
print(f'MAE: {mean_absolute_error(y_test, y_pred):.2f}')
print(f'MSE: {mean_squared_error(y_test, y_pred):.2f}')
print(f'R2: {r2_score(y_test, y_pred):.4f}')

# Regresión Polinómica
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
y_pred_poly = poly_model.predict(X_test_poly)

print('Resultados Regresión Polinómica:')
print(f'MAE: {mean_absolute_error(y_test, y_pred_poly):.2f}')
print(f'MSE: {mean_squared_error(y_test, y_pred_poly):.2f}')
print(f'R2: {r2_score(y_test, y_pred_poly):.4f}')

# Árbol de Decisión
tree_model = DecisionTreeRegressor(random_state=42, max_depth=5)
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)

print('Resultados Árbol de Decisión:')
print(f'MAE: {mean_absolute_error(y_test, y_pred_tree):.2f}')
print(f'MSE: {mean_squared_error(y_test, y_pred_tree):.2f}')
print(f'R2: {r2_score(y_test, y_pred_tree):.4f}')

# Random Forest
rf_model = RandomForestRegressor(n_estimators=200, max_depth=6, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

print('Resultados Random Forest:')
print(f'MAE: {mean_absolute_error(y_test, y_pred_rf):.2f}')
print(f'MSE: {mean_squared_error(y_test, y_pred_rf):.2f}')
print(f'R2: {r2_score(y_test, y_pred_rf):.4f}')

# Crear variable categórica Impacto
df_v2 = df.copy()

promedio = df_v2['Producción_alimentos'].mean()
desvia = df_v2['Producción_alimentos'].std()

impacto = []

for valor in df_v2['Producción_alimentos']:
    if valor < promedio - desvia:
        impacto.append('Bajo')
    elif valor > promedio + desvia:
        impacto.append('Alto')
    else:
        impacto.append('Medio')

df_v2['Impacto'] = impacto

# Variables clasificación
X_clf = df_v2.drop(['País', 'Producción_alimentos', 'Impacto'], axis=1)
y_clf = df_v2['Impacto']

X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42, stratify=y_clf
)

scaler_clf = StandardScaler()
X_train_clf_scaled = scaler_clf.fit_transform(X_train_clf)
X_test_clf_scaled = scaler_clf.transform(X_test_clf)

# Clasificadores
# 1. KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_clf_scaled, y_train_clf)
y_pred_knn = knn.predict(X_test_clf_scaled)

# 2. Árbol
tree_clf = DecisionTreeClassifier(random_state=42)
tree_clf.fit(X_train_clf, y_train_clf)
y_pred_tree_clf = tree_clf.predict(X_test_clf)

# 3. SVM
svm_clf = SVC(random_state=42, probability=True)
svm_clf.fit(X_train_clf_scaled, y_train_clf)
y_pred_svm = svm_clf.predict(X_test_clf_scaled)

# Evaluación
print('\nResultados KNN:')
print(f'Accuracy: {accuracy_score(y_test_clf, y_pred_knn):.4f}')
print(f'Precisión: {precision_score(y_test_clf, y_pred_knn, average="weighted"):.4f}')
print(f'Sensibilidad (Recall): {recall_score(y_test_clf, y_pred_knn, average="weighted"):.4f}')
print(f'F1-Score: {f1_score(y_test_clf, y_pred_knn, average="weighted"):.4f}')

print('\nResultados Árbol de Decisión:')
print(f'Accuracy: {accuracy_score(y_test_clf, y_pred_tree_clf):.4f}')
print(f'Precisión: {precision_score(y_test_clf, y_pred_tree_clf, average="weighted"):.4f}')
print(f'Sensibilidad (Recall): {recall_score(y_test_clf, y_pred_tree_clf, average="weighted"):.4f}')
print(f'F1-Score: {f1_score(y_test_clf, y_pred_tree_clf, average="weighted"):.4f}')

print('\nResultados SVM:')
print(f'Accuracy: {accuracy_score(y_test_clf, y_pred_svm):.4f}')
print(f'Precisión: {precision_score(y_test_clf, y_pred_svm, average="weighted"):.4f}')
print(f'Sensibilidad (Recall): {recall_score(y_test_clf, y_pred_svm, average="weighted"):.4f}')
print(f'F1-Score: {f1_score(y_test_clf, y_pred_svm, average="weighted"):.4f}')

# Curvas ROC One-vs-Rest
y_test_bin = label_binarize(y_test_clf, classes=['Bajo', 'Medio', 'Alto'])
y_prob_svm = svm_clf.predict_proba(X_test_clf_scaled)

for i, clase in enumerate(['Bajo', 'Medio', 'Alto']):
    fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_prob_svm[:, i])
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, label=f'{clase} (AUC = {roc_auc:.2f})', color='blue')
    plt.plot([0,1],[0,1],'k--')
    plt.xlabel('Tasa de Falsos Positivos')
    plt.ylabel('Tasa de Verdaderos Positivos')
    plt.title(f'Curva ROC - Clase {clase}')
    plt.legend(loc='lower right')
    plt.show()


# 4. Optimización de modelos (2 puntos) 
# • Ajusta hiperparámetros utilizando validación cruzada y búsqueda en grilla. 
# • Aplica técnicas de regularización y analiza su impacto en los modelos. 

param_grid_rf = {'max_depth': [4, 6, 8, None], 'min_samples_split': [2, 5, 10], 'n_estimators': [100, 200, 300]}

grid_rf = GridSearchCV(RandomForestRegressor(random_state=42), param_grid_rf, cv=5, scoring='r2', n_jobs =-1)
grid_rf.fit(X_train, y_train)

print("Mejores parámetros RF:", grid_rf.best_params_)
print("Mejor R² en CV:", grid_rf.best_score_)

param_grid_svm = {'C': [0.1, 1, 10],'gamma': ['scale', 0.01, 0.001],'kernel': ['linear', 'rbf']}

grid_svm = GridSearchCV(SVC(probability=True, random_state=42),param_grid_svm,cv= 5,scoring='accuracy',n_jobs = -1)
grid_svm.fit(X_train_clf_scaled, y_train_clf)

print("Mejores parámetros SVM:", grid_svm.best_params_)
print("Mejor Accuracy CV:", grid_svm.best_score_)

# Ridge
ridge = Ridge(alpha=1.0, random_state=42)
ridge.fit(X_train_scaled, y_train)
y_pred_ridge = ridge.predict(X_test_scaled)

print("\nResultados Ridge Regression:")
print(f"MAE: {mean_absolute_error(y_test, y_pred_ridge):.2f}")
print(f"MSE: {mean_squared_error(y_test, y_pred_ridge):.2f}")
print(f"R²: {r2_score(y_test, y_pred_ridge):.4f}")

# Lasso
lasso = Lasso(alpha=0.01, random_state=42)
lasso.fit(X_train_scaled, y_train)
y_pred_lasso = lasso.predict(X_test_scaled)

print("\nResultados Lasso Regression:")
print(f"MAE: {mean_absolute_error(y_test, y_pred_lasso):.2f}")
print(f"MSE: {mean_squared_error(y_test, y_pred_lasso):.2f}")
print(f"R²: {r2_score(y_test, y_pred_lasso):.4f}")


# 5. Análisis de resultados y conclusiones (1 punto) 
# • Compara los modelos utilizados y justifica cuál ofrece mejores resultados para la 
# predicción y clasificación. 
# • Relaciona los hallazgos con posibles implicaciones en la seguridad alimentaria 
# global.

# En los análisis de los modelos se observó que tanto la regresión lineal como la regresión polinómica no son
# adecuados para estudiar y predecir la producción de alimentos, como se evidencia en los valores negativos
# de R2. El modelo Ridge también mostró resultados similares, confirmando que los modelos lineales y
# polinómicos no son apropiados para este caso. Por otro lado, los modelos basados en árboles, como el
# Random Forest, mostraron una leve mejoría respecto a los lineales, aunque sin resultados significativamente
# superiores. Los modelos Lasso y polinómicos permanecieron a la par de los lineales, reforzando la
# conclusión de que las regresiones lineales y polinómicas no son las mejores para analizar estos datos.

# Los árboles de decisión y Random Forest fueron los modelos más efectivos, ya que capturan mejor las
# interacciones entre variables y entregan R2 superiores a los modelos lineales. La optimización de parámetros
# mediante GridSearchCV confirmó que estos modelos pueden mejorar su desempeño, respaldando los
# hallazgos anteriores.

# Para la segunda parte del ejercicio, se analizó la variable categórica Impacto usando modelos de
# clasificación. KNN y árbol de decisión lograron un accuracy de 0.8 y F1 ≈ 0.82, mostrando que pudieron
# separar de manera confiable los países en Bajo, Medio y Alto impacto. SVM, en cambio, obtuvo un accuracy
# de 0.6 y F1 ≈ 0.45, evidenciando que no logró separar bien las clases. Tras optimización con GridSearchCV,
# los mejores parámetros para SVM fueron C=0.1 y kernel lineal, con accuracy CV ≈ 0.667, mostrando cierta
# mejora, aunque limitada por el tamaño reducido del dataset.