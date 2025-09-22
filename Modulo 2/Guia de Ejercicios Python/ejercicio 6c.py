# Ejercicio 6: Validador de Contraseña Simple

# Pide al usuario que ingrese una contraseña. La contraseña se considera "fuerte" si cumple con las
# siguientes condiciones:

# ● Tiene al menos 8 caracteres de longitud.
# ● Contiene al menos una letra mayúscula.
# ● Contiene al menos una letra minúscula.
# ● Contiene al menos un dígito.


passw=str(input("ingrese su contraseña: "))

passw_limpia=passw.replace(" ", "")                                 #la funcion .strip() elimina los espacio al inicio y al final de la palabra, pero no los que estan entre medios

passw_cantidad=len(passw_limpia)                                    # En este caso hay que usar la funcion replace(" ", "") para eliminar todos los espacios, el primer espacio es para buscar y el segundo es para reemplazar
tiene_mayus=any(letra.isupper() for letra in passw_limpia)
tiene_minus=any(letra.islower() for letra in passw_limpia)
tiene_digit=any(letra.isdigit() for letra in passw_limpia)


if passw_cantidad>=8:
    if tiene_mayus:
        if tiene_digit:
            if tiene_minus:
                print("Su contraseña tiene mas de 8 caracteres, tiene mayusculas, tiene minusculas y tiene digitos")
                print("Se considera una contraseña fuerte")
            else:
                print("Su contraseña Su contraseña tiene mas de 8 caracteres, tiene mayusculas,tiene digitos pero no tiene minusculas")
        else:
            print("Su contraseña tiene mas de 8 caracteres, tiene mayusculas pero no tiene digitos")
    else:
        print("Su contraseña tiene 8 caracteres pero no mayusculas")
else:
    print("Su contraseña tiene menos de 8 caracteres")