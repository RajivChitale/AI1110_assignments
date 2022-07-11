import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

pts = 50

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
	
def gen_p_theory(xi):
	if(xi>=0):
		return math.exp(-xi/2) /2
	else:
		return 0.0
	
vecgen_p_theory = np.vectorize(gen_p_theory)
p_theory = vecgen_p_theory(x)

plt.scatter(x.T[0:(pts-1)], p, color="blue", label="Emperical PDF" )#plotting the empirical PDF
plt.plot(x.T, p_theory, color="orange", label="Theoretical PDF")#plotting the theoretical PDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$p_V(x)$")
plt.title("Empirical and theoretical PDF of V")
plt.savefig("../../figs/fig6.1b.png")
plt.show()


