import numpy as np

datos_originales=np.array([1,10,100,1000])

datos_log=np.log(datos_originales)   ### se le aplica el logaritmo a los datos del arreglo
print(datos_originales)
print(datos_log)


x=np.array([[1,1,1],[1,2,3],[1,3,4]])
print(x)
xtx=x.T   ### es para sacar la transpuesta de la matriz x
print(xtx)

det=np.linalg.det(x)
print(det)


datos=np.random.normal(0,1,100)
print(datos)
print(np.mean(datos))
print(np.std(datos))
print(np.max(datos))

arreglo=np.array([1,2,3,4,5,6,7,8,9])
arreglo2=arreglo.reshape(3,3)
print(arreglo2)