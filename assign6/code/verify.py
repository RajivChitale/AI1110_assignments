import random as rd
import numpy as np

C1 = 1 #label for cases satisfying X_2 = 1 and X_3 = 1
C2 = 2 #label for other cases satsifying X_3 = 1
N = 10000

#contains X2 and X3 for one trial
class EventTracker:
	def __init__(self):
		self.X2 = 0
		self.X3 = 0

#simulation of coin toss
def coin_toss(trial):
	trial.X2 = rd.randint(0,1)
	return

#simulation of die throw
def dice_throw(trial):
	X1 = rd.randint(1,6)
	if (X1 == 3): trial.X3 = 1  #when 3 appears in a die throw
		
	if(X1 % 3 == 0):
		dice_throw(trial)
	else:
		coin_toss(trial)
	return

#returns labels depending on outcome from dice throw
def outcome_gen():
	trial = EventTracker()
	dice_throw(trial)
	if(trial.X2 == 1 and trial.X3 == 1): return C1
	elif(trial.X3 == 1): return C2
	else: return 0

outcomes = np.zeros(N)
for i in range(N):
	outcomes[i] = outcome_gen()
	
#Note: each trial may have different number of steps due to recursion after die throw 
#Thus, a single operation cannot be on the entire array. The loop is used because the trials had to be carried out individually
	
ncount = np.count_nonzero(outcomes == C1)		  #cases satisfying X_2 = 1 and X_3 = 1
dcount = ncount +  np.count_nonzero(outcomes == C2)		 #all cases satisfying  X_3 = 1
print("Required conditional probability from", N, "trials is:")
print(ncount/dcount)


