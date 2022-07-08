import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 50
n = 10**6
X = np.fromfile("chi.dat", dtype=float, count= n, sep='', offset=0)

x = np.linspace(-2,8,pts)
F = [] 
for i in range(0,pts):
	F_n = np.count_nonzero(X < x[i]) 
	F.append(F_n/n) 

plt.plot(x.T, F, color="blue" )#plotting the CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$F_V(x)$")
plt.title("Empirical CDF of V")
plt.savefig("../../figs/fig6.1a.png")
plt.show()


