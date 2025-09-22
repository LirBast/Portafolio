## 1.- Importa la librería Pandas y crea un DataFrame
import pandas as pd

data={'Jugador':['Lionel Messi','Cristiano Ronaldo','Kevin de Bruyne','Kylian Mbappé','Luka Modric'],
      'Posicion':['Delantero','Delantero','Mediocampista','Delantero','Mediocampista'],
      'Edad':[35,38,31,24,37],
      'Goles':[20,18,8,25,3],
      'Asistencias':[10,5,15,12,8]}

df=pd.DataFrame(data)

print(df)
print('\n')
# 2. Selecciona una columna y muestra los nombres de todos los jugadores

print('Nombre de los jugadores:')
for jugador in df['Jugador']:
    print(jugador)
print('\n')
# 3. Filtra jugadores con más de 10 goles y muestra solo su nombre y cantidad de goles

goleadores=df[df['Goles']>10]
print(goleadores[['Jugador','Goles']])
print('\n')
# 4.- Agrega una nueva columna al DataFrame llamada Puntos, donde cada jugador obtiene Puntos = (Goles * 4) + (Asistencias * 2)


df['Puntos']=df['Goles']*4+df['Asistencias']*2

print(df)
print('\n')
# 5.- Calcula el promedio de goles de todos los jugadores

promedio_goles=df['Goles']

print(f'El promedio de goles de todos los jugadores es: {promedio_goles.mean()}')
print('\n')

# 6.- Obtén el máximo y mínimo de asistencias en el equipo

asistidor_max=df[df['Asistencias'].max()==df['Asistencias']]
asistidor_min=df[df['Asistencias'].min()==df['Asistencias']]

print('El jugador con mas asistencias:')
print(asistidor_max[['Jugador','Asistencias']])
print('El jugador con menos asistencias:')
print(asistidor_min[['Jugador','Asistencias']])
print('\n')
# 7.- Cuenta cuántos jugadores hay por posición (Delantero, Mediocampista)

print('Cantidad de jugadores que juegan de delantero:')
print(df['Posicion'].value_counts().get('Delantero',0))

print('Cantidad de jugadores que juegan de mediocampista:')
print(df['Posicion'].value_counts().get('Mediocampista',0))
print('\n')
# 8.- Ordena el DataFrame en función de los goles en orden descendente

df_Orden_Goles=df.sort_values(by='Goles',ascending=False)
print(df_Orden_Goles)
print('\n')
# 9.- Aplica describe() para obtener estadísticas generales del DataFrame

print('Estadisiticas de los jugadores'.center(50))
print(df.describe())
print('\n')
# 10.- Usa value_counts() para contar cuántos jugadores hay en cada posición

print('Cantidad de jugadores por posicion:'.center(55))
print(df['Posicion'].value_counts())