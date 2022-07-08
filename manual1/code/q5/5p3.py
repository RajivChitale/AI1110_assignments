import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n = 10**6
Y = np.fromfile("max.dat", dtype='double', count= n, sep='', offset=0)
X = np.fromfile("ber.dat", dtype='double', count= n, sep='', offset=0)

delta = np.linspace(-0.3,0.3,n)
X = X+delta

plt.scatter(X, Y, color="blue", alpha=0.1) #plotting the CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter plot of Y")
plt.savefig("../../figs/fig5.3.png")
plt.show()


plt.scatter(X[0:n:100], Y[0:n:100], color="blue", alpha=0.1) #plotting the CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter plot of Y")
plt.savefig("../../figs/fig5.3b.png")
plt.show()

