import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 80
n = 10**6
V = np.fromfile("exp.dat", dtype='double', count= n, sep='', offset=0)

x = np.linspace(-2,10,pts)
F = [] 

for i in range(0,pts):
	F_n = np.count_nonzero(V < x[i]) #checking probability condition
	F.append(F_n/n) #storing the probability values in a list

plt.plot(x.T, F, color="blue" )#plotting the CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$F_V(x)$")
plt.title("Empirical CDF of V")
plt.savefig("../../figs/fig3.1.png")
plt.show()


