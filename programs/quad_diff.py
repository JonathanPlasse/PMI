#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:39:22 2018

@author: ROHR Julien, ROUSSEL Loïc, PLASSE Jonathan, NAILI Kamel
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from imageio import imread

z=1
lamb=500e-9
a=1
k=2*np.pi/lamb

def dbquadrect(f,xi,yi,Map) :
    global nbpx
    J=0.
    JX=0.
    x=np.linspace(-nbpx,nbpx,nbpx)
    y=np.linspace(-nbpx,nbpx,nbpx)
    for i in range(nbpx) :
        for j in range(nbpx) :
            if Map[i][j]!=0 :
                JX+=f(x[i],y[j],xi,yi)*(1/nbpx)
        J+=JX
    return(J) 

def r(x,y,xi,yi) :
    global z
    return((xi-x)**2+(yi-y)**2+z**2)
    
def realfquad(x,y,xi,yi) :
    global k
    return(np.cos(k*r(x,y,xi,yi))/(k*r(x,y,xi,yi)))
    
def imagfquad(x,y,xi,yi) :
    global k
    return(np.sin(k*r(x,y,xi,yi))/(k*r(x,y,xi,yi)))