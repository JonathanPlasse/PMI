#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.fftpack import fft2,fftshift
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

a=1 #m
z=100 #m
lamb=2 #m

n=100

def distribe(x,y,e):
    if ((x/a)**2*(1-e**2)+(y/a)**2)<=1:
        return 1
    else:
        return 0

size=a*10
ech=1000
isize = (ech-1)/4/size*lamb*z
xi = np.linspace(-size,size,ech)
yi = np.linspace(-size,size,ech)

oaxis = np.array([-size,size,-size,size])
iaxis = np.array([-isize,isize,-isize,isize])

f, (ax1, ax2) = plt.subplots(1, 2)

e=0
for i in range(n):
    D=np.array([[distribe(xi[i],yi[j],e) for j in range(ech)] for i in range(ech)])
    I=fftshift(fft2(D))

    ax1.imshow(D, cmap=cm.gray, extent=oaxis)
    ax2.imshow(abs(I), cmap=cm.gray, extent=iaxis)
    ax2.axis(iaxis/4)
    plt.savefig(str(i)+".png")
    print(i+1,"/",n)
    e+=(9/10)**(i+1)/9
