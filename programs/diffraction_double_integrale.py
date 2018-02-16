#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from numba import jit #You must use conda or anaconda to use this module

#Constants of the problem
z=1 #distance between the aperture plane and the screen where the diffraction pattern shows in meters
lamb=500e-9 #wavelength in meters
a=0.0008 #sidelength of the square image containing the aperture in meters
k=2*np.pi/lamb #wavevector associated with the wavelength

ech=100
n=20

aperture_size=0.0001

size=a
isize = (ech-1)/4/size*lamb*z #scale of the diffraction pattern

X = np.linspace(-size,size,ech)
Y = np.linspace(-size,size,ech)

x = np.linspace(-isize,isize,ech)
y = np.linspace(-isize,isize,ech)

#Axis scale of the diffraction plane [xmin,xmax,ymin,ymax]
oaxis = np.array([-size,size,-size,size])
#Axis scale of the interference figure plane [xmin,xmax,ymin,ymax]
iaxis = np.array([-isize,isize,-isize,isize])

@jit
def distribsqr(x,y):
    """Square distribution"""
    if abs(x)<=aperture_size and abs(y)<=aperture_size:
        return 1
    else:
        return 0

@jit
def fsqr(X,Y,x,y):
    """Integrated function for a square aperture"""
    return distribsqr(X,Y)*np.cos(-k/z*(x*X+y*Y))

@jit
def distribc(x,y):
    """Circle distribution"""
    if x**2+y**2<=aperture_size**2:
        return 1
    else:
        return 0

@jit
def fc(X,Y,x,y):
    """Integrated function for a circular aperture"""
    return distribc(X,Y)*np.cos(-k/z*(x*X+y*Y))

@jit
def integraleDoubleRectangle(f,x,y,n):
    """Double quadrature using the rectangle rule"""
    I=np.zeros((ech,ech))
    X=np.linspace(-aperture_size,aperture_size,n)
    Y=np.linspace(-aperture_size,aperture_size,n)
    for xi in range(ech):
        for yi in range(ech):
            for Xi in X:
                for Yi in Y:
                    I[xi,yi]+=f(Xi,Yi,x[xi],y[yi])
    return I

@jit
def aux(f,xi,yi,Xi,Y):
    s = 0
    s =(f(Xi,-aperture_size,x[xi],y[yi])+f(Xi,aperture_size,x[xi],y[yi]))/2
    for Yi in Y:
        s+=f(Xi,Yi,x[xi],y[yi])
    return s

@jit
def integraleDoubleTrapeze(f,x,y,n):
    """Double quadrature using the trapezoidal rule"""
    I=np.zeros((ech,ech))
    X=np.linspace(-aperture_size,aperture_size,n)[1:n-1]
    Y=np.linspace(-aperture_size,aperture_size,n)[1:n-1]
    for xi in range(ech):
        for yi in range(ech):
            I[xi,yi]+=(aux(f,xi,yi,-aperture_size,Y)+aux(f,xi,yi,aperture_size,Y))/2
            for Xi in X:
                I[xi,yi]+=aux(f,xi,yi,Xi,Y)
            
    return I

#Diffraction pattern calculation
D1=np.array([[distribsqr(X[i],Y[j]) for j in range(ech)] for i in range(ech)])

I1=integraleDoubleRectangle(fsqr,x,y,n)
I1=(abs(I1)/ech)**2

I2=integraleDoubleTrapeze(fsqr,x,y,n)
I2=(abs(I2)/ech)**2


D2=np.array([[distribc(X[i],Y[j]) for j in range(ech)] for i in range(ech)])

I3=integraleDoubleRectangle(fc,x,y,n)
I3=(abs(I3)/ech)**2

I4=integraleDoubleTrapeze(fc,x,y,n)
I4=(abs(I4)/ech)**2

#Diffraction pattern display
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)

ax1.imshow(D1, extent=oaxis)
ax2.imshow(I1, extent=iaxis)
ax3.imshow(I2, extent=iaxis)

ax4.imshow(D2, extent=oaxis)
ax5.imshow(I1, extent=iaxis)
ax6.imshow(I4, extent=iaxis)

plt.show()
