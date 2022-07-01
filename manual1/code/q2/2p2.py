import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 50
n = 10**6
X = np.fromfile("gau.dat", dtype=float, count= n, sep='', offset=0)

x = np.linspace(-6,6,pts)
F = [] 
for i in range(0,pts):
	F_n = np.count_nonzero(X < x[i]) 
	F.append(F_n/n) 

plt.plot(x.T, F, color="blue" )#plotting the CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$F_X(x)$")
plt.title("Empirical CDF of X")
plt.savefig("../figs/fig2.2.png")
plt.show()


