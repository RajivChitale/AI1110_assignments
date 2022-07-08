import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import mpmath

#Finding theoretical pe
def Q(z):
	return (1-mpmath.erf(z /math.sqrt(2) ) )/2
	
def p_e_theory(A):
	return Q(A) #because equally probable 2, * 0.5 * Q(A) 

#Finding experimental pe
def case_e(x, y):
	if( y<0 and x == 1):
		return 1		#pe0
	elif( y>0 and x == -1):
		return 1		#pe1
	else:
		return 0

vec_e = np.vectorize(case_e)

def p_e(X,Y):
	return np.sum(vec_e(X,Y)) / np.size(X)
