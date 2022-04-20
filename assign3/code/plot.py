#Generates excel sheet with classmarks and point names. 
#Then it plots the corresponding frequency polygon

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string

#takes coordinates of points and labels them according to namelist
def annotate2d(X , Y, namelist):
	for i in range(len(X)):
		plt.text(X[i]-2, Y[i]+0.15, namelist[i], fontsize=15, color='red', zorder=2)
	return
	
#read excel file
data = pd.read_excel('../tables/table1.xlsx', index_col=False, skiprows=[11])

#find L, U, C 
data[['L','U']] = data['Marks'].str.split('-', expand=True)
data['L'] = data['L'].astype(int)
data['U'] = data['U'].astype(int)
data['C']= (data['L'] + data['U']) / 2
data['C'] = data['C'].astype(int) 		#removed decimal points only after checking that all classmarks are integers

#add higher imaginary class
w = data.iat[1,4] - data.iat[0,4]  #classwidth
pos= len(data.index) - 1 #final row position
Lmax= data.iat[pos,2] + w
Umax= data.iat[pos,3] + w
Cmax= data.iat[pos,4] + w
data.loc[pos+1] = ['{}-{}'.format(Lmax,Umax), 0, Lmax, Umax, Cmax] 

#add lower imginary class 
Lmin= data.iat[0,2] - w
Umin= data.iat[0,3] - w
Cmin= data.iat[0,4] - w
firstrow = pd.DataFrame({'Marks':['({})-{}'.format(Lmin, Umin)],
                    'Number of Students':[0],
                    'L' : [Lmin],
                    'U' : [Umin],
                    'C' : [Cmin] })                
data= pd.concat([firstrow, data], ignore_index=True)

#gives points names in the order A,B,C...
alphabet_string = string.ascii_uppercase
namelist = list(alphabet_string)[0:pos+3:]
data['Points']= namelist

#store excel file
data.to_excel('../tables/classmarks.xlsx', index=False)

#plot
data = data.to_numpy()
f = data[:,1].flatten()
C = data[:,4].flatten()
annotate2d(C, f, namelist)
plt.plot(C ,f, marker='.', color='b', label='(C,f)', zorder=1) 	#frequencies
plt.plot(C, np.zeros(pos+3), marker=2, color='b')		#x axis with class marks


plt.xlabel('Marks', fontsize=15)
plt.ylabel('Number of Students', fontsize=15)
plt.legend(loc='best')
plt.grid() 
plt.title('Frequency Polygon for Students vs Marks', fontsize=15)
plt.show()





