#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from numba import jit

a=1 #m
z=100 #m
lamb=2 #m
k=2*np.pi/lamb

size=a*64
ech=500
n=20
isize = (ech-1)/4/size*lamb*z

X = np.linspace(-size,size,ech)
Y = np.linspace(-size,size,ech)

x = np.linspace(-isize,isize,ech)
y = np.linspace(-isize,isize,ech)

oaxis = np.array([-size,size,-size,size])
iaxis = np.array([-isize,isize,-isize,isize])

@jit
def distribc(x,y):
    if abs(y)<=a and abs(y)<=a:
        return 1
    else:
        return 0

@jit
def fc(X,Y,x,y):
    return distribc(X,Y)*np.cos(-2*np.pi*(x*X+y*Y)/(lamb*z))

@jit
def integraleDoubleRectangle(f,x,y,n):
    I=np.zeros((ech,ech))
    X=np.linspace(-a,a,n)
    Y=np.linspace(-a,a,n)
    for xi in range(ech):
        for yi in range(ech):
            for Xi in X:
                for Yi in Y:
                    I[xi,yi]+=fc(Xi,Yi,x[xi],y[yi])
    return I

@jit
def integraleDoubleTrapeze(f,x,y,n):
    I=np.zeros((ech,ech))
    X=np.linspace(-a,a,n)[1:n-1]
    Y=np.linspace(-a,a,n)[1:n-1]
    for xi in range(ech):
        for yi in range(ech):
            I[xi,yi]+=(fc(-a,-a,x[xi],y[yi])+fc(-a,a,x[xi],y[yi]))/4
            for Yi in Y:
                I[xi,yi]+=fc(-a,Yi,x[xi],y[yi])/2

            I[xi,yi]+=(fc(a,-a,x[xi],y[yi])+fc(a,a,x[xi],y[yi]))/4
            for Yi in Y:
                I[xi,yi]+=fc(a,Yi,x[xi],y[yi])/2
                
            for Xi in X:
                I[xi,yi]+=(fc(Xi,-a,x[xi],y[yi])+fc(Xi,a,x[xi],y[yi]))/2
                for Yi in Y:
                    I[xi,yi]+=fc(Xi,Yi,x[xi],y[yi])
    return I

D=np.array([[distribc(X[i],Y[j]) for j in range(ech)] for i in range(ech)])

I1=integraleDoubleRectangle(fc,x,y,n)
I1=(abs(I1)/ech)**2

I2=integraleDoubleTrapeze(fc,x,y,n)
I2=(abs(I2)/ech)**2

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.imshow(I1, extent=iaxis)
ax1.axis(iaxis)

ax2.imshow(I2, extent=iaxis)
ax2.axis(iaxis)

plt.imshow(I1-I2, extent=iaxis)
plt.colorbar()

plt.show()
