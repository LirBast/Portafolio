### Grafico de Lineas entre cantidad de autos y dias

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 4\Clases 6\datos_trafico.csv")
print(df.head())

plt.figure(figsize=(8,5))
plt.plot(df['Día'], df['Vehículos'],color='blue',label='Vehículos por día',marker='o')
plt.legend()
plt.grid(True)
plt.title('Grafico de lineas')
plt.xlabel('Dias')
plt.ylabel('Cantidad de autos')
plt.savefig('grafico_acidentes.png')
plt.show()


### Histograma para distribucion de velocidades

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 4\Clases 6\datos_trafico.csv")
print(df.head())

print('---------------------------')
max=df['Velocidad_Promedio'].max()
min=df['Velocidad_Promedio'].min()
print(f'El valor maxino de la velocidad promedio es: {max}')
print(f'El valor minimo de la velocidad promedio es: {min}')
print('---------------------------')
rango=max-min
print(f'El valor del rango de la velocidad promedio es: {rango}')
print('---------------------------')
numero_de_intervalos=8   ### Se cambia a mano el numero de intervalos
tama_del_intervalo=rango/numero_de_intervalos
print(f'El tamaño del intervalo es: {tama_del_intervalo}')

bins = [min + i * tama_del_intervalo for i in range(numero_de_intervalos + 1)]

print("Intervalos:")
for i in range(len(bins) - 1):
    print(f"{bins[i]:.2f} - {bins[i+1]:.2f}")

plt.figure(figsize=(8,5))
plt.hist(df['Velocidad_Promedio'],bins=numero_de_intervalos,color='grey',edgecolor='black',label='frecuencia agrupadas')
plt.legend()
plt.grid(True)
plt.title('Distribucion De Velocidades')
plt.xlabel('Velocidades')
plt.ylabel('Frecuencia')
plt.savefig('Distribucion De Velocidades.png')
plt.show()

### Grafico de Dispersion

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 4\Clases 6\datos_trafico.csv")
print(df.head())

plt.scatter(df['Vehículos'],df['Accidentes'],color='red',label='Relacion de cantidad de vehiculos por accidente',marker='.')
plt.legend()
plt.grid(True)
plt.title('Grafico de Dispersion')
plt.xlabel('Vehiculos')
plt.ylabel('Accidentes')
plt.savefig('Grafico de Dispersion')
plt.show()