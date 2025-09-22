# Dataset ficticio donde analizaremos el rendimiento de estudiantes de un curso de ciencia de datos.
# Variable 1: Registro de 100 estudiantes.
# Variable 2: Puntuación del examen (rango: 0 a 100).
# Variable 3: Horas de estudio semanales.
# Variable 4: Aprobación del curso (1 = aprobado, 0 = no aprobado).
import pandas as pd
import numpy as np

np.random.seed(42)  # Para reproducibilidad

n = 100
# Generar horas de estudio: normal, centrado en 10 horas con desviación estándar 4
horas_estudio = np.clip(np.random.normal(10, 4, n), 0, 20)

# Relación positiva entre horas de estudio y puntuación
puntuaciones = np.clip(horas_estudio * 6 + np.random.normal(0, 10, n), 0, 100)

# Aprobado si la nota es igual o mayor a 60
aprobado = (puntuaciones >= 60).astype(int)

# Crear el DataFrame
df = pd.DataFrame({
    "Estudiante": range(1, n + 1),
    "Puntuacion": puntuaciones.round(1),
    "Horas_Estudio": horas_estudio.round(1),
    "Aprobado": aprobado
})

print(df.head())