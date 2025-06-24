# Eres contratado/a por una pequeña cadena de librerías llamada "Libros & Bytes" para desarrollar un 
# sistema que gestione su inventario y permita a los usuarios simular una compra en línea. Trabajarás 
# solo en la lógica del sistema sin preocuparte de la interfaz visual. El sistema debe cumplir con los 
# siguientes requerimientos y funcionalidades.


# 1. Definir variables básicas y tipos de datos (1 punto): 

libros=[{"titulo":"Introduccion a Python","autor":"Omar trejos","precio":18530,"stock":28},
        {"titulo":"El señor de los anillos","autor":"J. R. R. Tolkien","precio":16070,"stock":11},
        {"titulo":"Los Simpson y la filosofía","autor":"William Irwin","precio":24370,"stock":6},
        {"titulo":"Sandman","autor":"Neil Gaiman","precio":37820,"stock":72},
        {"titulo":"Infierno","autor":"Dan Brown","precio":16440,"stock":10}]

# print(libros)

# 2. Control de flujo (1 punto):


# def mostrar_libros_disponibles():
#     for libro in libros:
#         if libro.get("stock")>=1:
#             print(libro)

# mostrar_libros_disponibles()

# # 3. Condiciones y operadores (1 punto): 

# minimo=float(input("Ingrese el precio minimo par filtrar: "))
# maximo=float(input("Ingrese un precio maximo para filtrar: "))

# while True:
#     if minimo>=maximo:
#         print("Minimo no puede ser mayor a maximo")
#         break
#     else:
#         for libro in libros:
#             if libro.get("precio")>=minimo and libro.get("precio")<=maximo:
#                 print(libro)
#         break

# #4. Función personalizada para simular una compra (2 puntos): 


libroN=input("Ingrese el libro que requiere: ")
cantidad=input("Ingrese la cantidad de libros que necesita: ")

def comprar_libros(libroN, cantidad):
    for libro in libros:
        if libroN.lower == libro.get("titulo").lower and libro("stock")>=cantidad:
            print("hola")
        else:
             print(libro)
comprar_libros(libroN, cantidad)