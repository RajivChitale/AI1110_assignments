import numpy as np

R = np.arange(1,7)   #range of X and Y is [1,6]
Y,X = np.meshgrid(R,R) 
X = X.flatten()
Y = Y.flatten()
S = np.array((X,Y)).T  #S is sample space, containing all (X,Y) pairs
#note, S[:,0] represents values of X, S[:,1] represents values of Y

#generating sets A,B,C
locA = np.where(S[:,0] + S[:,1] > 8)  #locA has indices in S satisfying conditions for Set A
A = S[locA]	
locB = np.where( (S[:,0] == 2) | (S[:,1] == 2) )
B = S[locB]
locC = np.where( (S[:,0] + S[:,1] > 7) & ( (S[:,0] + S[:,1]) % 3 == 0) )
C = S[locC]

#1d indices useful in finding intersections of sets
locAnB = np.intersect1d(locA,locB)
AnB = S[locAnB]
locBnC = np.intersect1d(locB,locC)
BnC = S[locBnC]
locCnA = np.intersect1d(locC,locA)
CnA = S[locCnA]

#printing
print('Set A =') 
print(A) 
print('\nSet B =') 
print(B) 
print('\nSet C =') 
print(C) 

print('\nA ∩ B =') 
print(AnB) 
print('\nB ∩ C =') 
print(BnC) 
print('\nC ∩ A =') 
print(CnA) 
	
print('')
if(len(AnB)==0):
	print("A, B are mutually exclusive")
if(len(BnC)==0):
	print("B, C are mutually exclusive")
if(len(CnA)==0):
	print("C, A are mutually exclusive")
	
