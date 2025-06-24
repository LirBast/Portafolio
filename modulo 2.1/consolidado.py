# 1. Definir variables básicas y tipos de datos (1 punto): 
libros=[{"titulo":"Finanzas","autor":"Pedro","precio":50.00,"stock":1},
        {"titulo":"Dune","autor":"Frank Herbert","precio":11.99,"stock":50},
        {"titulo":"La casa de los espiritus","autor":"Isabel Allende","precio":20.00,"stock":30},
        {"titulo":"La bilbia","autor":"Varios","precio":200.00,"stock":25},
        {"titulo":"100 años de soledad","autor":"Gabriel Garcia Marquez","precio":25.00,"stock":10}]

# print(libros)

# 2. Control de flujo (1 punto):
"""

def mostrar_libros_disponibles():
    for libro in libros:
        if libro.get("stock")>=1:
            print(libro)

mostrar_libros_disponibles()

"""
# 3. Condiciones y operadores (1 punto): 

minimo=float(input("Ingrese el precio minimo par filtrar: "))
maximo=float(input("Ingrese un precio maximo para filtrar: "))

for libro in libros:
    if libro.get("precio")>=minimo and libro.get("precio")<=maximo:
        print(libro)


#4. Función personalizada para simular una compra (2 puntos): 
