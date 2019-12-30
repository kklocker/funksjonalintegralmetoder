import numpy as np 
import matplotlib.pyplot as plt 

ef = 1

k = np.linspace(0,1.5)
ek = k**2

Vb = 1/4


Ekp = 1/2 * (ek + ef + np.sqrt((ek-ef)**2 + 4*Vb**2))
Ekm = 1/2 * (ek + ef - np.sqrt((ek-ef)**2 + 4*Vb**2))


plt.plot(k, Ekp)
plt.plot(k, Ekm)
plt.show()


print(k, ek, Ekp, Ekm)
