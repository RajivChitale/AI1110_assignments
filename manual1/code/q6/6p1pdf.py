import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 80

n = 10**6
X = np.fromfile("chi.dat", dtype=float, count= n, sep='', offset=0)

x = np.linspace(-2,8,pts)
F = [] 
for i in range(0,pts):
	Fcount = np.count_nonzero(X < x[i]) 
	F.append(Fcount/n) 

p = []
for i in range(0,pts-1):
	p.append( (F[i+1] - F[i])/ (x[i+1]-x[i]) )

plt.plot(x.T[0:(pts-1)], p, color="blue" )#plotting the CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$p_V(x)$")
plt.title("Empirical PDF of V")
plt.savefig("../../figs/fig6.1b.png")
plt.show()


