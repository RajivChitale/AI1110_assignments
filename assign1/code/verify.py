import numpy as np

#find matrix X from B
B= np.array([ [1,1], [8, 3] ])
X= B*B- 4*B

Solution = np.array([ [1], [10] ])
L= X*Solution
R= np.array([ [5], [50] ])

coeff = np.poly(B)					#finds characteristic polynomial coefficients 
pol = np.polynomial.polynomial.Polynomial(coeff[::-1])  #creating polynomial object (needs reverse order of coeff)
np.polynomial.set_default_printstyle('unicode')
print('Characteristic polynomial of B is:')
print(pol)

print('\nMatrix X=')
print(X)
print('\nVerifying whether LHS=RHS for a=1 and b=10,')
print('\nLHS=')
print(L)
print('\nRHS=')
print(R)


