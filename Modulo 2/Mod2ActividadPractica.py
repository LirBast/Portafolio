
#Crear tres variables en Python:

Precio_producto=1200   
Cantidad=3
Descuento=10

#Calcular el precio total sin descuento

Total_sin_descuento=Precio_producto*Cantidad

#Calcular el monto de descuento

monto_descuento=Precio_producto*(Descuento/100)*Cantidad

#Calcular el precio total con descuento

total_con_descuento=Total_sin_descuento-monto_descuento
                                                                             
#Imprime los resultados de cada cálculo con mensajes claros

print("El precio total de los productos sin descuento es:",Total_sin_descuento,"pesos")
print("El monto total del descuento:",monto_descuento,"pesos")
print("El total con descuento es:",total_con_descuento,"pesos")