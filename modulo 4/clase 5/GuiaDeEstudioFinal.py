import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

## crear un Dataframe con datos de ejemplo

df = pd.DataFrame({
    'Edad': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Ingresos': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
    'Años_Educación': [12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
    'Horas_Sueño': [7, 6.5, 7.5, 8, 7, 6, 7, 8, 7.5, 6.5]})

## Matriz de correlacion

correlacion=df.corr()
print(correlacion)

## Crear el heatmap
plt.figure(figsize=(8,6))
sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5,linecolor='black')
plt.title('Mapa de Calor de Correlaciones',fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()