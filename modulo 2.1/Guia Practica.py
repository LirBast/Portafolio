while True:                 #se puede obligar a que entre al bucle altiro con la funcion true
    nombre=input("Ingrese el nombre del alumno o salir para finalizar el programa: ")
    if nombre.lower()=="salir":
        break                           #y se puede terminar el bluque si se termina con el break
    calificacion=float(input("Ingrese la calificacion: ")) 
    if calificacion>=60:
        print(f"El alumno {nombre} obtuvo una nota de {calificacion}, lo que implica que aprobo")
    else:
        print(f"El alumno {nombre} obtuvo una nota de {calificacion}, lo que implica que no aprobo")
    materias=["matematicas","ciencias","ingles"]
    notas=[]
    for materia in materias:
        while True:
            try:                              #este try es en el caso de que introduzca una letra o un valor erroneo
                nota=float(input(f"Ingrese la calificacion de {materia } 0-100: "))
                if 0<=nota<=100:
                    notas.append(nota)
                    break
                else:
                    print("La calificacion debe estar entre 0 y 100")
            except ValueError:
                print("Ingresaste un valor invalido")
    promedio=sum(notas)/len(notas)
    print(f"el promedio de las notas ingresadas es: {promedio}")