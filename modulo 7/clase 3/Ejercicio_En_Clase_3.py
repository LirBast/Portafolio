import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

data = {
    'Monto': np.concatenate([np.random.normal(200, 50, 90), np.random.normal(2000, 300, 10)]),
    'Tiempo': np.concatenate([np.random.normal(10, 2, 90), np.random.normal(1, 0.5, 10)])
}

df = pd.DataFrame(data)
print(df.head())

# Escalado
escalado = StandardScaler()
df_scalado = escalado.fit_transform(df)

# DBSCAN
db_scan = DBSCAN(eps=0.5, min_samples=5)
etiquetas = db_scan.fit_predict(df_scalado)

# Plot
plt.scatter(df['Monto'], df['Tiempo'], c=etiquetas, cmap='viridis')
plt.title('Detección de outliers de transacciones bancarias con DBSCAN')
plt.xlabel('Monto')
plt.ylabel('Tiempo')
plt.show()

# Métricas
num_clusters = len(set(etiquetas)) - (1 if -1 in etiquetas else 0)
num_ruido = list(etiquetas).count(-1)
print(f'Número de clusters: {num_clusters}')
print(f'Puntos de ruido (outliers): {num_ruido}')

# Outliers reales (DBSCAN marca outliers con -1)
outliers = df[etiquetas == -1]
print('Outliers:')
print(outliers if not outliers.empty else 'No se detectaron outliers')