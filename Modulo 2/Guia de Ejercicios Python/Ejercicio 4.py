# Ejercicio 4: Clasificador de Estaciones del Año
# Pide al usuario que ingrese un número de mes (del 1 al 12) y determina a qué estación del año pertenece. 
# (Considera un esquema simple para las estaciones).
try:
    mes=int(input("ingrese un numero del 1 al 12 para identificar el mes: "))

    if mes==1:
        print("Enero")
    elif mes==2:
        print("Febrero")
    elif mes==3:
        print("Marzo")
    elif mes==4:
        print("Abril")
    elif mes==5:
        print("Mayo")
    elif mes==6:
        print("Junio")
    elif mes==7:
        print("Julio")
    elif mes==8:
        print("Agosto")
    elif mes==9:
        print("Septiembre")
    elif mes==10:
        print("Octubre")
    elif mes==11:
        print("Noviembre")
    elif mes==12:
        print("Diciembre")
    else:
        print("Ingrese un valor entero entre 1 y 12")
except ValueError:
    print("Valor erroneo, por favor ingresar un valor entre 1 y 12")




# Esta es la version de la IA

# try:
#     mes = int(input("Ingrese un número del 1 al 12 para identificar el mes: "))

#     meses = {
#         1: "Enero", 2: "Febrero", 3: "Marzo",
#         4: "Abril", 5: "Mayo", 6: "Junio",
#         7: "Julio", 8: "Agosto", 9: "Septiembre",
#         10: "Octubre", 11: "Noviembre", 12: "Diciembre"
#     }

#     print(meses.get(mes, "⚠️ Ingrese un número válido entre 1 y 12."))

# except ValueError:
#     print("⚠️ Ingreso inválido. Por favor ingrese un número entero.")
