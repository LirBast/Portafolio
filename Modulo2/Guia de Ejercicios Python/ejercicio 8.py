# Ejercicio 8: Juego de Adivinanza (Bucle while)

# Crea un juego simple donde el programa "piensa" en un número aleatorio entre 1 y 10, y el
# usuario tiene que adivinarlo. El juego continúa hasta que el usuario adivina el número correcto.

import random

numero = random.randint(1, 10)
numero2 = int(input("Ingresa un numero del 1 al 10: "))

while numero2 != numero:
    if numero2!=numero:
        i