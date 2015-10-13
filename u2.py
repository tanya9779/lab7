import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-2.05,3.05,0.01)
plt.plot(x,x**2-6-x,x,x*0)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)=x^2-6-x$')
plt.grid(True)
plt.show()
