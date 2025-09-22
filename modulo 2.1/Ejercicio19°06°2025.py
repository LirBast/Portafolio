import numpy as np
import time

notas_c1=[22,73,56,44,100]
print(notas_c1)
notas_c2=np.array([78,89,95,100,75])
long=len(notas_c1)

print(notas_c2)
print(long)

inicio=time.time()
suma=0
for nota in notas_c1:
    suma+=nota

promedio=suma/long

print(f"el promedio de las notas es: {promedio}")
print(inicio)

inicio2=time.time()
suma2=np.sum(notas_c2)
print(suma2)

long2=np.size(notas_c2)

print(long2)
print(inicio2)

promedio2=suma2/long2

print(promedio2)

inicio3=time.time()

media=np.mean(notas_c2)   ### Se puede calcular el promedio de forma directa mas facil

print(media)
print(inicio3)


