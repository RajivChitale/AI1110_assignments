import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 50
n = 10**6
U = np.fromfile("uni.dat", dtype='double', count= n, sep='', offset=0)

x = np.linspace(-2,2,pts)

F = [] 
for i in range(0,pts):
	F_n = np.count_nonzero(U < x[i]) #checking probability condition
	F.append(F_n/n) #storing the probability values in a list

def gen_F_theory(xi):
	if(xi<0):
		return 0.0
	elif(xi>1):
		return 1.0
	else:
		return xi

vecgen_F_theory = np.vectorize(gen_F_theory)
F_theory = vecgen_F_theory(x)

plt.scatter(x.T, F, color="blue", label="Empirical CDF" )#plotting the experimental CDF
plt.plot(x.T, F_theory, color="orange", label="Theoretical CDF" )#plotting the theoretical CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$F_U(x)$")
plt.legend(loc="best")
plt.title("Theoretical CDF of U")
plt.savefig("../../figs/fig1.3.png")
plt.show()


