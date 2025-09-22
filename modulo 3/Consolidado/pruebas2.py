import pandas as pd
import numpy as np

df=pd.read_csv('C:\\Users\\liroy\\OneDrive\\Escritorio\\bootcamp\\clases\\modulo 3\\consolidado final\\material complementario evaluacion final\\migracion.csv')

import pandas as pd

# Crear tabla con solo Q1 y Q3
tabla_outliers = df.describe().loc[['25%', '75%']].round(2)

# Renombrar filas para mayor claridad (opcional)
tabla_outliers = tabla_outliers.rename(index={'25%': 'Q1', '75%': 'Q3'})

# Calcular IQR, límites inferior y superior
tabla_outliers.loc['IQR (Q3-Q1)'] = tabla_outliers.loc['Q3'] - tabla_outliers.loc['Q1']
tabla_outliers.loc['Límite Inferior'] = tabla_outliers.loc['Q1'] - 1.5 * tabla_outliers.loc['IQR (Q3-Q1)']
tabla_outliers.loc['Límite Superior'] = tabla_outliers.loc['Q3'] + 1.5 * tabla_outliers.loc['IQR (Q3-Q1)']

# Mostrar tabla reducida
print("------ Tabla solo con Q1, Q3, IQR y límites para outliers ------")
print(tabla_outliers)

for col in tabla_outliers.columns:
    if col in df.columns:
        li = tabla_outliers.loc['Límite Inferior', col]
        ls = tabla_outliers.loc['Límite Superior', col]
        
        # Filas con outliers en esta columna
        outliers_col = df[(df[col] < li) | (df[col] > ls)]
        
        if not outliers_col.empty:
            print(f"\nOutliers detectados en la columna '{col}':")
            print(outliers_col[['Pais_Origen', 'Pais_Destino', col]])
        else:
            print(f"\nNo se detectaron outliers en la columna '{col}'.")