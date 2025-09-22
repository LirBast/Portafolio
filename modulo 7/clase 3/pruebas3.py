import numpy as np
from sklearn.preprocessing import StandardScaler

X_train = np.array([[10.0],[12.0],[14.0]])  # datos de entrenamiento (una sola columna)
X_test  = np.array([[16.0]])                # dato nuevo (test)

scaler = StandardScaler()
scaler.fit(X_train)              # aprende: media=12.0, desv=~1.632
print("media aprendida:", scaler.mean_)
print("varianza aprendida:", scaler.var_)

print("train escalado:", scaler.transform(X_train).ravel())
print("test escalado:",  scaler.transform(X_test).ravel())