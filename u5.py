from math import*
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-10,10.01, 0.01)
plt.xkcd()
f=input()
plt.plot(x,eval(f))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)$')
plt.grid(True)
plt.show()

