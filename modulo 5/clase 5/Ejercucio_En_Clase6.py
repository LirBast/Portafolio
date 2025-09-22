from scipy.stats import norm

lvls_confianza = [0.85, 0.90 , 0.95 , 0.99]

for nc in lvls_confianza:
    z_crit = norm.ppf(1 - (1 - nc) / 2)
    print(f'El valor critico z para {nc * 100}% de confianza: {z_crit}')

# A medida que aumenta el nivel de confianza, también lo hace el valor crítico z.
# Esto se traduce en intervalos más amplios: tenemos más confianza de que el parámetro
# poblacional está dentro del intervalo, pero sacrificamos precisión.