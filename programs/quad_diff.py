#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:39:22 2018

@author: ROHR Julien, ROUSSEL Loïc, PLASSE Jonathan, NAILI Kamel
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from aperture_func import load_map
from numba import jit
import time

z=1 #distance between the aperture plane and the screen where the diffraction pattern shows in meters
lamb=500e-9 #wavelength in meters
a=0.01 #sidelength of the square containing the aperture in meters
k=2*np.pi/lamb #wavevector associated with the wavelength

@jit
def dbquadrect(f,xi,yi,Map) :
    """Returns the value of the surface integration of a given function using the rectangle rule.\n
    As it is intended to be used to draw a diffraction pattern, the function is supposed to be dependent on
    coordinates of the image plane, given as arguments. For the same reason, an array representing the transmittance
    of the aperture is also given as an argument."""
    J=0.
    JX=0.
    nbpx=Map.shape[0]
    x=np.linspace(-a,a,nbpx)
    y=np.linspace(-a,a,nbpx)
    for i in range(nbpx) :
        for j in range(nbpx) :
            if Map[i][j]!=0 :
                JX+=Map[i][j]*f(x[i],y[j],xi,yi)*(1/nbpx)
        J+=JX
    return(J) 
@jit
def r(x,y,xi,yi) :
    """Returns the distance between a point in the aperture plane and a point in the image plane."""
    global z
    return((xi-x)**2+(yi-y)**2+z**2)

@jit    
def realfquad(x,y,xi,yi) :
    """Real part of the function exp(ikr)/kr 
    integrated when calculating the amplitude associated to a point in the image plane."""
    global k
    return(np.cos(k*r(x,y,xi,yi))/(k*r(x,y,xi,yi)))
    
@jit    
def imagfquad(x,y,xi,yi) :
    """Imaginary part of the function exp(ikr)/kr 
    integrated when calculating the amplitude associated to a point in the image plane."""
    global k
    return(np.sin(k*r(x,y,xi,yi))/(k*r(x,y,xi,yi)))

@jit
def quad_diffpattern(Map,quadmethod=dbquadrect) :
    """Displays the diffraction pattern of an aperture -which is given as an argument array- 
    using an integration passed as an argument.\n
    We hold no responsibility about what happens if the array does not represent an aperture.""" 
    nbpx=Map.shape[0]
    Imap=np.zeros([nbpx,nbpx])
    xi=np.linspace(-a,a,nbpx)
    yi=np.linspace(-a,a,nbpx)
    for i in range(nbpx) :
        print("Working : ",i+1,'/',nbpx)
        for j in range(nbpx) :
            Imap[i][j]=dbquadrect(realfquad,xi[i],yi[j],Map)**2+dbquadrect(imagfquad,xi[i],yi[j],Map)**2
    diffsize=(nbpx-1)/2/a*lamb*z
    diffaxis = np.array([-diffsize,diffsize,-diffsize,diffsize])
    plt.figure()
    plt.imshow(abs(Imap),cmap=cm.gray,extent=diffaxis)
    plt.colorbar()
    plt.show()
    
#%%Test
if __name__=="__main__" :
    start_time=time.clock()
    Map=load_map("../resources/apertures/square_test.png")
    quad_diffpattern(Map)
    plt.figure()
    apaxis=np.array([-a,a,-a,a])
    plt.imshow(Map,cmap=cm.gray,extent=apaxis)
    plt.show()
    print(time.clock())
