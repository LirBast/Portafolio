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


# 1. Carga y exploración de datos (1 punto)

df = pd.read_csv(r'C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 6\consolidado\cambio_climatico_agricultura.csv')

# Exploración inicial de los datos

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

# 2. Preprocesamiento y escalamiento de datos (2 puntos) 


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

# modelo 1 lineal

model = LinearRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Resultados Regresión Lineal:")
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"R2: {r2:.4f}")

# Polinómica
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
y_pred_poly = poly_model.predict(X_test_poly)

mse_poly = mean_squared_error(y_test, y_pred_poly)
mae_poly = mean_absolute_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print("Resultados Regresión Polinómica:")
print(f"MAE: {mae_poly:.2f}")
print(f"MSE: {mse_poly:.2f}")
print(f"R2: {r2_poly:.4f}")

# Árbol de Decisión
tree_model = DecisionTreeRegressor(random_state=42, max_depth=5)
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)

mse_tree = mean_squared_error(y_test, y_pred_tree)
mae_tree = mean_absolute_error(y_test, y_pred_tree)
r2_tree = r2_score(y_test, y_pred_tree)

print("Resultados Árbol de Decisión:")
print(f"MAE: {mae_tree:.2f}, MSE: {mse_tree:.2f}, R2: {r2_tree:.4f}")

# Random Forest
rf_model = RandomForestRegressor(n_estimators=200, max_depth=6, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

mse_rf = mean_squared_error(y_test, y_pred_rf)
mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print("Resultados Random Forest:")
print(f"MAE: {mae_rf:.2f}, MSE: {mse_rf:.2f}, R2: {r2_rf:.4f}")


df_v2 = df.copy()

# Crear variable categórica Impacto
promedio = df_v2["Producción_alimentos"].mean()
desvia = df_v2["Producción_alimentos"].std()

def clasificar_std(valor):
    if valor < promedio - desvia:
        return "Bajo"
    elif valor > promedio + desvia:
        return "Alto"
    else:
        return "Medio"

df_v2["Impacto"] = df_v2["Producción_alimentos"].apply(clasificar_std)

# Variables clasificación
X_clf = df_v2[["Temperatura_promedio", "Cambio_lluvias", "Frecuencia_sequías"]]
y_clf = df_v2["Impacto"]

# Train/Test
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42, stratify=y_clf
)

# Escalado
scaler_clf = StandardScaler()
X_train_clf_scaled = scaler_clf.fit_transform(X_train_clf)
X_test_clf_scaled = scaler_clf.transform(X_test_clf)

# Modelos
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

# ============================
# 5. Evaluación Clasificación
# ============================
# --- KNN ---
print("\n=== Resultados KNN ===")
print("Accuracy:", accuracy_score(y_test_clf, y_pred_knn))
print("Precisión:", precision_score(y_test_clf, y_pred_knn, average='weighted'))
print("Sensibilidad (Recall):", recall_score(y_test_clf, y_pred_knn, average='weighted'))
print("F1-Score:", f1_score(y_test_clf, y_pred_knn, average='weighted'))

cm_knn = confusion_matrix(y_test_clf, y_pred_knn)
sns.heatmap(cm_knn, annot=True, fmt="d", cmap="Blues")
plt.title("Matriz de Confusión - KNN")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.show()

# --- Árbol ---
print("\n=== Resultados Árbol de Decisión ===")
print("Accuracy:", accuracy_score(y_test_clf, y_pred_tree_clf))
print("Precisión:", precision_score(y_test_clf, y_pred_tree_clf, average='weighted'))
print("Sensibilidad (Recall):", recall_score(y_test_clf, y_pred_tree_clf, average='weighted'))
print("F1-Score:", f1_score(y_test_clf, y_pred_tree_clf, average='weighted'))

cm_tree = confusion_matrix(y_test_clf, y_pred_tree_clf)
sns.heatmap(cm_tree, annot=True, fmt="d", cmap="Greens")
plt.title("Matriz de Confusión - Árbol de Decisión")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.show()

# --- SVM ---
print("\n=== Resultados SVM ===")
print("Accuracy:", accuracy_score(y_test_clf, y_pred_svm))
print("Precisión:", precision_score(y_test_clf, y_pred_svm, average='weighted'))
print("Sensibilidad (Recall):", recall_score(y_test_clf, y_pred_svm, average='weighted'))
print("F1-Score:", f1_score(y_test_clf, y_pred_svm, average='weighted'))

cm_svm = confusion_matrix(y_test_clf, y_pred_svm)
sns.heatmap(cm_svm, annot=True, fmt="d", cmap="Oranges")
plt.title("Matriz de Confusión - SVM")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.show()

# ============================
# 6. Curvas ROC One-vs-Rest
# ============================
y_test_bin = label_binarize(y_test_clf, classes=["Bajo", "Medio", "Alto"])
y_prob_svm = svm_clf.predict_proba(X_test_clf_scaled)

for i, clase in enumerate(["Bajo", "Medio", "Alto"]):
    fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_prob_svm[:, i])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f"{clase} (AUC = {roc_auc:.2f})")

plt.plot([0,1],[0,1],'k--')
plt.xlabel("Tasa de Falsos Positivos")
plt.ylabel("Tasa de Verdaderos Positivos")
plt.title("Curvas ROC - SVM One-vs-Rest")
plt.legend()
plt.show()
