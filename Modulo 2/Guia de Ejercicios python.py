try:
    numero=int(input("ingrese un numero: "))

    if numero >0:
        print("el valor:",numero,"es positivo")
    elif numero <0:
        print(f"el numero: {numero} es negativo")
    else:
        print(f"el nuermo es 0")
except ValueError:
    print("Entrada invalida, por favor ingresa un numero entero")

#se puede escribir los caracteres de dos formas, puede hacerse con una coma o se puede hacer con
# una f y con corchetes, como en el elif 
#si se selecciona cierta parte del codigo y apretamos tabular se puede indentar todo al mismo tiempo
#Try es para arreglar los errores que se crean al digitar datos para arreglar al momento de tipiar, por ejemplo este ejercicio
# pide un numero entero y aparece un valuError al momento de ingresas una letra o algo como caracter




n=-20
mensaje="es positivo" if n>0 else "es cero o negativo"
print(mensaje)


#tambien se puede escribir de esta forma para ahorrar lineas de codigo 