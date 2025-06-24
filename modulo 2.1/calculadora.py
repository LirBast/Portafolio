import libreria.matematicas as math

print("Operaciones")
print("1- suma")
print("2- resta")
print("3- multiplicacion")
print("4- division")

opcion=input("Seleccione una opcion 1,2,3 o 4: ")
op1=float(input("Ingrese un numero: "))
op2=float(input("Ingrese un numero: "))

match opcion:
    case "1":
        r = math.suma(op1,op2)
    case "2":
        r = math.resta(op1,op2)
    case "3":
        r = math.multiplicacion(op1,op2)
    case "4":
        r = math.division(op1,op2)

print(f"El resultado de la operacion {r:.2f}")