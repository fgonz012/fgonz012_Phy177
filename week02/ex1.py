'''
Created on Apr 11, 2015

author: Francisco Gonzalez
StudentID: 861077407
'''

def SimpsonsRule(x,y):
    
    h = (x[len(x)-1] - x[0]) / float(len(x)) ## h = (b-a) / N

    I = h * 0.5 * (y[0] + 2.0*sum(y[1:len(y)-1]) + y[len(y)-1] ) # I = (0.5*f(a) + 0.5*f(b) + SUM(rest of the values) ) * h
    
    return I


def TrapRule(x,y):
    h = (x[len(x)-1] - x[0]) / float(len(x)) ## h = (b-a) / N
    
    I = y[0] + y[len(y)-1]
    
    for i in range(1,len(y)):
        
        if  i%2 != 0:
            I += 4.*y[i]
            
        else:
            I += 2.*y[i]
            
    I =  ( h * I ) / 3
    
    return I