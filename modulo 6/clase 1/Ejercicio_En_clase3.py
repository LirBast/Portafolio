import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
data = {'Horas_de_estudio': [2,3,4,5,6,7,8,9,10,11],
        'Notas': [50,60,65,70,75,80,85,90,95,98]}

df = pd.DataFrame(data)

modelo = LinearRegression()
modelo.fit(df[['Horas_de_estudio']], df['Notas'])

error_entrenamiento = 1 - modelo.score(df[['Horas_de_estudio']], df['Notas'])
print(f'Error de Entrenamiento: {error_entrenamiento:.2f}')

X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(df[['Horas_de_estudio']], df['Notas'], test_size=0.2, random_state=42)

modelo.fit(X_entrenamiento, y_entrenamiento)

error_de_prueba = 1 - modelo.score(X_prueba, y_prueba)
print(f'El error de prueba es: {error_de_prueba:.2f}')

### Sobreajuste

poly = PolynomialFeatures(degree=10)
x_poly = poly.fit_transform(X_entrenamiento)
modelo.fit(x_poly, y_entrenamiento)

print(x_poly)

### Ajuste Apropiado (polimonio de grado 2)

poly2 = PolynomialFeatures(degree=10)
x_poly2 = poly2.fit_transform(X_entrenamiento)
modelo.fit(x_poly2, y_entrenamiento)

print(x_poly)