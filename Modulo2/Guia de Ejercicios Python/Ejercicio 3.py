# Ejercicio 3: Selector de Menú Interactivo

# Presenta al usuario un menú de opciones (por ejemplo, "Ver perfil", "Editar configuración","Cerrar sesión"). 
# Pide al usuario que elija una opción y muestra un mensaje diferente para cada elección.

print(f" [Ver Perfil] " " [Editar configuracion]" " [Cerrar Sesion]")
opcion=str(input("Elija una de las opciones: "))   #### el str al inicio esta demas porque el resultado por defecto de input es un texto

opcion_mayus=opcion.upper()        ###se me recomienda usar la funcion .strip() para eliminar los espacios antes de los caracteres opcion_mayus = opcion.strip().upper()

if opcion_mayus=="VER PERFIL":
    print(f"acaba de elegir la opcion {opcion}, quiere modificar el usuario?")
elif opcion_mayus=="EDITAR CONFIGURACION":
    print(f"acaba de elegir la opcion {opcion}, quiere modificar los terminos de su cuenta?")
elif opcion_mayus=="CERRAR SESION":
    print(f"acaba de elegir la opcion {opcion}, al cerrar la sesion no se guardan los cambios, desea continuar?")
else:
    print("Opcion no valida. Por favor, elija una opción de las lista.")    #### me falto el else para dar el error cuando el usuario ingresa un valor que no esta dentro 
