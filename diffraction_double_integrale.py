#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

a=1 #m
z=100 #m
lamb=2 #m
k=2*np.pi/lamb

size=a*16
ech=100
n=40
isize = (ech-1)/4/size*lamb*z

X = np.linspace(-size,size,ech)
Y = np.linspace(-size,size,ech)

x = np.linspace(-isize,isize,ech)
y = np.linspace(-isize,isize,ech)

oaxis = np.array([-size,size,-size,size])
iaxis = np.array([-isize,isize,-isize,isize])

def integraleDouble(f,x,y,iaxis,n):
    I=np.zeros((ech,ech))
    X=np.linspace(-a,a,n)
    Y=np.linspace(-a,a,n)
    for xi in range(ech):
        for yi in range(ech):
            for Xi in X:
                for Yi in Y:
                    I[xi,yi]+=fc(Xi,Yi,x[xi],y[yi])
        print(xi+1,"/",ech)
    return I

def distribc(x,y):
    if x**2+y**2<=a**2:
        return 1
    else:
        return 0

def fc(X,Y,x,y):
    return distribc(X,Y)*np.cos(-2*np.pi*(x*X+y*Y)/(lamb*z))

D=np.array([[distribc(X[i],Y[j]) for j in range(ech)] for i in range(ech)])

I=integraleDouble(fc,x,y,iaxis,n)
I=(abs(I)/ech)**2

plt.imshow(I, extent=iaxis)
plt.axis(iaxis)

plt.show()
