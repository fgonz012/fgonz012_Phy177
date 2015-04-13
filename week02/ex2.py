'''
Created on Apr 11, 2015

@author: Francisco Gonzalez
SID: 861077407
'''

import ex1 as est #Import the function from part 1
import numpy as np
import matplotlib.pyplot as plt


fileID = open('velocities.txt','r')

data_arr = np.loadtxt(fileID) # This is the data array it is an array of 1x2 arrays

time = [] # These are the time and velocities data we are gooing to fill later on
velocities = []

for i in range(len(data_arr)): #Filling the data here, data is i'th row and 0th column and velocities is i'th row and 1st column
    time.append(  data_arr[i][0]  )
    velocities.append( data_arr[i][1]  )
    
distanceSimpson = est.SimpsonsRule(time,velocities) # Total Distance traveled
distanceTrap = est.TrapRule(time, velocities)

distanceList = []# distance at different intervals according to SimpsonsRule

for i in range(1,len(time)+1): # Filling in the distance list
    distanceList.append( est.SimpsonsRule( time[0:i], velocities[0:i] ) )

# Print out the total distance for each estimate
print "Simpson's Rule estimates the distance to be: ", round(distanceSimpson,6) , " meters."
print "The Trapezoidal rule estimates the distance to be: ", round(distanceTrap,6), " meters."


#Plotting the two subplots and making them pretty
f = plt.subplot(2,1,1)
g = plt.subplot(2,1,2)

f.plot(time, velocities)
g.plot(time, distanceList)

f.set_title('Time vs Velocities')
g.set_title('Time vs Distance')

plt.xlabel('Time [s]')
plt.ylabel('                                                         Distance [m]                                  Velocities [m/s]')
g.grid()
f.grid()
plt.show()

fileID.close()