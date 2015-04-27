'''
Created on Apr 26, 2015

@author: Francisco Gonzalez
'''


import numpy as np
from numpy.linalg import solve

Vss= 5

# system of equations
A = np.array([[4,-1,-1,-1],[-1,0,3,-1],[1,1,1,-4],[1,-3,0,1]],float)
V = np.array([Vss,Vss,0,0],float)

#Gaussian elimination
for m in range(len(V)): # divide the row by the first column's number
    V[m] /= A[m,m]
    A[m,:] /= A[m,m]
    
    for i in range(m+1,(len(V))):#subtract rows to make the m+1's row lead with a 0
        V[i] -= V[m] * A[i,m]
        A[i,:] -= A[m,:]*A[i,m]
        
x = np.array([0,0,0,0],float) # holder for the solutions

for m in range(len(V)-1,-1,-1):#back substitution to get the x array filled
    x[m] = V[m]
    for i in range(m+1,len(V)):
        x[m] -= A[m,i]*x[i]
        
        
x_better = solve(A,V)#using the built in solver
        
rnd = 2 #round to make it look better
print "Using custom solution. In [V]: \nV1 = ", round(x[0],rnd),"\nV2 = ",round(x[1],rnd),"\nV3 = ",round(x[2],rnd),"\nV4 = ",round(x[3],rnd),"\n"
print "Using numpy linalg. In [V]:\nV1 = ", round(x_better[0],rnd),"\nV2 = ",round(x_better[1],rnd),"\nV3 = ",round(x_better[2],rnd),"\nV4 = ",round(x_better[3],rnd)