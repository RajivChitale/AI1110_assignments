import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

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
	
p_theory = []
for i in range(0,pts):
	p_theory.append(math.exp(-(x[i]**2)/2) / math.sqrt(2*math.pi))	

dx = (x[pts-1]-x[0])/(pts-1)
F_theory = [p_theory[0]]
for i in range(1,pts):
	F_theory.append( F_theory[i-1] + p_theory[i] * dx )

#F_theory = np.cumsum(p_theory)* dx

plt.scatter(x.T[0:(pts-1)], p, color="blue",label="Empirical PDF" )   #plotting the empirical CDF
plt.plot(x.T, p_theory, color="orange", label="Theoretical PDF" ) #plotting the experimental CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$p_X(x)$")
plt.title("Theoretical PDF of X")
plt.legend(loc="best")
plt.savefig("../../figs/fig2.5.png")
plt.show()

plt.scatter(x.T, F, color="blue",label="Empirical CDF" )   #plotting the empirical CDF
plt.plot(x.T, F_theory, color="orange", label="Theoretical CDF" ) #plotting the experimental CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$F_X(x)$")
plt.title("Theoretical CDF of X")
plt.legend(loc="best")
plt.savefig("../../figs/fig2.5b.png")
plt.show()


