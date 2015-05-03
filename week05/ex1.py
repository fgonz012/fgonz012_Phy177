'''
Created on May 1, 2015

@author: Francisco Gonzalez
'''

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as sc


def f(x):#original function
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1



def F(x): #derivative of the function
    return 5544*x**5 - 13860*x**4 + 12600*x**3 - 5040*x**2 + 840*x - 42



def findZeros(f,fderiv,tol,p0):#function to solve for 0s with a guess and within some error
    
    while(True):#calculate the error and compare with the specified error
        p = p0 - f(p0)/F(p0)#guess again
        if( abs(p-p0) < tol):# if its within the tolerance then exit and return the newst guess
            return p
        else:# otherwise update the guesses and continue
            p0 = p

t = np.linspace(0,1,100)#used to plot

#guess x = 0.03
zero1 = findZeros(f,F,1e-10,0.03)
zero2 = findZeros(f,F,1e-10,0.2)
zero3 = findZeros(f,F,1e-10,0.35)
zero4 = findZeros(f,F,1e-10,0.6)
zero5 = findZeros(f,F,1e-10,0.83)
zero6 = findZeros(f,F,1e-10,0.95)
print "First zero is: ", round(zero1,10)
print "Second zero is: ", round(zero2,10)
print "Third zero is: ", round(zero3,10)
print "Fourth zero is: ", round(zero4,10)
print "Fifth zero is: ", round(zero5,10)
print "Sixth zero is: ", round(zero6,10)

plt.plot(t,f(t))
plt.grid()
plt.title('Plot of function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig('ex1Plot.png',format = 'png')