## 1.-Importar la librería NumPy

import numpy as np


## 2.- Crear un vector de 10 elementos con valores del 1 al 10 utilizando arange()


vector=np.arange(1,11,1)
print('\n')
print('La matriz vector de 10 valores es: ')
print(vector)
print('\n')
## 3.-Generar una matriz de 3x3 con valores aleatorios entre 0 y 1 usando random.rand()

matriz=np.random.rand(3,3)
print('La matriz random de 3 por 3 e:')
print(matriz)
print('\n')
## 4.- Crear una matriz identidad de tamaño 4x4 utilizando eye()

matriz_identidad=np.eye(4,4)
print('La matriz identidad de 4 por 4 es:')
print(matriz_identidad)
print('\n')
## 5.- Redimensionar el vector creado en el punto 2 en una matriz de 2x5 usando .reshape()

matriz_redimensionada=vector.reshape(2,5)
print('\n')
print('El vector original de 10 valores es:')
print(vector)
print('\n')
print('La matriz redimensionada del vector es:')
print(matriz_redimensionada)

## 6.- Seleccionar los elementos mayores a 5 del vector original y mostrarlos

print('\n')
print('El vector original de 10 valores es:')
print(vector)

mayores_a_5=[]

for vec in vector:
    if vec >5:
        mayores_a_5.append(int(vec))
print('\n')
print(f'Los valores mayores a 5 del vector son: {mayores_a_5}')
print('\n')
## 7.- Realizar una operación matemática entre arreglos

arreg_1=np.arange(1,10,2)
arreg_2=np.arange(1,15,3)

print('El arreglo 1 es:')
print(arreg_1)
print('\n')
print('El arreglo 2 es:')
print(arreg_2)
print('\n')
suma_de_arrglos=arreg_1 + arreg_2
print('La suma del arreglo 1 y del arreglo 2:')
print(suma_de_arrglos)

## 8.- Aplicar una función matemática a un arreglo

print('\n')
print('El vector original de 10 valores es:')
print(vector)

raiz_cuadrada=np.sqrt(vector)

print('\n')
print('La raiz cudrada del vector original es')
print(raiz_cuadrada)