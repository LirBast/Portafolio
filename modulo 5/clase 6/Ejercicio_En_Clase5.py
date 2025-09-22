import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
 
arreglo1 = np.linspace(-4,8,1000)
h0 = norm.pdf(arreglo1,0,1)
h1 = norm.pdf(arreglo1,3,1)
 
 
plt.plot(arreglo1,h0,label="H0")
plt.plot(arreglo1,h1,label="H1")
plt.axvline(norm.ppf(0.95), color='red', linestyle='--', label ='alpha')
plt.fill_between(arreglo1[arreglo1>norm.ppf(0.95)], h1[arreglo1>norm.ppf(0.95)], alpha=0.3 , label = 'Power')
plt.legend()
plt.show()
 