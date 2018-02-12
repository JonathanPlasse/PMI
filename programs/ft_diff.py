#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:35:55 2018

@author: ROHR Julien, ROUSSEL Loïc, PLASSE Jonathan, NAILI Kamel
"""
import numpy as np
from scipy.fftpack import fft2,fftshift
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from aperture_func import load_map,x_sine_transmittance,y_sine_transmittance

z=1
lamb=500e-9
a=1

def ft_diffpattern(Map) :
    nbpx=Map.shape[0]
    Imap=fftshift(fft2(Map))
    diffsize=(nbpx-1)/2/a*lamb*z
    diffaxis = np.array([-diffsize,diffsize,-diffsize,diffsize])
    plt.figure()
    plt.imshow(abs(Imap),cmap=cm.gray,extent=diffaxis)
    plt.colorbar()
    plt.show()
    
#%%Test
if __name__=="__main__" :
    Map=load_map("../resources/apertures/square_test.png")
    Map=y_sine_transmittance(x_sine_transmittance(Map))
    ft_diffpattern(Map)
    plt.figure()
    apaxis=np.array([-a,a,-a,a])
    plt.imshow(Map,cmap=cm.gray,extent=apaxis)
    plt.show()