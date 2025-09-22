# Ejercicio 8: Juego de Adivinanza (Bucle while)

# Crea un juego simple donde el programa "piensa" en un número aleatorio entre 1 y 10, y el
# usuario tiene que adivinarlo. El juego continúa hasta que el usuario adivina el número correcto.



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