import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import mpmath

def Q(z):
	return (1-mpmath.erf(z /math.sqrt(2) ) )/2

pts = 50

n = 10**6
X = np.fromfile("gau.dat", dtype=float, count= n, sep='', offset=0)

x = np.linspace(-6,6,pts)

#Empirical CDF
F = [] 
for i in range(0,pts):
	Fcount = np.count_nonzero(X < x[i]) 
	F.append(Fcount/n) 
	
#Empirical PDF
p = []
for i in range(0,pts-1):
	p.append( (F[i+1] - F[i])/ (x[i+1]-x[i]) )
	
#Theoretical PDF
def gen_p_theory(xi):
	return math.exp(-(xi**2)/2) / math.sqrt(2*math.pi)
	
vecgen_p_theory = np.vectorize(gen_p_theory)
p_theory = vecgen_p_theory(x)

#Theoretical CDF
def gen_F_theory(xi):
	return  1-Q(xi)

vecgen_F_theory = np.vectorize(gen_F_theory)
F_theory = vecgen_F_theory(x)
		
#Method1: cumulative
#dx = (x[pts-1]-x[0])/(pts-1)
#F_theory = [p_theory[0]]
#for i in range(1,pts):
#	F_theory.append( F_theory[i-1] + p_theory[i] * dx )

#Method2: using library
#F_theory = np.cumsum(p_theory)* dx

#Method3: using Q and error function, without vectorize
#F_theory = []
#for i in range(0,pts): 
#	F_theory.append( 1-Q(x[i]) )		#for mean =0 and variance = 1

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


