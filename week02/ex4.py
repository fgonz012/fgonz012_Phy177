'''
Created on Apr 19, 2015

@author: Francisco Gonzalez
'''
import numpy as np
import ex1 as est

def f(x):
    return ((np.sin(np.sqrt(100*x)))**2)

def I(N):
    return est.TrapRule( np.linspace(0,1,num=N) , f(np.linspace(0,1,num=N)))


rmin = 0
rmax = 1
N = 2

a = 0
b = 1

I1 = I(1) # initial 

sm = 0

while True:
    
    h = (b-a)/float(N) # h = (b-a)/N
    
    for k in range(1,N): # the sum SUM(a+k*h) from 0 to N (odds)
        if k % 2 != 0:
            sm += f(a + k*h)
    
    
    I2 = 0.5*I1 + h*sm # new value of I
    N = 2*N # new value of N
    sm = 0 # reset the sum from the above loop

    err = abs((I2-I1)/3) # calculate error for trap rule

    I1 = I2 # the previous I becomes the new I
    
    print "I = ", I2, " Error = ", err, " N = ", N
    if err < 1e-6: # if the error is less than 10^-6 stop the loop
        break

