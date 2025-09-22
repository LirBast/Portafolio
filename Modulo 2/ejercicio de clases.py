op1=float(input("ingrese primer numero "))
op2=float(input("ingrese segundo numero "))

print("menu")
print("1, suma")
print("2, resta")
print("3, producto")
print("4, division")

opcion=input("elija una opcion 1,2,3,4:")


match opcion:         #match es para evaluar el valor ingresado con las opciones que le dimos
    case"1":
        r=op1+op2
    case"2":
        r=op1-op2
    case"3":
        r=op1*op2
    case"4":
        try:
            r=op1/op2
        except ZeroDivisionError:
            print("existe una indeterminacion. No se puede dividir por cero")
if op2==0 and opcion!="4":
    print(f"resultado: {r}")
else:
    print(r)

### Es la version de la profe

op1=float(input("ingrese primer número"))
op2=float(input("ingrese segundo número"))

print("Menú")
print("1. suma")
print("2. resta")
print("3. producto")
print("4. división")

opcion=input("Elija una opción")

match opcion:
  case "1":
    r=op1+op2
  case "2":
    r=op1-op2
  case "3":
    r=op1*op2
  case "4":
    try:
      r=op1/op2
    except ZeroDivisionError:
      print("Existe una indeterminación. No se puede dividir por cero")
if op2==0 and opcion=="4":
  print("No se pudo obtener un resultado")
else:
  print(f"resultado:{r}")