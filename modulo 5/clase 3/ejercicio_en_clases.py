import pandas as pd

tiempos=[1.2, 2.5, 3.0, 4.1, 5.3, 0.8, 6.7, 7.2, 1.9, 3.5, 4.8, 5.9, 2.1, 0.5, 8.1, 9.0, 3.3, 4.5, 6.1, 7.8, 1.5, 2.8, 3.9, 5.0, 6.3, 0.9, 7.5, 8.5, 2.2, 3.7, 4.9, 6.0, 7.0, 1.1, 8.8, 9.5, 3.1, 4.6, 5.8, 6.9, 2.0, 0.7, 7.3, 8.2, 1.8, 3.2, 4.3, 5.5, 6.5, 9.8]

print(tiempos)

df=pd.DataFrame(tiempos)

print(df.describe().round(3))
print(f'la cantidad de valores del data es: {df.count()}')
