import numpy as np

#code to verify value of lambda and image vector R
#succesful if R = (0, -1, -3)

A = np.array([ [3], [-2], [1] ])
n = np.array([ [3],[-1],[4] ])
c = 2
nt = n.transpose()
lamda = (c- (nt @ A)) / (nt @ n)
R = A + 2* lamda * n

print('lambda =\n', lamda[0][0]) 
print('Given point A =\n', A)
print('Image R =\n', R)


