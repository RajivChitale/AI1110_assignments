import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 50

n = 10**6
X = np.fromfile("gau.dat", dtype=float, count= n, sep='', offset=0)

x = np.linspace(-6,6,pts)
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
plt.ylabel("$p_X(x)$")
plt.title("Empirical PDF of X")
plt.savefig("../../figs/fig2.3.png")
plt.show()


