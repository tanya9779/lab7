# 7. Построить график функции Вейерштрасса
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    a=3
    b=0.5
    n=20
    result=0
    for i in range(n):
        result+=b**i * math.cos(a**i*math.pi*x)
    return result


x=np.arange(-2,2.01,0.01)
y= [f(tmp) for tmp in x]


plt.plot(x,y)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)$')
plt.grid(True)
plt.show()
