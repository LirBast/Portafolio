import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

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

print(f'Caracteristicas normalizadas: \n{X_normalizada}')
print(f'Precio normalizado: \n{y_normalizada}')

modelo_seq=Sequential()
modelo_seq.add(Dense(units=1, input_dim=2, activation=None))
modelo_seq.compile(optimizer='adam', loss='mean_squared_error')
modelo_seq.summary()

history=modelo_seq.fit(X_normalizada,y_normalizada, epochs=100, verbose=0)

import matplotlib.pyplot as plt

plt.plot(history.history['loss'])
plt.title('Historial de perdida (loss) durante el entrenamiento')
plt.xlabel('Epoca')
plt.ylabel('Perdida(MSE)')
plt.show()

nueva_casa=np.array([[180,3]])
nueva_casa_normalizada=(nueva_casa-X_media)/X_desv
precio_pre_normalizado=modelo_seq.predict(nueva_casa_normalizada, verbose=0)
precio_pre=(precio_pre_normalizado*y_desv)+y_media
print(f'Prediccion para una casa de 180m2 de 3 habitaciones: {precio_pre[0][0]:.2f} miles de dolares')