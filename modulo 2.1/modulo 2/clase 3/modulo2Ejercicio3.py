
### Punto 1

# nombre=input('Ingrese el nombre del alumno: ')
# nota=int(input('Ingrese la nota del alumno de 0 a 60: '))

# if 60<nota:
#     print('La nota del alumno es mayor a 60 por lo que aprueba el curso')
# else:
#     print('La nota del alumno es menor a 60 por lo que reprueba el curso')

### Punto 2

# while True:
#     try:
#         nombre=input('Ingrese el nombre del Alumno o salir para terminar el proceso: ')
#         if nombre.lower()=='salir':
#             print('Se termino el proceso')
#             break
#         nota=int(input('Ingrese la nota del alumno: '))
#         if 60<nota:
#             print('La nota del alumno es mayor a 60 por lo que aprueba el curso')
#         else:
#             print('La nota del alumno es menor a 60 por lo que reprueba el curso')
#     except ValueError:
#         print("valor invalido")


### Punto 3

# while True:
#     try:
#         nombre=input('Ingrese el nombre del Alumno o salir para terminar el proceso: ')
#         if nombre.lower()=='salir':
#             print('Se termino el proceso')
#             break
#         nota1=int(input('Ingrese la nota de matematicas del alumno: '))
#         nota2=int(input('Ingrese la nota de ciencias del alumno: '))
#         nota3=int(input('Ingrese la nota de ingles del alumno: '))
#         promedio=(nota1+nota2+nota3)/3
#         print(f'El promedio del alumno es {promedio}')
#     except ValueError:
#         print("valor invalido")

### Punto 4

# while True:
#     try:
#         nombre=input('Ingrese el nombre del Alumno o salir para terminar el proceso: ')
#         if nombre.lower()=='salir':
#             print('Se termino el proceso')
#             break
#         nota1=int(input('Ingrese la nota de matematicas del alumno: '))
#         nota2=int(input('Ingrese la nota de ciencias del alumno: '))
#         nota3=int(input('Ingrese la nota de ingles del alumno: '))
#         promedio=(nota1+nota2+nota3)/3
#         if promedio>=90:
#             print(f'El alumno {nombre} obtuvo un promedio de {promedio:.2f}, y al estar por encima de 90 o mas se considera Excelente')
#         elif 75<=promedio<90:  ### aca puede ser promedio<=89 o promedio<90 dado que el intervalo es abierto
#             print(f'El alumno {nombre} obtuvo un promedio de {promedio:.2f}, y al estar entre 75 a 89 se considera Bueno')
#         else:
#             print(f'El alumno {nombre} obtuvo un promedio de {promedio:.2f}, y al por debajo de 75 considera que Necesita Mejorar')
            
#     except ValueError:
#         print("valor invalido")


### Punto 5
# alumnos=[]
# while True:
#     try:
#         nombre=input('Ingrese el nombre del Alumno o salir para terminar el proceso: ')
#         if nombre.lower()=='salir':
#             print('Se termino el proceso')
#             break
#         nota1=int(input('Ingrese la nota de matematicas del alumno: '))
#         nota2=int(input('Ingrese la nota de ciencias del alumno: '))
#         nota3=int(input('Ingrese la nota de ingles del alumno: '))
#         promedio=(nota1+nota2+nota3)/3
#         if promedio>=90:
#             print(f'El alumno {nombre} obtuvo un promedio de {promedio:.2f}, y al estar por encima de 90 o mas se considera Excelente')
#         elif 75<=promedio<90:  ### aca puede ser promedio<=89 o promedio<90 dado que el intervalo es abierto
#             print(f'El alumno {nombre} obtuvo un promedio de {promedio:.2f}, y al estar entre 75 a 89 se considera Bueno')
#         else:
#             print(f'El alumno {nombre} obtuvo un promedio de {promedio:.2f}, y al por debajo de 75 considera que Necesita Mejorar')
#         alumnos.append({'nombre':nombre,'promedio':promedio})

#     except ValueError:
#         print("valor invalido")
# print("----- Resumen de Alumnos -----")
# print(alumnos)


### punto 6
alumnos=[]
while True:
    try:
        nombre=input('Ingrese el nombre del Alumno o salir para terminar el proceso: ')
        if nombre.lower()=='salir':
            print('Se termino el proceso')
            break
        nota1=int(input('Ingrese la nota de matematicas del alumno: '))
        nota2=int(input('Ingrese la nota de ciencias del alumno: '))
        nota3=int(input('Ingrese la nota de ingles del alumno: '))
        promedio=(nota1+nota2+nota3)/3
        if promedio>=90:
            comentario='Excelente'
        elif 75<=promedio<90: 
            comentario='Bueno'
        else:
            comentario='Necesita Mejorar'
        if promedio>=100:
            comentario+=' - Obtuvo un puntuacion igual o superior a 100'
        alumnos.append({'nombre':nombre,'promedio':promedio,'comentario':comentario})
    except ValueError:
        print("valor invalido")
print("----- Resumen de Alumnos -----")
# print(alumnos)
for alumno in alumnos:
    print(f"{alumno['nombre']} - Promedio: {alumno['promedio']:.2f} - {alumno['comentario']}")