import matplotlib.pyplot as plt
import numpy as np

#takes vector n and constant c from equation of a plane. Takes point A and returns its image wrt the plane
def reflect(n, c, A):
	nt = n.transpose()
	lamda = (c- (nt @ A)) / (nt @ n)
	R = A + 2* lamda * n
	return R
	
#annotates the name and coordinates of a point P in 3d
def annotate3d(P, name):
	x= P[0,0]
	y= P[1,0]
	z= P[2,0]
	ax.text(x,y,z+0.2, '{} ({},{},{})'.format(name,x,y,z) , size= 15, zorder=3, color='r')
	return

#joints two endpoints into a single array for the purpose of plotting
def line_gen(P,Q):
	return np.concatenate((P,Q),axis=1)

#takes vector n and constant c from equation of a plane. Also takes a centrepoint mid
#plots a surface with a given size along x and y directions, centred at mid
def plane_gen(n, c, mid):
	xmid = mid[0,0]
	ymid = mid[1,0]
	size = 1.5
	x = np.linspace(xmid-size, xmid+size, 10)
	y = np.linspace(ymid-size, ymid+size, 10)
	X,Y = np.meshgrid(x,y)
	Z = (c - n[0,0]*X - n[1,0]*Y) / n[2,0]			#solving plane equation for Z		
	ax.plot_surface(X, Y, Z, color='orange', alpha=0.4)
	return

#sets the plot boundaries at a distance delta from a central point
def set_plot_boundary(centre, delta):
	ax.set_xlim3d(centre[0,0]-delta, centre[0,0]+delta)
	ax.set_ylim3d(centre[1,0]-delta, centre[1,0]+delta)
	ax.set_zlim3d(centre[2,0]-delta, centre[2,0]+delta)
	return

#Calculating R 
A = np.array([ [3], [-2], [1] ])
n = np.array([ [3],[-1],[4] ])
c = 2
R = reflect(n, c, A)

#Plotting
ax = plt.axes(projection='3d')
X_AR = line_gen(A, R)
plt.plot(X_AR[0,:], X_AR[1,:], X_AR[2,:], marker='o', label = "$AR$")	#plots A,R and line joining them
annotate3d(A, 'A')
annotate3d(R, 'R')

centrepoint=(A+R)/2 
plane_gen(n, c, centrepoint)		#plots plane

set_plot_boundary(centrepoint, 2.5)	
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.title('Image of a point about a plane')
plt.legend(loc="best")
plt.show()


