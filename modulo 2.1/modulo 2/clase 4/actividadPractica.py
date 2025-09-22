import statistics
import random
# # DataPro Solutions

# Punto 1

def calcular_area_rectangulo(largo, ancho):
    return largo*ancho

resultado = calcular_area_rectangulo(5, 3)
print(f'El área del rectángulo es:', resultado)


# Punto 2

def calcular_circunferencia(radio):
    return radio*2*3.1416

resultado1=calcular_circunferencia(5)
print(f'La circunferencia es',resultado1)

# Punto 3

def calcular_promedio(a,b,c,d,e):
    return sum([a,b,c,d,e])/5

resultado2=calcular_promedio(1,2,3,4,5)
print(f'el promedio es', resultado2)

# Punto 3.1

def calcular_promedio2(numeros):
    if len(numeros)==0:
        return 0
    return sum(numeros)/len(numeros)

lista=[1,2,3,4,5]
promedio=calcular_promedio2(lista)
print(f'El promedio es',promedio)

# Punto 4

promedio2=statistics.mean(lista)
print(f'El promedio es',promedio2)

# Punto 5

def generar_numeros_aleatorios(cantidad,limite):
    return [random.randint(1,limite) for i in range(cantidad)]

aleatorios =generar_numeros_aleatorios(5,100)
print(f'Numeros aleatorios', aleatorios)
