def suma(a, b):
    return a + b

def main():
    op1 = float(input("Ingrese el primer operando: "))
    op2 = float(input("Ingrese el segundo operando: "))

    resultado = suma(op1, op2)
    resultado2 = suma(op1, op2)

    print("Resultado 1:", resultado)
    print("Resultado 2:", resultado2)

if __name__ == "__main__":
    main()
