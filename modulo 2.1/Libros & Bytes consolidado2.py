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

print(libros)


# 2. Control de flujo (1 punto):

# Implementa una función llamada mostrar_libros_disponibles() que recorra la lista de
# libros y muestre en pantalla los libros que tienen más de una unidad en stock usando
# una sentencia for y una condición if.

def mostrar_libros_disponibles():
    for libro in libros:
        if libro.get("stock")>=1:
            print(libro)

mostrar_libros_disponibles()

# 3. Condiciones y operadores (1 punto):

# Solicita al usuario que ingrese un rango de precios (mínimo y máximo) y utiliza una
# sentencia if elif else para filtrar los libros en el rango ingresado y mostrarlos en
# pantalla.

minimo=float(input("Ingrese el precio minimo par filtrar: "))
maximo=float(input("Ingrese un precio maximo para filtrar: "))

while True:
    if minimo>=maximo:
        print("Minimo no puede ser mayor a maximo")
        break
    else:
        for libro in libros:
            if libro.get("precio")>=minimo and libro.get("precio")<=maximo:
                print(libro)
        break


#4. Función personalizada para simular una compra (2 puntos):


titulo=input("Ingrese el libro que requiere: ")
cantidad=int(input("Ingrese la cantidad de libros que necesita: "))



for libro in libros:
    if titulo.lower()==libro["titulo"].lower():
      if cantidad <=libro["stock"]:
                libro["stock"]-=cantidad
                total =libro["precio"]*cantidad
                print(f'Compra realizada. Monto a cancelar {total}')
                print(f"Quedan {libro['stock']} unidades de '{libro['titulo']}'")
                break
      else:
          print(f"No quedan unidades del libro '{titulo}'. Solo quedan {libro['stock']} unidades.")
          break
      
# 5. Uso de bucle while para iterar hasta que el usuario decida salir (1 punto):

libros=[{"titulo":"Introduccion a Python","autor":"Omar trejos","precio":18530,"stock":28},
        {"titulo":"El señor de los anillos","autor":"Tolkien","precio":16070,"stock":11},
        {"titulo":"Los Simpson y la filosofía","autor":"William Irwin","precio":24370,"stock":6},
        {"titulo":"Sandman","autor":"Neil Gaiman","precio":37820,"stock":72},
        {"titulo":"Infierno","autor":"Dan Brown","precio":16440,"stock":10}]

while True:
    try:
        titulo=input('Ingrese el libro que desea o salir: ')
        if titulo.lower()=="salir":
            print("Gracias por asistir a nuestra biblioteca, adios")
            break
        cantidad=int(input('Ingrese la cantidad de libros que necesita: '))
        for libro in libros:
            if titulo.lower()==libro["titulo"].lower():
                if cantidad<=libro["stock"]:
                    libro["stock"]-=cantidad
                    total =libro["precio"]*cantidad
                    print(f"Compra realizada. Monto a cancelar {total}")
                    print(f"Quedan {libro['stock']} unidades de '{libro['titulo']}'")
                else:
                    print(f"No quedan unidades del libro '{titulo}'. Solo quedan {libro['stock']} unidades.")
    except ValueError:
             print("valor invalido")


# 6. Estructura de datos, gestión de descuentos (2 puntos):

libros=[{'titulo':'Introduccion a Python','autor':'Omar trejos','precio':18530,'stock':28},
        {'titulo':'El señor de los anillos','autor':'Tolkien','precio':16070,'stock':11},
        {'titulo':'Los Simpson y la filosofía','autor':'William Irwin','precio':24370,'stock':6},
        {'titulo':'Sandman','autor':'Neil Gaiman','precio':37820,'stock':72},
        {'titulo':'Infierno','autor':'Dan Brown','precio':16440,'stock':10}]

descuento_libros=[{'titulo':'Introduccion a Python','autor':'Omar trejos','descuento':0.1},
                  {'titulo':'El señor de los anillos','autor':'Tolkien','descuento':0.2},
                  {'titulo':'Los Simpson y la filosofía','autor':'William Irwin','descuento':0.3},
                  {'titulo':'Sandman','autor':'Neil Gaiman','descuento':0.4},
                  {'titulo':'Infierno','autor':'Dan Brown','descuento':0.5}]

titulo=input('Ingrese el libro que requiere: ')
cantidad=int(input('Ingrese la cantidad de libros que necesita: '))

def comprar_libros(titulo,cantidad):
    for libro in libros:
        if titulo.lower()==libro['titulo'].lower():
            if cantidad<=libro['stock']:
                descuento=0
                for desc in descuento_libros:
                    if titulo.lower()==desc['titulo'].lower():
                        descuento=desc['descuento']
                        break

                precio_con_descuento=libro['precio']*(1 - descuento)
                precio_sin_descuento =libro['precio']*cantidad
                total = precio_con_descuento*cantidad
                monto_del_descuento= precio_sin_descuento - total
                libro['stock']-=cantidad

                print(f'Compra realizada con éxito.')
                print(f'Quedan {libro["stock"]} unidades de {libro["titulo"]}')
                print(f'Monto a cancelar (sin descuento): {precio_sin_descuento}')
                print(f'El monto del descuento es: {monto_del_descuento}')
                print(f'Monto a cancelar (con descuento): {total}')
                return
            else:
                print(f'No hay suficientes libros de{titulo}. Quedan en el stock {libro["stock"]}')
                return
    print(f'El no se encuentra el libro {titulo}')

comprar_libros(titulo, cantidad)


#   7 Simulación de una factura (2 punto):

libros=[{'titulo':'Introduccion a Python','autor':'Omar trejos','precio':18530,'stock':28},
        {'titulo':'El señor de los anillos','autor':'Tolkien','precio':16070,'stock':11},
        {'titulo':'Los Simpson y la filosofía','autor':'William Irwin','precio':24370,'stock':6},
        {'titulo':'Sandman','autor':'Neil Gaiman','precio':37820,'stock':72},
        {'titulo':'Infierno','autor':'Dan Brown','precio':16440,'stock':10}]

descuento_libros=[{'titulo':'Introduccion a Python','autor':'Omar trejos','descuento':0.1},
                  {'titulo':'El señor de los anillos','autor':'Tolkien','descuento':0.2},
                  {'titulo':'Los Simpson y la filosofía','autor':'William Irwin','descuento':0.3},
                  {'titulo':'Sandman','autor':'Neil Gaiman','descuento':0.4},
                  {'titulo':'Infierno','autor':'Dan Brown','descuento':0.5}]

print('-----Sistema de compras-----')
print('1.- Motrar libros disponibles')
print('2.- Filtrar libros por rango de precios')
print('3.- Comprar Libros')
print('4.- Finalizar la compra y mostrar la factura')
opcion=int(input('Ingrese una de las opciones anteriores'))

if opcion == 1:
  print(libros)
if opcion ==2:
  print('Filtrar libros por rango de precios')
  minimo=input('Ingrese el valor minimo del rango')
  maximo=input('Ingrese el valor maximo del rengo')
  
  minimo=int(minimo)
  maximo=int(maximo)
  
  libros_filtrados = []

  for libro in libros:
    if minimo<=libro['precio'] and maximo>=libro['precio']:
      libros_filtrados.append(libro)
  if libros_filtrados:
    print(f'Libros encontrados en los rangos minimo {minimo} y en el maximo {maximo}')
    for libro in libros_filtrados:
      print(f"{libro['titulo']} con el precio de  {libro['precio']}")
  else:
        print('No se encontraron libros en ese rango de precios.')
if opcion ==3:
  titulo = input('Ingrese el libro que requiere: ')
  cantidad = int(input('Ingrese la cantidad de libros que necesita: '))

  def comprar_libros(titulo,cantidad):
      for libro in libros:
          if titulo.lower() ==libro['titulo'].lower():
              if cantidad <=libro['stock']:
                  descuento =0
                  for desc in descuento_libros:
                      if titulo.lower() == desc['titulo'].lower():
                          descuento = desc['descuento']
                          break

                  precio_con_descuento = libro['precio'] * (1 - descuento)
                  precio_sin_descuento = libro['precio'] * cantidad
                  total = precio_con_descuento * cantidad
                  monto_del_descuento = precio_sin_descuento - total
                  libro['stock'] -= cantidad

                  print(f'\nCompra realizada con éxito.')
                  print(f'Quedan {libro["stock"]} unidades de {libro["titulo"]}')
                  print(f'Monto a cancelar (sin descuento): {precio_sin_descuento}')
                  print(f'El monto del descuento es: {monto_del_descuento}')
                  print(f'Monto a cancelar (con descuento): {total}')
                  return
              else:
                  print(f'No hay suficientes libros de{titulo}. Quedan en el stock {libro["stock"]}')
                  return
      print(f'No se encuentra el libro {titulo}')

  comprar_libros(titulo,cantidad)