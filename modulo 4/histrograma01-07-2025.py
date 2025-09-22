import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.DataFrame({'id':range(1,21),
                     'Producto':np.random.choice(['camiseta','pantalon','zapastos','gorras','Calcetines'],20),
                     'Precio':np.round(np.random.uniform(10,100,20)),
                     'Ventas':np.random.randint(1,50,20),
                     'Region':np.random.choice(['norte','Sur','Este','Oeste'],20),
                     'Descuento':np.random.choice([True,False],20),
                     'Calificacion_Cliente':np.random.randint(1,6,20)
                     })

df=pd.DataFrame(data)
media_ventas=df['Ventas'].median()
df['Ventas'].fillna(media_ventas, inplace=True)

media_precio=df['Precio'].median()
df['Precio'].fillna(media_precio, inplace=True)

moda_region=df['Region'].mode()[0]
df['Region'].fillna(moda_region, inplace=True)

print(df)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
sns.histplot(df['Ventas'],bins=5,kde=True)
plt.title('Distribucion de Ventas')
plt.xlabel("ventas")  #Eje X Ventas
plt.ylabel("Frecuencia") # Eje Y Frecuencia