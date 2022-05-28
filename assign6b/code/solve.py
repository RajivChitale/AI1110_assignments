import numpy as np
import pandas as pd

N=50
#large N limiting to stationary state

#transition matrix
data_matrix = pd.read_excel('../tables/data_matrix.xlsx', index_col=False, usecols=range(1,6))
P = data_matrix.to_numpy()

#initial state
data_initial = pd.read_excel('../tables/data_initial.xlsx', index_col=False)
S = data_initial.to_numpy()
S = S.flatten()

#calculating limiting state
Q = S@(np.linalg.matrix_power(P, N))
Q = Q.round(4)

#print required probability
print("Steady state vector of Markov chain:")
print(Q)
print("Required Probability = ", Q[4]) 

#save to file
data_final = pd.DataFrame(Q).T
data_final.to_excel(excel_writer = "../tables/table3.xlsx")
