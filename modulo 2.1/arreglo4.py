import numpy as np


##creacion de un vector
vector=np.array([1,2,3,4,5])
print(f"Dimensiones: {vector.shape}")
print(f"Tipo de datos:{vector.dtype}")

##creacion de una matriz

matriz=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)
print(matriz.shape)


### creacion de tensor 3D (2x2x2)

tensor=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(tensor)
print(tensor.shape)
