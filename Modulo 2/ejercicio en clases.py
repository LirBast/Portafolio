#01
colores=["rojo","verde", "azul"]
print(colores)
#02
colores.append("amarillo")
print(colores)
#03
colores.insert(1,"morado")
print(colores)
#04
print(colores[1])
#05
sublista=colores[2:4]
print(sublista)
#06
lista="Python es divertido"
print(lista.split())
#07
numeros=[2,4,5,6,9,10]
print(numeros)
#08
cuadrado=[]      
for numero in numeros:
    if numero%2!=0:    ##esto muestra los valores impares
        cuadrado.append(numero*numero)
print(cuadrado)

cuadrado2=[numero2*numero2 for numero2 in numeros]
print(cuadrado2)

#09
cuadrado3=[numero3*numero3 for numero3 in numeros if numero3%2==0]
print(cuadrado3)