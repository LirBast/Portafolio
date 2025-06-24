def saludar(nombre):
    """
    Imprime un saludo personalizado.
    """
    print(f"Hola, {nombre}")

if __name__ == "__main__":
    nombre = input("¿Cómo te llamas? ")
    saludar(nombre)