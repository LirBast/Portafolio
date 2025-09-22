import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve,accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

num_clientes = 1000
ingresos = np.random.normal(loc=50000, scale=15000, size=num_clientes)
deuda = np.random.normal(loc=15000, scale=7000, size=num_clientes)
historial_cred = np.random.randint(300, 850, num_clientes)
riesgo = ((deuda / ingresos > 0.3) | (historial_cred < 600)).astype(int)

df = pd.DataFrame({'Ingresos': ingresos,
                   'Deuda': deuda,
                   'Historial_cred': historial_cred,
                   'Riesgo': riesgo})
print(df.head())
print(df['Riesgo'].value_counts())

X = df[['Ingresos', 'Deuda', 'Historial_cred']]
y = df['Riesgo']

# 1) Split antes de escalar (evita fuga de datos)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f'Tamaño del conjunto de entrenamiento: {X_train.shape}')
print(f'Tamaño del conjunto de pruebas: {X_test.shape}')
print(f'Proporcion de riesgo en y_train:\n{y_train.value_counts(normalize=True)}')
print(f'Proporcion de riesgo en y_test:\n{y_test.value_counts(normalize=True)}')

# 2) Escalado: ajustar con train y aplicar a train/test
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.transform(X_test)

# 3) Modelo
modelo = LogisticRegression(solver='liblinear', random_state=42)
modelo.fit(X_train_scaled, y_train)

print('\nCoeficiente del Modelo')
for i, col in enumerate(X.columns):
    print(f'{col}: {modelo.coef_[0][i]:.4f}')
print(f'Intercepto: {modelo.intercept_[0]:.4f}')

# 4) Cliente ficticio (lista de listas)
cliente_fic = pd.DataFrame([[50000, 20000, 550]], columns=X.columns)
cliente_fic_scaled = ss.transform(cliente_fic)
p_riesgo = modelo.predict_proba(cliente_fic_scaled)[0]
print(f'Probabilidad de bajo riesgo para el cliente ficticio: {p_riesgo[0]:.4f}')
print(f'Probabilidad de alto riesgo para el cliente ficticio: {p_riesgo[1]:.4f}')

# 5) Predicciones y probabilidades
y_pred_proba = modelo.predict_proba(X_test_scaled)[:, 1]  # prob de clase positiva (alto riesgo)
y_pred = modelo.predict(X_test_scaled)

# 6) Matriz de confusión
mc = confusion_matrix(y_test, y_pred)
print(mc)

plt.figure(figsize=(6, 5))
sns.heatmap(mc, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['bajo riesgo (0)', 'alto riesgo (1)'],
            yticklabels=['bajo riesgo (0)', 'alto riesgo (1)'])
plt.xlabel('Predicción')
plt.ylabel('Valor real')
plt.title('Matriz de Confusión')
plt.show()

print(f'\nVerdaderos positivos (VP): {mc[1, 1]}')
print(f'Verdaderos negativos (VN): {mc[0, 0]}')
print(f'Falsos positivos (FP): {mc[0, 1]}')
print(f'Falsos negativos (FN): {mc[1, 0]}')

# 7) Métricas
acc_s = accuracy_score(y_test, y_pred)
prec_sco = precision_score(y_test, y_pred)
recall_sco = recall_score(y_test, y_pred)
f1_scr = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

print(f'\nAccuracy Score: {acc_s:.4f}')
print(f'Precision Score: {prec_sco:.4f}')
print(f'Recall Score: {recall_sco:.4f}')
print(f'F1 Score: {f1_scr:.4f}')
print(f'ROC AUC Score: {roc_auc:.4f}')

# 8) Curva ROC
fpr, tpr, threshold = roc_curve(y_test, y_pred_proba)
print(f'\nFalse Positive Rate (FPR): {fpr}')
print(f'True Positive Rate (TPR): {tpr}')
print(f'Umbrales de decisión: {threshold}')

# 9) Gráfico ROC
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='red', label=f'ROC (AUC = {roc_auc:.3f})')
plt.plot([0, 1], [0, 1], color='blue', linestyle='--', lw=2, label='Azar')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Tasa de Falsos Positivos (FPR)')
plt.ylabel('Tasa de Verdaderos Positivos (TPR)')
plt.title('Curva ROC')
plt.legend(loc='lower right')
plt.show()

param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'penalty': ['l2'],
    'solver': ['liblinear']
}

log_reg = LogisticRegression(random_state = 42)

grid = GridSearchCV(log_reg, param_grid, cv = 5, scoring = 'roc_auc', n_jobs = -1)
grid.fit(X_train_scaled, y_train)

best_log_reg = grid.best_estimator_

print(f'\nMejores Parametros encontrados: {grid.best_params_}')
print(f'\nMejor Puntuacion AUC : {grid.best_score_:.4f}')
print(f'Mejor modelo entrenado: {best_log_reg}')

y_pred_proba_opt = best_log_reg.predict_proba(X_test)[:,1]

auc_opt = roc_auc_score(y_test, y_pred_proba_opt)
print(f'AUC del modelo optimizado en el conjunto de prueba: {auc_opt}')

modelo_base = LogisticRegression(solver = 'liblinear', random_state = 42)
modelo_base.fit(X_train, y_train)
y_pred_proba_base = modelo_base.predict_proba(X_test)[:,1]
auc_base = roc_auc_score(y_test, y_pred_proba_base)
print(f'AUC del modelo base en el conjunto de prueba: {auc_base}')

if auc_opt > auc_base:
  print('El modelo optimizado mejoro el rendimiento.')
else:
  print('El modelo optimizado no mostro mejoria o empeoro')