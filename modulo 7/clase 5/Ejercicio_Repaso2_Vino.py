import kagglehub
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier #construye muchos arboles de manera secuencual y cada arbol nuevo corrige los errores del arbol anterior
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
import joblib
import  numpy as np

# Download latest version
path = kagglehub.dataset_download("uciml/red-wine-quality-cortez-et-al-2009")

print("Path to dataset files:", path)

print("Archivos disponibles:", os.listdir(path))
dataset_path = os.path.join(path, 'winequality-red.csv')
df = pd.read_csv(dataset_path)

#Exploracion de los datos

print(df.head())
print("\n" + "="*80 + "\n")
print(df.info())
print("\n" + "="*80 + "\n")
print(df.describe())
print("\n" + "="*80 + "\n")

df['Buena Calidad'] = (df['quality'].apply(lambda x: 1 if x >= 7 else 0))
print(df['Buena Calidad'].value_counts())

df = df.drop('quality', axis=1)
print(df.head())
print("\n" + "="*80 + "\n")
X = df.drop('Buena Calidad', axis=1)
y = df['Buena Calidad']

#Visualizacion de la distribucion de las variables con Histograma
df.hist(bins=20, figsize=(15,12), color='red')
plt.suptitle('Histograma de la propiedades del vino', fontsize=16)
plt.tight_layout(rect=(0,0.03,1,0.95)) #coordenada de los subgraficos, tight_layout los ajusta
plt.show()
print("\n" + "="*80 + "\n")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Forma del conjunto de entrenamiento:", X_train.shape)
print("Forma del conjunto de prueba:", X_test.shape)
print("\n" + "="*80 + "\n")
#n_est numero de arboles (mas grande mayor precision pero mas lento)
modelo_gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
modelo_gb.fit(X_train, y_train)
print('Entrenamiento completado satisfactoriamente')
print("\n" + "="*80 + "\n")

y_pred = modelo_gb.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy}')
print("\n" + "="*80 + "\n")
print('Matriz de confusion')
print(confusion_matrix(y_test, y_pred))
print("\n" + "="*80 + "\n")
print(classification_report(y_test, y_pred))
print("\n" + "="*80 + "\n")

#Escalar los datos para ver si mejora la presicion
escalador = StandardScaler()
X_train_escalado = escalador.fit_transform(X_train)
X_test_escalado = escalador.transform(X_test)

print("Forma del conjunto de entrenamiento escalado:", X_train_escalado.shape)
print("Forma del conjunto de prueba escalado:", X_test_escalado.shape)
print("\n" + "="*80 + "\n")

modelo_gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
modelo_gb.fit(X_train_escalado, y_train)
print('Entrenamiento completado satisfactoriamente')
print("\n" + "="*80 + "\n")


#Grid search probar diferentes parametros para ver cual ofrece el mejor rendimiento (optimizacion)
param_grid = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 7]
}

#scoring ='accurancy' el modelo buscara el mejor scoring - cv=5 validacion cruzada con 5 folds - verbose=1 nos brinda detalles sobre el grid search (si es = 0 no nos entrega informacion)
gs = GridSearchCV(estimator=modelo_gb, param_grid=param_grid, cv=5, scoring='accuracy', verbose=1)
gs.fit(X_train_escalado, y_train)

print("Mejores parámetros encontrados:")
print(gs.best_params_)
print("\n" + "="*80 + "\n")
print(f'{gs.best_score_:.4f}')
print("\n" + "="*80 + "\n")
modelo_gs = gs.best_estimator_
y_pred = modelo_gs.predict(X_test_escalado)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy}')
print('El modelo entrenado satisfactoriamente')

y_pred = modelo_gb.predict(X_test_escalado)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy}')
print("\n" + "="*80 + "\n")
print('Matriz de confusion')
print(confusion_matrix(y_test, y_pred))
print("\n" + "="*80 + "\n")
print(classification_report(y_test, y_pred))
print("\n" + "="*80 + "\n")

joblib.dump(modelo_gs, 'modelo_vino.pkl')
joblib.dump(escalador, 'escalador_vino.pkl')


def predecir_calidad_vino():
  try:

    modelo_cargado = joblib.load('modelo_vino.pkl')
    escalador_cargado = joblib.load('escalador_vino.pkl')

    print('Ingrese las características del vino:')

    caracteristicas_vino = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']

    entradas_usuario = []

    for caracteristica in caracteristicas_vino:
      valor = float(input(f'Ingrese el valor de {caracteristica}: '))
      entradas_usuario.append(valor)

    nueva_data = np.array(entradas_usuario).reshape(1, -1)
    datos_nuevos_escalados = escalador_cargado.transform(nueva_data)
    prediccion = modelo_cargado.predict(datos_nuevos_escalados)
    print("\n" + "="*80 + "\n")
    if prediccion[0] == 1:
      print("\n" + "="*80 + "\n")
      print('Este es un vino de buena calidad')
    else:
      print("\n" + "="*80 + "\n")
      print('Este es un vino de mala calidad')
  except FileNotFoundError:
    print("\n" + "="*80 + "\n")
    print('Asegurese de que el "modelo_vino.pkl" y el "escalador_vino.pkl" existen en el directorio')
  except ValueError:
    print("\n" + "="*80 + "\n")
    print('Asegurese de ingresar valores válidos para todas las características')

if __name__ == "__main__":
  predecir_calidad_vino()