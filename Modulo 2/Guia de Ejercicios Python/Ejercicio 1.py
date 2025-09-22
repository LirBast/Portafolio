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