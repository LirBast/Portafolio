## la lista empieza con el valor cero no con el uno
# La sentencia for se utiliza para iterar sobre una secuencia (como una lista, una tupla o un string) o sobre un rango de números.
### Ejemplo de uso de la sentencia for
nombres= ["Pedro", "María", "Ana"]
for nombre in nombres:
    print(f"hola, {nombre}")
    
# En este caso, la variable i toma los valores del 0 al 9, uno por uno.

# Ejemplo de uso de la sentencia for con un rango de números
for i in range(1,11,2):
    if i==1:
        print(0)
    print(i)