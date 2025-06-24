import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])

suma=a+b
print(suma)
# suma2=np.sum(a,b)   Hay que ver como se puede arreglar
# print(suma2)

producto=a*b
print(producto)

punto=np.dot(a,b)   #la suma de las multiplicaciones 1*4+2*5+3*6=total
print(punto)


