'''
Created on Apr 11, 2015

author: Francisco Gonzalez
StudentID: 861077407
'''

def SimpsonsRule(x,y):
    
    h = (x[len(x)-1] - x[0]) / float(len(x)) ## h = (b-a) / N
    
    I = y[0] + y[len(y)-1] # I = f(a) + f(b)
    
    
    for i in range(1,len(y)):
        I = I + 2*y[i] # I = f(a) + f(b) + 2 * SUM( y_k )
        
    I =I * 0.5 * h   # I =  h * [ 0.5f(a) +  0.5f(b) + y1 + y2 + y3 + ... + yN ]
    
    return I


def TrapRule(x,y):
    h = (x[len(x)-1] - x[0]) / float(len(x)) ## h = (b-a) / N
    
    I = y[0] + y[len(y)-1]
    
    for i in range(1,len(y)):
        
        if  i%2 != 0:
            I = I + 4*y[i]
            
        else:
            I = I + 2*y[i]
            
    I =  ( h * I ) / 3
    
    return I