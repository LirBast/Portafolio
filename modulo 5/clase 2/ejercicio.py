import pandas as pd

# Datos como lista de listas
datos = [
    ["Maria", 25, "dados", 50],
    ["Pedro", 38, "cartas", 150],
    ["Sofia", 19, "ruleta", 20],
    ["Carlos", 45, "cartas", 300],
    ["Luisa", 30, "dados", 75]
]

# Crear DataFrame
df = pd.DataFrame(datos, columns=["Nombre", "Edad", "Juego", "Dinero"])

print(df)
