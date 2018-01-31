#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.fftpack import fft2,fftshift
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from scipy import misc

def readPicture(pictureName):
    """Converts 'Image array' to binary array"""
    return np.array(misc.imread(pictureName)[:,:])/255

def savePicture(pictureName,D):
    """Converts 'Image array' to binary array"""
    misc.imsave(pictureName,D*255)



a=1 #m
z=100 #m
lamb=2 #m

pictureName="Fractales/mandelbrot"

D=readPicture(pictureName+".png")
I=abs(fftshift(fft2(D)))
savePicture(pictureName+"d.png",I)

size=a*10
ech=D.shape[0]
isize = (ech-1)/4/size*lamb*z
xi = np.linspace(-size,size,ech)
yi = np.linspace(-size,size,ech)

oaxis = np.array([-size,size,-size,size])
iaxis = np.array([-isize,isize,-isize,isize])

f, (ax1, ax2) = plt.subplots(1, 2)

ax1.imshow(D, cmap=cm.gray, extent=oaxis)
ax2.imshow(I, extent=iaxis)
ax2.axis(iaxis)
plt.show()
