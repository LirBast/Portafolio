mi_diccionario={'nombre':'Maria','apellido':'Perez','edad':25,'ciudad':'valparaiso'}
print(mi_diccionario)
mi_diccionario['rut']='116109-k'
print(mi_diccionario)
print(mi_diccionario['edad'])
pais=mi_diccionario.get('pais','Desconocido')
print(pais)

usuarios={'usuario1':{'nombre':'Maria','apellido':'Perez','edad':25,'ciudad':'valparaiso'},
         'usuario2':{'nombre':'Luis','apellido':'Mendez','edad':35,'ciudad':'Santiago'}}

print(usuarios['usuario2']) ###es para saber solo los datos de el usuario 2}


producto={'nombre':'laptop','precio':1000000,'stock':10}

print(producto)
producto['marca']='HP'
print(producto)
print(producto['precio'])


libro = {'libro1': {'titulo': '100 años de soledad','autor': 'Gabriel García Márquez','detalles': {'año': '1982', 'idioma': 'español'}},'libro2': {'titulo': 'Inés del alma mía','autor': 'Isabel Allende','detalles': {'año': '2005', 'idioma': 'español'}}}

print(libro)