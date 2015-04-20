import numpy as np
import ex1 as est #from the prvious examples
import scipy.integrate as inte


def f(x): #The Function to integrate
    return x**4 - 2.*x + 1

# create the N=20 function and fill it in
x = np.linspace(0,2,num=20)

func = np.zeros(len(x))

for i in range(0,len(x)):
    func[i] = f(x[i])
#estimate with simpsons rule
I20 = est.SimpsonsRule(x,func)

#use scipy's trap and simps rules and print all the results to screen
print "Simpson's rule estimates: ", round(I20,6)
print "Trapezoidal rule estimates: ", round(est.TrapRule(x, func),6)
print ""
print "Scipy's Simpson's rule estimates: ", round(inte.simps(func,x),6)
print "Scipy's Trapezoidal rule estimates: ", round(inte.trapz(func,x),6)

#creat the N=10 function and fill it in
x2 = np.linspace(0,2,num=10)
func2 = np.zeros(len(x))

for i in range(0,len(x2)):
    func2[i] = f(x2[i])

#estimate with simpsons's rule
I10 = est.SimpsonsRule(x2,func2)

#print to screen
print "\nError", round(abs((I20-I10)/15),6)
print "Exact value: 4.4"