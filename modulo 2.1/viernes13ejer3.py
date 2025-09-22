
def main():
    op1 = float(input("Ingrese el primer operando: "))

    while True:
        op2 = float(input("Ingrese el siguiente operando o escriba salir: "))
        if op1.lower()=="salir":
            break
        else:
            op2=int(op2)
        
        suma1=suma1+suma(op1,op2)
        op1=suma1

    resultado = suma(op1, op2)
    resultado2 = suma(op1, op2)

    print("Resultado 1:", resultado)
    print("Resultado 2:", resultado2)


def suma(a, b):
    return a + b


if __name__ == "__main__":
    main()
