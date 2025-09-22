import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

np.random.seed(42)

X=np.array([[100,2], #Casa 1
            [150,3], #Casa 2
            [200,4], #Casa 3
            [250,4], #Casa 4
            [300,5]]) #Casa 5

y=np.array([250,350,480,550,650])

X_media=np.mean(X, axis=0)
X_desv=np.std(X, axis=0)
X_normalizada=(X-X_media)/X_desv

y_media=np.mean(y, axis=0)
y_desv=np.std(y, axis=0)
y_normalizada=(y-y_media)/y_desv

modelo_deep=Sequential()
#Capa de entrada y primera capa oculta
modelo_deep.add(Dense(units=64, input_dim=2, activation='relu'))
#Segunda capa oculta
modelo_deep.add(Dense(units=32, activation='relu'))
#Tercera capa oculta
modelo_deep.add(Dense(units=16, activation='relu'))
#Capa de salida
modelo_deep.add(Dense(units=1, activation=None))

#Compilacion
modelo_deep.compile(optimizer='adam', loss='mean_squared_error')

modelo_deep.summary()

history_deep=modelo_deep.fit(X_normalizada, y_normalizada, epochs=500, verbose=0)



plt.plot(history_deep.history['loss'])
plt.title('Perdida de la red profunda')
plt.ylabel('Perdida')
plt.xlabel('Época')
plt.show()

nueva_casa=np.array([[180,3]])
nueva_casa_normalizada=(nueva_casa-X_media)/X_desv

precio_predicho_normalizado=modelo_deep.predict(nueva_casa_normalizada, verbose=0)
precio_predicho=(precio_predicho_normalizado*y_desv)+y_media

print(f'La prediccion(deep learning): ${precio_predicho[0][0]:.2f} miles de dolares')

modelo_simple=Sequential()
modelo_simple.add(Dense(units=1, input_dim=2, activation=None))

modelo_simple.compile(optimizer='adam', loss='mean_squared_error')

history_simple=modelo_simple.fit(X_normalizada, y_normalizada, epochs=100, verbose=0)

precio_predicho_simple_norm=modelo_simple.predict(nueva_casa_normalizada, verbose=0)
precio_predicho_simple=(precio_predicho_simple_norm*y_desv)+y_media

print(f'Prediccion(Modelo Simple): ${precio_predicho_simple[0][0]:.2f} miles de dolares')