import random as r   # import es para importar el modulo de una libreria

num_random = r.randint(1, 10)
num_usuario = int(input("adivina un número entre 1 y 10: "))
    
if num_usuario == num_random:
        print("¡Has acertado!")
else:
        print("fallaste, quieres volver a intertarlo? (s/n)")
if respuesta =="n":
        print("gracias por jugar")

# El módulo random proporciona funciones para generar números aleatorios
# El método randint(a, b) devuelve un número entero aleatorio entre a y b, ambos incluidos.


# hay que tener cuidado con las mayusculas, y tengo que converitr la respuesta a minusculas
respuesta = input("¿Quieres volver a intentarlo? (s/n): ").lower()

## tengo que ver el tema de como resolver cuando el usuario ingresa un valor que no es un número
if respuesta == "s":
    num_random = r.randint(1, 10)
    num_usuario = int(input("adivina un número entre 1 y 10: "))
    
    if num_usuario == num_random:
        print("¡Has acertado!")
    else:
        print(f"fallaste, el número era {num_random}.")

## tengo que resolver si gana y quiere quedarse a jugar o salir del juego
else:
    print("Gracias por jugar")



import random as r
 
respuesta = 'Y'
 
while respuesta.upper() == 'Y':
  num_random = r.randint(1, 10)
 
  num_usuario = int(input('Adivina el número: '))
 
  if num_usuario == num_random:
    print('Adivinaste :D')
    respuesta = input('Quieres seguir jugando? Y / N: ')
  else:
    respuesta = input('Fallaste :( ¿quieres volver a intentarlo? Y / N: ')
    if respuesta.upper() == 'N':
      print('Gracias por participar.')