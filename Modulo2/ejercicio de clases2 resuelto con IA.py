op1 = float(input("Ingrese primer número: "))
op2 = float(input("Ingrese segundo número: "))

print("Menú")
print("1. Suma")
print("2. Resta")
print("3. Producto")
print("4. División")

opcion = input("Elija una opción: ")

r = None  # Inicializamos la variable

match opcion:  # match es válido desde Python 3.10
    case "1":
        r = op1 + op2
    case "2":
        r = op1 - op2
    case "3":
        r = op1 * op2
    case "4":
        try:
            r = op1 / op2
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
    case _:
        print("Opción no válida.")

# Solo mostramos el resultado si r se calculó correctamente
if r is not None:
    print(f"Resultado: {r}")