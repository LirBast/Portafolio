import pandas as pd

serie=pd.Series([10,20,30], index=["b0","b1","c"])
print(serie["b0"])

print(serie)

print(serie.mean)

materias=pd.Series([50,40,60], index=["matematicas", "ciencias", "lenguas"])
print(materias)

datos2={"matematicas":50, "ciencias":40, "lenguas":60}       ###Diccionario las claves son las materias y las notas son los valores
materias2=pd.Series(datos2)
print(materias2)