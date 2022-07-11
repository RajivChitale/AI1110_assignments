import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pe as pefuncs
import os

n = 10**6
pts = 20
A = np.linspace(0, 3, pts, dtype='double') #A varies from 0 to 1 

#Experimental pe
X = np.fromfile("ber.dat", dtype='double', count= n, sep='', offset=0)
pe = []
for a in A:
	os.system("./5p2.out "+str(a))
	Y = np.fromfile("max.dat", dtype='double', count= n, sep='', offset=0)
	pe.append(pefuncs.p_e(X,Y))
os.system("./5p2.out 0.5") #back to default

#Theoretical pe
pe_theory = []	
for a in A:
	pe_theory.append(pefuncs.p_e_theory(a))

plt.scatter(A, pe, color="blue", label="Empirical $P_e$" )#plotting the graph of experimental Pe
plt.plot(A, pe_theory, color="orange", label="Theoretical $P_e$" )#plotting the theoretical of experimental Pe
plt.grid()
plt.minorticks_on()
plt.xlabel("$A (Bell)$")
plt.ylabel("$P_e$")
plt.legend(loc="best")
plt.title("$P_e$ vs $A$")
plt.savefig("../../figs/fig5.7.png")
plt.show()


plt.semilogy(A, pe, '.' )#plotting the graph of experimental Pe
plt.semilogy(A, pe_theory)#plotting the theoretical of experimental Pe
plt.grid()
plt.minorticks_on()
plt.xlabel("$A (Bell)$")
plt.ylabel("$log(P_e)$")
plt.legend(["Empirical $P_e$", "Theoretical $P_e$"])
plt.title("$log(P_e)$ vs $A$")
plt.savefig("../../figs/fig5.7b.png")
plt.show()

 
