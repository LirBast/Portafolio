# Ejercicio 4: Clasificador de Estaciones del Año
# Pide al usuario que ingrese un número de mes (del 1 al 12) y determina a qué estación del año pertenece. (Considera un esquema simple para las estaciones).

mes= input("ingrese un numero entre 1 y 12 que corresponde a un mes del año: ")
if mes in ["1", "2", "3"]:
    print("El mes corresponde al verano")
elif mes in ["4", "5", "6"]:
    print("El mes corresponde al otoño")
elif mes in ["7", "8", "9"]:
    print("El mes corresponde al invierno")
elif mes in ["10", "11", "12"]:
    print("El mes corresponde a la primavera")
else:
    print("El mes ingresado no es válido. Debe ser un número entre 1 y 12.")
