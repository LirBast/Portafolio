# Ejercicio 2: Calculadora de Descuento
# Pide al usuario el precio de un producto y la cantidad. Aplica un descuento basado en el monto total de la compra:
# ● Si el total es $100 o más, aplica un 10% de descuento.
# ● Si el total es entre $50 y $99.99, aplica un 5% de descuento.
# ● Si el total es menor a $50, no hay descuento.
try:
    precio_producto=float(input("Ingrese el valor del producto: "))
    cantidad=int(input("ingrese la cantidad de productos: "))     

    Total=precio_producto*cantidad

    if Total >= 100:
        total1=Total-Total*(10/100)
        print(f"su venta total es de {Total} pero al ser mayor o igual a 100 pesos tiene un descuento de 10%, por lo el valor a pagar es de {total1}")
    elif Total>=50:
        total2=Total-Total*(5/100)
        print(f"su venta total es de {Total} pero al ser mayor a 50 y menor de 99,99 pesos tiene un descuento de 5%, por lo el valor a pagar es de {total2}")
    else:
        print(f"el valor de su compra es {Total} pero al ser menor de 50 pesos no tiene descuento")
except:
    print("El valor ingreso no corresponde, probar otra vez")