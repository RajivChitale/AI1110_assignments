import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 30
n = 10**6
V = np.fromfile("exp.dat", dtype='double', count= n, sep='', offset=0)

x = np.linspace(-2,10,pts)
F = [] 

for i in range(0,pts):
	F_n = np.count_nonzero(V < x[i]) #checking probability condition
	F.append(F_n/n) #storing the probability values in a list

#Experimental CDF
F_theory = []
for i in range(0,pts):
	F_theory.append(1-np.exp(-x/2)) #storing the probability values in a list

#Theoretical CDF	
def gen_F_theory(xi):
	return  1-np.exp(-xi/2)

vecgen_F_theory = np.vectorize(gen_F_theory)
F_theory = vecgen_F_theory(x)

plt.scatter(x.T, F, color="blue", label="Empirical CDF" )#plotting the empirical CDF
plt.plot(x.T, F, color="orange", label="Theoretical CDF" )#plotting the theoretical CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$F_V(x)$")
plt.title("Theoretical CDF of V")
plt.legend(loc="best")
plt.savefig("../../figs/fig3.2.png")
plt.show()


