import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'Horas_de_estudio': [2,3,4,5,6,7,8,9,10,11],
        'Notas': [50,60,65,70,75,80,85,90,95,98]}

df = pd.DataFrame(data)

# Definir variables aparte
X = df[['Horas_de_estudio']]  # DataFrame 2D para variables independientes
y = df['Notas']               # Serie 1D para variable dependiente

modelo = LinearRegression()
modelo.fit(X, y)  # Aquí pasamos las dos variables separadas

error_entrenamiento = 1 - modelo.score(X, y)
print(f'Error de Entrenamiento: {error_entrenamiento:.4f}')
