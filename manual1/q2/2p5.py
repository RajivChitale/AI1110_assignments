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

plt.scatter(x.T[0:(pts-1)], p, color="blue",label="Emperical PDF" )   #plotting the emperical CDF
plt.plot(x.T, p_theory, color="orange", label="Experimental PDF" ) #plotting the experimental CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$p_X(x)$")
plt.title("PDF of X")
plt.legend(loc="best")
plt.savefig("../figs/fig2.5.png")
plt.show()


