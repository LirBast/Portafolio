from scipy.stats import pearsonr
import numpy as np

horas_sueno=np.array([5,6,7,8,9])
calificaciones=np.array([60,65,70,75,95])

### hay que estudiar que es cada variable y como se puede interpretar los resultados


coeff, p_value=pearsonr(horas_sueno,calificaciones)
print('-----------------------------------------------------------------------------')
print(f'El coeficiente de pearson es: {coeff}')
print(f'El valor de p es: {p_value}')

if p_value<0.05:
    print('-----------------------------------------------------------------------------')
    print('La correlacion es estadisticamente significativa')
    print('Se rechaza la hipotesis nula, hay evidencia que el sueño afecta a las notas')
else:
    print('-----------------------------------------------------------------------------')
    print('La correlacion no es estadisticamente significativa')
    print('Se acepta la hipotesis nula, no hay evidencia que el sueño afecta a las notas')
