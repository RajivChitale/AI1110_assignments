import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 80
n = 10**6
U = np.fromfile("uni.dat", dtype='double', count= n, sep='', offset=0)

x = np.linspace(-2,2,pts)
F = [] 

for i in range(0,pts):
	F_n = np.count_nonzero(U < x[i]) #checking probability condition
	F.append(F_n/n) #storing the probability values in a list

plt.plot(x.T, F, color="blue" )#plotting the CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$F_U(x)$")
plt.title("Empirical CDF of U")
plt.savefig("../figs/fig1.2.png")
plt.show()


