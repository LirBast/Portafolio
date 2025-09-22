#lista=[1,2,1,True,5.0,True,True]
mi_Set={1,2,3}
print(mi_Set)

conjunto_duplicados={1,2,2,3,4,4,5}   ###en los conjuntos no pueden haber elementos duplicados, e ilimina los elementos que se repiten
print(conjunto_duplicados)


lista_numeros=[1,2,2,3,4,4]
conjunto_desde_lista=set(lista_numeros)     ##Un set (o conjunto) es una colección de elementos únicos, es decir, no permite duplicados.
print(conjunto_desde_lista)                 ###El set es ideal para realizar comparaciones y operaciones matemáticas entre conjuntos porque evita duplicados y permite búsquedas eficientes.


## union de conjuntos
conjunto_a={1,2,3}
conjunto_b={3,4,5}

union=conjunto_a | conjunto_b        ###la barra une los conjuntos
print(union)

# Intersepcion de conjuntos
interseccion=conjunto_a & conjunto_b
print(interseccion)