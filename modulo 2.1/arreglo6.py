import numpy as np


ang=np.array([0,np.pi/2,np.pi])   ###

print(ang)     ### son los angulos de cero pasando por pi divido 2 hasta pi
print(np.sin(ang))  ### Esto saca el seno de esos angulos
print(np.cos(ang))   ### Esto sacca el cos de los angulos    ### son expresiones en radianes 


hora=np.arange(0,24)    ### Este código sirve para calcular las componentes seno y coseno del ángulo asociado a cada hora del día, representando así las 24 horas como puntos sobre un círculo unitario. Es útil, por ejemplo,en análisis cíclicos o temporales como:

sin_hora=np.sin(hora*2*np.pi/24)
cos_hora=np.cos(hora*2*np.pi/24)

print(hora)

print(sin_hora)
print(cos_hora)