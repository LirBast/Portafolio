import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut, cross_val_predict, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Datos: horas de estudio y porcentaje de asistencia a clases
X = np.array([[5, 80], [7, 85], [6, 90], [8, 75], [7, 70],
              [9, 95], [10, 90], [4, 60], [6, 65], [8, 88],
              [5, 50], [7, 78], [6, 82], [9, 92], [10, 85]])
y = np.array([1,1,1,1,0,
              1,1,0,0,1,
              0,1,1,1,1])

# Crear DataFrame para visualizar
df = pd.DataFrame(X, columns=['Horas_estudio','Asistencias_a_Clases'])
df['Nota_Final'] = y
print(df)

# Dividir datos: 70% entrenamiento, 30% prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42) 

# Mostrar dimensiones de los conjuntos
print('\nDimensiones de los conjuntos de Datos')
print(f'X_train (entrenamiento - características): {X_train.shape}')
print(f'y_train (entrenamiento - etiquetas): {y_train.shape}')
print(f'X_test  (prueba - características): {X_test.shape}')
print(f'y_test  (prueba - etiquetas): {y_test.shape}')

# Entrenar modelo
modelo = DecisionTreeClassifier()
modelo.fit(X_train , y_train)
y_pred = modelo.predict(X_test)
accuracy = accuracy_score(y_test , y_pred)
print(f'Exactitud del modelo: {accuracy:.2f}')

# Validación cruzada con KFold
kf = KFold(n_splits=5, shuffle=True, random_state=42)
accuracies_kfold = []

for fold, (train_index, test_index) in enumerate(kf.split(X)):
    X_train_fold, X_test_fold = X[train_index], X[test_index]
    y_train_fold, y_test_fold = y[train_index], y[test_index]

    model_kfold = DecisionTreeClassifier(random_state=42)
    model_kfold.fit(X_train_fold, y_train_fold)
    y_pred_kfold = model_kfold.predict(X_test_fold)

    accuracy_kfold = accuracy_score(y_test_fold, y_pred_kfold)
    accuracies_kfold.append(accuracy_kfold)
    print(f'Exactitud del modelo en el fold {fold+1}: {accuracy_kfold:.2f}')

media_accuracies_kfold = np.mean(accuracies_kfold)
std_accuracies_kfold = np.std(accuracies_kfold)
print(f'Media de las exactitudes en los folds: {media_accuracies_kfold:.2f}')
print(f'Desviación estándar de las exactitudes en los folds: {std_accuracies_kfold:.2f}')

# Validación cruzada con cross_val_score (KFold)
kfold_scores = cross_val_score(DecisionTreeClassifier(random_state=42), X, y, cv=kf, scoring='accuracy')
print(f'Precisión por subconjunto (KFold_cross_val_score): {kfold_scores}')
print(f'Media de la precisión: {kfold_scores.mean():.2f}')
print(f'Desviación estándar de la precisión: {kfold_scores.std():.2f}')

# Validación Leave-One-Out (LOO)
loo = LeaveOneOut()
loo_scores = cross_val_score(DecisionTreeClassifier(random_state=42), X, y, cv=loo, scoring='accuracy')
print(f'Exactitudes LOO: {loo_scores}')
print(f'Media de la exactitud LOO: {loo_scores.mean():.2f}')
print(f'Desviación estándar de la exactitud LOO: {loo_scores.std():.2f}')
