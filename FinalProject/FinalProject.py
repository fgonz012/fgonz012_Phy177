'''
Created on May 23, 2015

@author: Francisco Gonzalez
'''
from numpy import loadtxt, size, shape, zeros,exp, double, fft
from pylab import imshow, gray, show,subplot,title

data = loadtxt("blur.txt",float)

(a,b) = shape(data)
gau = zeros(shape(data),float)

sig = 25.0;

subplot(121)
imshow(data)
title('Before')
gray()


for x in range(-a/2,a/2):
    for y in range(-b/2,b/2):
        gau[x,y] = exp(-1*( x**2 + y**2)/(2*sig**2) )

#imshow(gau)
#show()

gaufft = fft.rfft2(gau)
datafft = fft.rfft2(data)
print gaufft.shape

unblurredfft = zeros(shape(gaufft),complex)
(c,d) = shape(unblurredfft)
minimum = 1e-3
for i in range(c):
    for j in range(d):
        divident = gaufft[i,j]
        if divident > minimum:
            unblurredfft[i,j] = datafft[i,j]/divident

unblurred = fft.irfft2(unblurredfft)

subplot(122)
imshow(unblurred)
title('After')
gray()
show()