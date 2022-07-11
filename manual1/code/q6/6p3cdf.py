import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

pts = 50
n = 10**6
X = np.fromfile("ray.dat", dtype=float, count= n, sep='', offset=0)

#Empirical CDF
x = np.linspace(-2,4,pts)
F = [] 
for i in range(0,pts):
	F_n = np.count_nonzero(X < x[i]) 
	F.append(F_n/n) 
	
#Theoretical CDF
def gen_F_theory(xi):
	if(xi>=0):
		return 1.0 - math.exp(-xi**2/2)
	else:
		return 0.0
	
vecgen_F_theory = np.vectorize(gen_F_theory)
F_theory = vecgen_F_theory(x)

plt.scatter(x.T, F, color="blue", label="Emperical CDF" )#plotting the empirical CDF
plt.plot(x.T, F_theory, color="orange", label="Theoretical CDF")#plotting the theoretical CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$F_A(x)$")
plt.legend(loc="best")
plt.title("Empirical and Theoretical CDF of A")
plt.savefig("../../figs/fig6.3.png")
plt.show()

