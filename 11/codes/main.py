import matplotlib.pyplot as plt
import numpy as np

data=np.loadtxt("terms.txt", skiprows=1)

plt.close("all")

n=data[:5,0]
y_n=data[:5,1]


plt.stem(n, y_n, markerfmt='bo', linefmt='b-', basefmt='r-',label=r'Simulation') 
plt.axhline(y=243, color='green', linestyle='--',label='y=243')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.xticks(n)
plt.title('Simulation v/s Analysis')

plt.legend()
plt.grid(True)
plt.savefig("figure_plot.png")
plt.show()
