import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


diciconario = {'tamaño':[50,60,70,80,90,100,None,120],
               'habitaciones':[1,2,2,3,3,3,4,4],
               'ubicacion':[1,1,2,2,3,3,4,4],
               'precio':[150000,170000,190000,210000,230000,270000,290000,310000]}

df = pd.DataFrame(diciconario)


media_tamaño = df['tamaño'].mean()

df['tamaño'] = df['tamaño'].fillna(media_tamaño)

print('\n')
print(media_tamaño.round(2))
print('\n')
print(df)
print('\n')

X = df[['tamaño','habitaciones','ubicacion']]
y = df['precio']
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)
print(X_train)
print('\n')
print(X_test)
print('\n')
print(y_train)
print('\n')
print(y_test)
print('\n') 

## 4 Seleccion del modelo [Regresion lineal]
model = LinearRegression()

## 5 entrenamiento del modelo
model.fit(X_train, y_train)

y_prediccion = model.predict(X_test)

MSE = mean_squared_error(y_test, y_prediccion)

print(f'El valor del error cuadratico medio es: {MSE:.2f}')

## precio = 50.000 + (2.000*x1 × tamaño) + (10.000*x2 × habitaciones) + (-5.000*x3 × ubicacion)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.colorbar(label = 'precio')
plt.xlabel('Componente principal 1')
plt.ylabel('Componente principal 2')
plt.show()
