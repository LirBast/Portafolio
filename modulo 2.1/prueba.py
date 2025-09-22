mi_lista=[1,2,3,4,5]
print(mi_lista)
lista_vacia=[]
lista_combinada=[1,"hola",3.14,True, False,5,"adios"]

lista_vacia.append("python")
print(lista_vacia)
mi_lista.append(6)   #esto hace que agrege otro dato al final de la lista original 
print(mi_lista)

mi_lista.insert(2,10)
print(mi_lista)

print(mi_lista[6])      ### Estas 2 lineas hacen referencia al mismo dato de la lista, ya que
print(mi_lista[-1])     ### ambas se pueden leer de adelante ahi atras o adelante o atras


 
sub_lista=lista_combinada[2:4]    ### los intervalos son abiertos
print(sub_lista)

sub_lista=lista_combinada[:4] 
print(sub_lista)

sub_lista=lista_combinada[2:] 
print(sub_lista)

cadena="Bienvenido al curso de ciencia de datos"
lista_cadena=cadena.split()
print(lista_cadena)

palabras=["Python", "es","un","lenguaje","interpretado"]
frase="".join(palabras)
print(frase)   ### el resultado de esto ya no es una lista


matriz=[[1,2],[3,4],[True,"a"]]

print(matriz)
print(matriz[1][0])    ### el primer valor hace referencia a las filas horizonantales
                        ### y el segundo numero hace referencia a las columnas verticales


### nueva_lista=[expresion for item in interable if condicion dada]
dobles=[]
for numero in mi_lista:
    dobles.append(numero*2)
print(dobles)

dobles2=[numero*2 for numero in mi_lista if numero<10]   

print(dobles2)
