import numpy as np


arreglo=np.arange(0,10,2)    ### el primer dato cero de esta funcion es de donde empieza y el 10 hasta donde llega, y el 2 que vaya de 2 en 2 hasta el limite
print(arreglo)

arreglo123=np.arange(1000)   ### me genera datos hasta 1000 datos pero de forma secuencial  
print(arreglo123)

matriz_ceros=np.zeros((2,3))   ###hay que ingresar las dimensions como si fuera una tupla, por eso van entre parentesis dentro
print(matriz_ceros)

matriz_unos=np.ones((4,5)) 
print(matriz_unos)

matriz_random=np.random.randint(1,100,((3,3)))
print(matriz_random)

arr=np.array([10,20,30,40,50,60,70])

## indexacion basica
print("Elemento en posicion 2:",arr[2])

### slicin[star:stor:step]
print("elemento del 1 al 4: ", arr[1:5]) # hay que tener encuenta que al colocar los limites para mostrar valores, los limites son abiertos
print("elementos pares: ", arr[::2])   # muestra las posiciones de los pares de lista

#indexacion boolenaa
condicion=arr>35
print("Condicion arr:35: ", condicion)    ### esto solo me hace una comparacion entre la condicion y la variable
print("elementos arr>35: ",arr[condicion])  ### aca me muestra los valores que si cumplen con la condicion


matriz5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matriz5[1,2])
print(matriz5[0:])
print(matriz5[:,2])
print(matriz5[:,-1])
