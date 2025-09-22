# promedio 150 gramos

# distribucion esta sesgada a la derecha

# desvicion estandar de 

# muestra subconjunto representativo de la poblacion

# pesos de las manzanas

# [148g, 162g, 155g, 139g, 170g, 150g, 145g, 160g, 135g, 
#  158g, 142g, 165g, 153g, 140g, 168g, 147g, 159g, 130g, 
#  163g, 151g, 144g, 166g, 137g, 154g, 149g, 161g, 133g, 
#  156g, 146g, 164g]


import matplotlib.pyplot as plt

# Datos originales
datos = [148, 162, 155, 139, 170, 150, 145, 160, 135, 
         158, 142, 165, 153, 140, 168, 147, 159, 130, 
         163, 151, 144, 166, 137, 154, 149, 161, 133, 
         156, 146, 164]

# Promedios de las muestras
promedios = [150.4, 151.9, 150.6, 153.0, 150.0, 150.9, 150.1, 150.3, 149.7, 150.1, 150.1, 147.7, 149.1]

# Promedio total de los promedios
promedio_total = sum(promedios) / len(promedios)

# Promedio poblacional
promedio_poblacion = sum(datos) / len(datos)

# Índices para las muestras
indices = list(range(1, len(promedios) + 1))

plt.figure(figsize=(11,6))
# Barras para promedios individuales
plt.bar(indices, promedios, color='skyblue', label='Promedios muestras')

# Líneas horizontales para promedio total y promedio poblacional
plt.axhline(promedio_total, color='orange', linestyle='--', linewidth=2, label=f'Promedio total ({promedio_total:.2f})')
plt.axhline(promedio_poblacion, color='green', linestyle='-', linewidth=2, label=f'Promedio poblacional ({promedio_poblacion:.2f})')

# Etiquetas y título
plt.xticks(indices)
plt.ylabel('Promedio (g)')
plt.xlabel('Muestra')
plt.title('Promedios de muestras con promedio total y poblacional superpuestos')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
