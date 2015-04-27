'''
Created on Apr 26, 2015

@author: Francisco Gonzalez
'''

import pylab as plt
import numpy as np

# Constants
eps =  8.854187817
q1 = 1 #Coulombs
q2 = -1 #Coulombs

#create the x and y axes [0,1,2,3,...,100] 100cm=1m
side = np.linspace(0,100,100)
X,Y = np.meshgrid(side,side)

#Create the distances grid
R1 = np.sqrt(    (Y-50)**2   +   (X-45)**2  )
R2 = np.sqrt(    (Y-50)**2   +   (X-65)**2  ) 
 
phi = 1/(4*np.pi*eps)*(  q1/R1 + q2/R2   ) #calculate the potential

#E = np.sqrt(1/(4*np.pi*eps)*np.sqrt((q1/(R1**2))**2 + (q2/(R2**2))**2 )) #calculte the electric field

## X derivative
h = 1.

maxX = len(X) - 1
maxY = len(Y) - 1

E = phi*0 # hold for the electric field
phiX = phi*0 # hold for the partial X derivative
phiY = phi*0 # hold for the partual Y derivative

for i in range(0,len(X)): # calculating the X derivative and putting it into phiX the 0th and last rows are treated independently
    if i == 0:
        phiX[0,:] = (phi[0,:] - phi[1,:])/h
        continue
    if i == maxX:
        phiX[maxX,:] = ( phi[maxX,:] - phi[maxX-1,:] )/h
        continue
    
    phiX[i,:] = ( phi[i-1,:] - phi[i+1,:] )/h

for i in range(0,len(Y)):# calculating the Y derivative and poutting it into phiY the 0th and last columns are treated independently 
    if i == 0:
        phiY[:,0] = (phi[:,0] - phi[:,1])/h
        continue
    if i == maxY:
        phiY[:,maxY] = ( phi[:,maxY] - phi[:,maxY-1] )/h
        continue
    
    phiY[:,i] = ( phi[:,i-1] - phi[:,i+1] )/h

for i in range(0,len(X)):#we have the parial x and partial y and we can find the E field
    for j in range(0,len(Y)):
        E[i,j] = np.sqrt(  phiX[i,j]**2 + phiY[i,j]**2  )
    
    
# Plot the density map
f = plt.subplot(2,1,1)
g = plt.subplot(2,1,2)

f.imshow(phi, extent = (np.amin(X), np.amax(X), np.amin(Y), np.amax(Y)),vmin=-0.0002,vmax=0.0002)
f.set_title('Electric Potential of a Dipole')

g.imshow(E, extent = (np.amin(X), np.amax(X), np.amin(Y), np.amax(Y)),vmin=0,vmax=0.0001)
g.set_title('Electric Field Magnetude of a Dipole')

plt.show()

