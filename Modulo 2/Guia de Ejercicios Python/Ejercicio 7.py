# Ejercicio 7: Suma de Números Pares (Bucle for)

# Pide al usuario un número entero positivo y calcula la suma de todos los números pares desde 1
# hasta ese número (inclusive).

numero=int(input("Ingrese un numero entero positivo: "))

suma=0

if numero%2==0:
    for i in range (1,numero+1):
        if i%2==0:
            suma +=i                      
    print(f"La suma de los numeros pares hasta {numero} es {suma}")      
else:
    print("Su numero no es par, ingrese otro")



