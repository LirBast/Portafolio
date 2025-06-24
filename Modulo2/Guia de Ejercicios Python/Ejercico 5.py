# Ejercicio 5: Menú de Opciones de Bebida

# Crea un programa que muestre un menú de bebidas (Café, Té, Refresco) y pida al usuario que
# elija una. Luego, debe mostrar el precio de la bebida seleccionada o un mensaje de error si la
# opción no es válida.


print(f" [Café] " " [Té]" " [Refresco]")
opcion=str(input("Elija una de las opciones: "))   #### el str al inicio esta demas porque el resultado por defecto de input es un texto

opcion_mayus=opcion.strip().upper()        ###se me recomienda usar la funcion .strip() para eliminar los espacios al princio o al final de los caracteres opcion_mayus = opcion.strip().upper()

if opcion_mayus=="CAFE":
    print(f"acaba de elegir la opcion Café, tiene un precio de 2000")
elif opcion_mayus=="TE":
    print(f"acaba de elegir la opcion Té, tiene un precio de 1000")
elif opcion_mayus=="REFRESCO":
    print(f"acaba de elegir la opcion Refresco, tiene un precio de 1000")
else:
    print("Opcion no valida. Por favor, elija una opción de la lista.")