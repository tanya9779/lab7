import matplotlib.pyplot as plt;
import numpy as np
import matplotlib.pyplot as plt

x1=[]
performance = []
inp1='Эта строка типа загружена из файла. Это типа так было.'

in_f=open('input.txt')
s=in_f.readline().rstrip()
tmp = list(s.split()))
#tmp=list(inp1.split())

for i in range(len(tmp)):
    if x1.count(len(tmp[i]))>0 :
        performance[x1.index(len(tmp[i]))]+=1
    else:
        x1.append(len(tmp[i]))
        performance.append(1)

y_pos = np.arange(len(x1))

plt.bar(y_pos, performance, align='center')
plt.xticks(y_pos, x1)
plt.ylabel('Count')
plt.title('Words len')

plt.show()