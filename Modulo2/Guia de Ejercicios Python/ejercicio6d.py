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
tiene_mayus=any(letra.isupper() for letra in passw_limpia)            ##el any() se usa para un conjunto de valores, que si al menos uno entre el True y False si todos son falsos
tiene_minus=any(letra.islower() for letra in passw_limpia)
tiene_digit=any(letra.isdigit() for letra in passw_limpia)


if passw_cantidad>=8:
    if tiene_mayus:
        if tiene_minus:
            if tiene_digit:
                 print("Su contraseña cumple con todos los requisitos por lo que se considera fuerte")
            else:
                 print("Su contraseña no cumple con los requisitos porque le falta el caracter numerico")
        elif tiene_digit:
            print("Su contraseña no cumple con los requisitos porque el caracter en minuscula")
        else:
            print("Su contraseña no cumple con los requisitos porque le falta el caracter en minusculas y numerico")
    elif tiene_minus:
        if tiene_digit:
            print("Su contraseña no cumple con los requisitos porque le falta el caracter en mayuscula")
        else:
            print("Su contraseña no cumple con los requisitos porque le falta el caracter en mayuscula y en numeral")
    elif tiene_digit:
            if tiene_minus:
                 print("Su contraseña no cumple con el requisito porque le falta el caracter en mayuscula")
            else:
                 print("Su contraseña no cumple con los requisitos porque le faltan los caracteres en mayuscula y en numeral")
else:
     print("Ingrese una contraseña con al menos 8 caracteres")