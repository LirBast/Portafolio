import pandas as pd
import matplotlib.pyplot as plt

# Crear el DataFrame
df = pd.DataFrame({"Salario": [20000, 60000, 500000, 600000, 350000, 1000000, 250000, 850000, 4000000, 1000]})
print(df)
print("-----------------------")

# Calcular Q1 y Q3
q1 = df["Salario"].quantile(0.25)
q3 = df["Salario"].quantile(0.75)
print(f"El valor del cuartil 1 (Q1) es: {q1}")
print(f"El valor del cuartil 3 (Q3) es: {q3}")

# Calcular el IQR
iqr = q3 - q1
print(f"El valor del IQR es: {iqr}")

# Calcular límites inferior y superior para detectar outliers
lim_inf = q1 - 1.5 * iqr
lim_sup = q3 + 1.5 * iqr
print(f"El límite inferior es: {lim_inf}")
print(f"El límite superior es: {lim_sup}")

print("-----------------------")

# Filtrar outliers
outliers = df[(df["Salario"] < lim_inf) | (df["Salario"] > lim_sup)]
print("Outliers detectados:")
print(outliers)

# Visualización con boxplot
plt.figure(figsize=(8,5))
plt.boxplot(df["Salario"], vert=False)
plt.title("Boxplot de Salarios")
plt.xlabel("Salario")
plt.show()