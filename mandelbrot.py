# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numba import jit
import numpy as np
from scipy import misc

def readPicture(pictureName):
    """Converts 'Image array' to binary array"""
    return misc.imread(pictureName)[:,:,0]/255

def savePicture(pictureName,D):
    """Converts 'Image array' to binary array"""
    misc.imsave(pictureName,D*255)



@jit
def mandelbrot(creal,cimag,maxiter):
    real = creal
    imag = cimag
    for n in range(maxiter):
        real2 = real*real
        imag2 = imag*imag
        if real2 + imag2 > 4.0:
            return 0
        imag = 2* real*imag + cimag
        real = real2 - imag2 + creal       
    return 1


@jit
def mandelbrot_set4(xmin,xmax,ymin,ymax,width,height,maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            n3[i,j] = mandelbrot(r1[i],r2[j],maxiter)
    return (r1,r2,n3)


x,y,d=mandelbrot_set4(-20.5,19.5,-20,20,4000,4000,80)

savePicture("mandelbrot.png", d)