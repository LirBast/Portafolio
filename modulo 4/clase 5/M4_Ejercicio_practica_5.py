import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 2 creación del conjunto de datos

df = pd.DataFrame({'Edad': [25, 30, 35, 40, 45, 50, 55, 60, 22, 28, 33, 38],
                   'Ingreso': [300000, 450000, 600000, 750000, 900000, 1050000, 1200000, 1350000, 250000, 400000, 550000, 700000],
                   'Años_de_educacion': [12, 14, 16, 18, 20, 22, 24, 26, 11, 13, 15, 17],
                   'Horas_de_sueño': [8, 7, 7, 6, 6, 5, 5, 4, 9, 8, 7, 6]})

print(df)
print('\n')
# 3 Cálculo de la matriz de correlación

matriz_correlacion = df.corr()

print(matriz_correlacion)


# 4 Generación del heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(matriz_correlacion, cmap = 'viridis', annot = True, fmt = '.2f' , linewidths = 0.5)
plt.title('Mapa de calor del DataFrame')
plt.show()

# 5 Interpretación y Personalización del gráfico

### Primero, a simple vista: en el heatmap con la paleta viridis, los colores más claros (amarillos/verde claro) muestran relaciones positivas fuertes entre las variables.
### Por ejemplo, cuando ves un valor cercano a 1, significa que si una variable sube, la otra también lo hace. O sea, van de la mano.

## Por otro lado, los tonos más oscuros (azules/morados) indican relaciones negativas. Esto quiere decir que,
## cuando una variable aumenta, la otra baja. No es una relación perfecta, pero sí bastante fuerte.

### De todas las variables, la que más destaca es la de horas de sueño. Se nota que, a medida que alguien duerme más,
### tiende a tener menos años de estudio, menos ingresos y también suele ser más joven. Así que, según estos datos,
### dormir mucho podría estar relacionado con tener menos ingresos y menos años de educación.
### Obvio, esto es solo lo que muestra este pequeño dataset, pero igual es curioso ver cómo el sueño parece influir en varios aspectos de la vida.