import numpy as np

#simulating N unbiased coin tosses
N = 1000
T = np.random.choice([0, 1], size=(N))

#obtaining frequencies and probabilities
X0 = np.count_nonzero(T == 0)
X1 = np.count_nonzero(T == 1)
P0 = X0/N
P1 = X1/N

#printing
print('n(X=0) = ', X0)
print('n(X=1) = ', X1)
print('Pr(X=0) = ', P0)
print('Pr(X=1) = ', P1)
