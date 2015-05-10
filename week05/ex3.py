'''
Created on May 10, 2015

@author: Francisco Gonzalez
'''
import numpy as np
import matplotlib.pyplot as plt

def fourier(y):#Discrete Fourier transform, since our functions are real we can discard the 2nd half of the coefficients
    N = len(y)
    
    c = np.zeros(N/2+1,complex)
    
    for k in range(N/2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
            
    return c

y = np.loadtxt("sunspots.txt")
print "This may take 30-45sec to calculate."

t = y[:,0]
y = y[:,1]

c = fourier(y)
c = abs(c)
c = np.square(c)

N = float((len(c)-1)*2 + 1)#length of the FT data, will be used to calculate frequency from k

print "Estimate for cycle length: 100 months."
maxk = 10

for k in range(1,200):#seeing from the plot the highest peak is clearly between 10 and 200
    if c[k] > c[maxk]:
        maxk = k
        
fs = 1 # sample rate, 1 sample per month
months_per_cycle = 1/(maxk*fs/N) # calculation of the frequency from k

print "Non-zero k with the highest contribution: k =", maxk
print "Months per cycle, calculated: ", int(months_per_cycle), "months."

#Plotting all of the figures
plt.figure(1)

plt.subplot(311)
plt.plot(t,y)
plt.grid()
plt.title('Sunspots over months')
plt.xlabel('Month starting from 1749')
plt.ylabel('Number of Sunspots')



plt.subplot(312)
plt.plot(c)
plt.grid()
plt.title('Fourier Transform')
plt.xlabel('k')
plt.ylabel('Magnitude')
plt.ylim(0,2.1e9)


plt.subplot(313)
plt.plot(t,y,t,50*np.sin(2*np.pi*(1/months_per_cycle)*t)+50)
plt.grid()
plt.title('Data with its fundamental sine wave')

plt.tight_layout()
plt.show()



