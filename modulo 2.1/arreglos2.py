import numpy as np        ### aca se estan importando las funciones para 
import time

numeros=[1,2,3,4,5,6,7,8,9,10]
print(numeros)

inicio=time.time()
lista_python=list(range(1000000))
print(lista_python[0])
print(f"El proceso tuvo un duracion de: {time.time()-inicio}")

inicio2=time.time()
arreglo_python=np.arange(1,1000000)      ### usar numpy es mas rapido 
print(arreglo_python[5])
print(f"El proceso tuvo un duracion de: {time.time()-inicio2}")

# inicio=time.time()   ### una variable para darle inicio al proceso y ver cuanto se demora
# duplicados=[numero*2 for numero in numeros]
# print(duplicados)
# print(f"El proceso tuvo un duracion de: {time.time()-inicio}")