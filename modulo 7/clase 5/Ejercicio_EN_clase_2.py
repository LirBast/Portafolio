import kagglehub
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestClassifier

# Download latest version
path = kagglehub.dataset_download("fedesoriano/heart-failure-prediction")

print("Path to dataset files:", path)

print("Archivos disponibles:", os.listdir(path))
dataset_path = os.path.join(path, 'heart.csv')
df = pd.read_csv(dataset_path)

#Exploracion de la data

print(df.info())
print(df.describe())

#Preprocesamiento de la data

columnas_categoricas = df.select_dtypes(include=['object']).columns.tolist()
print(columnas_categoricas)

df_procesado = pd.get_dummies(df, columns=columnas_categoricas, drop_first=True) #dropfirst TRUE evita colinealidad
df_procesado.head()

#Division del dataset en un conjunto de entrenamiento y prueba 80-20
#Definicion de variables

X = df_procesado.drop('HeartDisease', axis=1) #se elimina la columna objetivo
y = df_procesado['HeartDisease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f'Forma del conjunto de entrenamiento: {X_train.shape, y_train.shape}')
print(f'Forma del conjunto de prueba: {X_test.shape, y_test.shape}')
print('\n'+'='*80+'\n')

#Evaluacion del modelo

modelo_logistico = LogisticRegression(max_iter=1000)
modelo_logistico.fit(X_train, y_train)
y_pred = modelo_logistico.predict(X_test)

precision = accuracy_score(y_test, y_pred)
print(f'Precision: {precision:.2f}') #85% de las veces que el modelo predice acierta
print('\n'+'='*80+'\n')

matriz_confusion = confusion_matrix(y_test, y_pred)
print("Matriz de confusión:")
print(matriz_confusion)
print('\n'+'='*80+'\n')

reporte_clasificacion = classification_report(y_test, y_pred)
print("Reporte de clasificación:")
print(reporte_clasificacion)

#Curva roc Nos permite evaluar el rendimiento del modelo de clasificacion en diferentes umbrales
#AOC Resume el rendimiento del modelo en un solo numero
#obtener la prob de pertenencia
y_pred_proba = modelo_logistico.predict_proba(X_test)[:,1]

fpr, tpr, threeholds = roc_curve(y_test, y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)
print('\n'+'='*80+'\n')
print(f'AUC (Area bajo la curva): {auc:.2f}') #90% de prob de distinguir uno aleatorio sano y uno enfermo
print('\n'+'='*80+'\n')

plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}',)
plt.plot([0,1],[0,1],'k--',label='Modelo aleatorio AUC 0.5')
plt.xlabel('Tasa de falsos positivos (FPR)')
plt.ylabel('Tasa de verdaderos positivos(TPR)')
plt.title('Curva ROC')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()

#Arboles de desicion

modelo_arbol = DecisionTreeClassifier(random_state=42)  # max_depth=5
modelo_arbol.fit(X_train, y_train)
y_pred_arbol = modelo_arbol.predict(X_test)

precision_arbol = accuracy_score(y_test, y_pred_arbol)
print(f'Precision del modelo de árbol de decisión: {precision_arbol:.2f}')
print('\n'+'='*80+'\n')

matriz_confusion_arbol = confusion_matrix(y_test, y_pred_arbol)
print("Matriz de confusión del modelo de árbol de decisión:")
print(matriz_confusion_arbol)
print('\n'+'='*80+'\n')

reporte_clasificacion_arbol = classification_report(y_test, y_pred)
print("Reporte de clasificación:")
print(reporte_clasificacion_arbol)
#presicion de todas las pred (+) cuantas fueron realmente correctas
#recall sensibilidad cuantos casos logro detectar positivos reales, el modelo logro identificar el 86% de los pacientes
#f1 score es un promedio armonico entre las dos variables anteriores

y_pred_proba = modelo_arbol.predict_proba(X_test)[:,1]

fpr, tpr, threeholds = roc_curve(y_test, y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)
print('\n'+'='*80+'\n')
print(f'AUC (Area bajo la curva): {auc:.2f}') #90% de prob de distinguir uno aleatorio sano y uno enfermo
print('\n'+'='*80+'\n')

plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}',)
plt.plot([0,1],[0,1],'k--',label='Modelo aleatorio AUC 0.5')
plt.xlabel('Tasa de falsos positivos (FPR)')
plt.ylabel('Tasa de verdaderos positivos(TPR)')
plt.title('Curva ROC')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()

#Random Forest, construye multiple arboles de desiciones, es una votacion de todos los arboles

modelo_rf = RandomForestClassifier(random_state=42, n_estimators=100)  # max_depth=5
modelo_rf.fit(X_train, y_train)
y_pred_rf = modelo_rf.predict(X_test)

precision_rf = accuracy_score(y_test, y_pred_rf)
print(f'Precision del modelo de árbol de decisión: {precision_rf:.2f}')
print('\n'+'='*80+'\n')

matriz_confusion_rf = confusion_matrix(y_test, y_pred_rf)
print("Matriz de confusión del modelo de árbol de decisión:")
print(matriz_confusion_rf)
print('\n'+'='*80+'\n')

reporte_clasificacion_rf = classification_report(y_test, y_pred_rf)
print("Reporte de clasificación:")
print(reporte_clasificacion_rf)
#presicion de todas las pred (+) cuantas fueron realmente correctas
#recall sensibilidad cuantos casos logro detectar positivos reales, el modelo logro identificar el 86% de los pacientes
#f1 score es un promedio armonico entre las dos variables anteriores

y_pred_proba = modelo_rf.predict_proba(X_test)[:,1]

fpr, tpr, threeholds = roc_curve(y_test, y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)
print('\n'+'='*80+'\n')
print(f'AUC (Area bajo la curva): {auc:.2f}') #90% de prob de distinguir uno aleatorio sano y uno enfermo
print('\n'+'='*80+'\n')

plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}',)
plt.plot([0,1],[0,1],'k--',label='Modelo aleatorio AUC 0.5')
plt.xlabel('Tasa de falsos positivos (FPR)')
plt.ylabel('Tasa de verdaderos positivos(TPR)')
plt.title('Curva ROC')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()
