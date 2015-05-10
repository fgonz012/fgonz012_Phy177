'''
Created on May 8, 2015

@author: Francisco Gonzalez
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
print "This may take 15-20sec to calculate."

def singlesquare(x,height):
    x_new = np.zeros(len(x),float)
    
    for i in range(len(x)):
        if x[i] <= height/2 and x[i] >= height*(-1)/2:
            x_new[i] = 1
        else:
            x_new[i] = 0
    return x_new

def modulated_sin(n):
    N = len(n)
    y = np.zeros(N,float)
    for i in range(N):
        y[i] = np.sin(np.pi*n[i]/N) * np.sin(20*np.pi*n[i]/N)
    return y

def fourier(y):
    N = len(y)
    
    c = np.zeros(N/2+1,complex)
    
    for k in range(N/2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
            
    return c

def sawtooth(n):
    
    return signal.sawtooth(n)

n = np.linspace(-50,50,1000)
n2 = np.linspace(-500,500,1000)

f1 = sawtooth(n)
f2 = modulated_sin(n2)
f3 = singlesquare(n, 1)

c1 = abs(fourier(f1))
c2 = abs(fourier(f2))
c3 = abs(fourier(f3))

c1_length = range(len(c1))
c2_length = range(len(c2))
c3_length = range(len(c3))

plt.figure(1)
plt.subplot(321)
plt.plot(n, f1)
plt.grid()
plt.title('Sawtooth Wave')

plt.subplot(322)
plt.plot(c1_length,c1)
plt.grid()
plt.title('Sawtooth Wave DTF')


plt.subplot(323)
plt.plot(n2,f2)
plt.grid()
plt.title('Modulated Sine')


plt.subplot(324)
plt.plot(c2_length,c2)
plt.grid()
plt.title('Modulated Sine DTF')


plt.subplot(325)
plt.plot(n,f3)
plt.grid()
plt.title('Square Pulse')


plt.subplot(326)
plt.plot(c3_length,c3)
plt.grid()
plt.title('Square Pulse DTF')


plt.show()








