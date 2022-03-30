import numpy as np

#find matrix X from B
B= np.matrix('1 1; 8 3')
X= B*B- 4*B

Solution = np.matrix('1;10')
L= X*Solution
R= np.matrix('5;50')

print('Matrix X=')
print(X)
print('\nVerifying whether LHS=RHS for a=1 and b=10,')
print('\nLHS=')
print(L)
print('\nRHS=')
print(R)
