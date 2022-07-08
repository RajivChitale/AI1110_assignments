import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n = 10**6
X = np.fromfile("ber.dat", dtype='double', count= n, sep='', offset=0)
Y = np.fromfile("max.dat", dtype='double', count= n, sep='', offset=0)
		
def case_e0(x, y):
	if( y<0 and x == 1):
		return 1
	else:
		return 0
		
def case_e1(x, y):
	if( y>0 and x == -1):
		return 1
	else:
		return 0

vec_e0 = np.vectorize(case_e0)
vec_e1 = np.vectorize(case_e1)

def p_e0(X,Y):
	return np.sum(vec_e0(X,Y)) / np.count_nonzero(X==1)
	
def p_e1(X,Y):
	return np.sum(vec_e1(X,Y)) / np.count_nonzero(X==-1)
		
p0 = p_e0(X,Y)		
p1 = p_e1(X,Y)

print("Pr(X^ = -1 | X = 1) = ", p0)
print("Pr(X^ = 1 | X = -1) = ", p1)
print("Experimental Pe = ", 0.5*(p0 + p1) )
print(np.sum(vec_e0(X,Y)) )


