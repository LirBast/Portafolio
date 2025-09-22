# Eres contratado/a por una pequeña cadena de librerías llamada "Libros & Bytes" para desarrollar un 
# sistema que gestione su inventario y permita a los usuarios simular una compra en línea. Trabajarás 
# solo en la lógica del sistema sin preocuparte de la interfaz visual. El sistema debe cumplir con los 
# siguientes requerimientos y funcionalidades.


# 1. Definir variables básicas y tipos de datos (1 punto): 

libros=[{"titulo":"Introduccion a Python","autor":"Omar trejos","precio":18530,"stock":28},
        {"titulo":"El señor de los anillos","autor":"Tolkien","precio":16070,"stock":11},
        {"titulo":"Los Simpson y la filosofía","autor":"William Irwin","precio":24370,"stock":6},
        {"titulo":"Sandman","autor":"Neil Gaiman","precio":37820,"stock":72},
        {"titulo":"Infierno","autor":"Dan Brown","precio":16440,"stock":10}]

# print(libros)

# 2. Control de flujo (1 punto):

# Implementa una función llamada mostrar_libros_disponibles() que recorra la lista de
# libros y muestre en pantalla los libros que tienen más de una unidad en stock usando
# una sentencia for y una condición if.

# def mostrar_libros_disponibles():
#     for libro in libros:
#         if libro.get("stock")>=1:
#             print(libro)

# mostrar_libros_disponibles()

# 3. Condiciones y operadores (1 punto): 

# Solicita al usuario que ingrese un rango de precios (mínimo y máximo) y utiliza una
# sentencia if elif else para filtrar los libros en el rango ingresado y mostrarlos en
# pantalla.

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

#4. Función personalizada para simular una compra (2 puntos): 


# titulo=input("Ingrese el libro que requiere: ")
# cantidad=int(input("Ingrese la cantidad de libros que necesita: "))


# def comprar_libros(titulo, cantidad):                             
#     for libro in libros:
#         if titulo.lower() == libro["titulo"].lower():
#             if cantidad <= libro["stock"]:    
#                 libro["stock"] -= cantidad      
#                 total = libro["precio"] * cantidad  
#                 print(f"Compra realizada. Monto a cancelar: ${total}")
#                 print(f"Quedan {libro['stock']} unidades de '{libro['titulo']}'")
#                 return
#             else:
#                 print(f"No hay suficiente stock de '{titulo}'. Solo quedan {libro['stock']} unidades.")
#                 return
# comprar_libros(titulo, cantidad)

# 5. Uso de bucle while para iterar hasta que el usuario decida salir (1 punto):
     
# while True:
#     try:
#         titulo=input("Ingrese el libro que desea o salir: ")
#         if titulo.lower()=="salir":
#             print("Gracias por asistir a nuestra biblioteca, adios")
#             break
#         cantidad=int(input("Ingrese la cantidad de libros que necesita: "))
#         for libro in libros:
#             if titulo.lower() == libro["titulo"].lower():
#                 if cantidad <= libro["stock"]:    
#                     libro["stock"] -= cantidad     
#                     total = libro["precio"] * cantidad  
#                     print(f"Compra realizada. Monto a cancelar: ${total}")
#                     print(f"Quedan {libro['stock']} unidades de '{libro['titulo']}'")
#                 else:
#                     print(f"No hay suficiente stock de '{titulo}'. Solo quedan {libro['stock']} unidades.")
#     except ValueError:
#              print("Acabas de ingresar un valor invalido")

# 6. Estructura de datos, gestión de descuentos (2 puntos):

# Usa un diccionario para almacenar descuentos especiales por autor. Por ejemplo, aplica un 10% de descuento en libro de un autor especifico.
# En la función comprar_libro, certifica si el autor tiene descuento y aplícalo al monto total si corresponde.

# Omar trejos tiene un descuento de 10%
# Tolkien tiene un descuento de 20%
# William Irwin tiene un descuento de 30%
# Neil Gaiman tiene un descuento de 40%
# Dan Brown tiene un descuento de 50%

def comprar_libros(titulo, cantidad):                             
    for libro in libros:
        if titulo.lower() == libro["titulo"].lower():
            if cantidad <= libro["stock"]:
                libro["stock"] -= cantidad      
                total = libro["precio"] * cantidad  
                print(f"Compra realizada. Monto a cancelar: ${total}")
                print(f"Quedan {libro['stock']} unidades de '{libro['titulo']}'")
                return
            else:
                print(f"No hay suficiente stock de '{titulo}'. Solo quedan {libro['stock']} unidades.")
                return

while True:
    try:
        titulo=input("Ingrese el libro que desea o salir: ")
        if titulo.lower()=="salir":
            print("Gracias por asistir a nuestra biblioteca, adios")
            break
        cantidad=int(input("Ingrese la cantidad de libros que necesita: "))
        comprar_libros(titulo, cantidad)                            
    except ValueError:
             print("Acabas de ingresar un valor invalido")

