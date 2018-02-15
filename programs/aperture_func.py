#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:41:55 2018

@author: ROHR Julien, ROUSSEL Loïc, PLASSE Jonathan, NAILI Kamel
"""

from imageio import imread
import numpy as np

def RGBtoBW(Arr) :
    """Converts an 'Image array' using the RGB system to a binary array, 
    i.e. an array containing only ones and zeros."""
    ArrBW=np.zeros(Arr.shape[:2])
    for i in range(Arr.shape[0]) :
        for j in range(Arr.shape[1]) :
            if type(Arr[i][j])!=int :
                if np.any(Arr[i][j][0]==255) :
                    ArrBW[i][j]=1
                else :
                    ArrBW[i][j]=0
    return ArrBW
    
def load_map(filepath) :
    """Loads an image located by its filepath (given as a string) and using the .png format and converts it into an array. 
    Loads a default square aperture image if the image is not square, i.e. NxN pixels."""
    LoadArray=imread(filepath)
    if LoadArray.shape[0]!=LoadArray.shape[1] :
        print("Please use a square image, i.e. NxN pixels")
        LoadArray=imread("../resources/apertures/square_test.png")
    Map=RGBtoBW(LoadArray)
    return Map

def x_sine_transmittance(Map) :
    """Modulates the transmittance of the aperture on the horizontal axis using the absolute value of a sine function"""
    ModMap=np.zeros(Map.shape)
    x=np.linspace(-Map.shape[1],Map.shape[1],Map.shape[1])
    for i in range(Map.shape[0]) :
        for j in range(Map.shape[1]) :
            ModMap[i][j]=Map[i][j]*abs(np.sin(x[j]))
    return ModMap
            
def y_sine_transmittance(Map) :
    """Modulates the transmittance of the aperture on the vertical axis using the absolute value of a sine function"""
    ModMap=np.zeros(Map.shape)
    y=np.linspace(-Map.shape[0],Map.shape[0],Map.shape[0])
    for i in range(Map.shape[0]) :
        for j in range(Map.shape[1]) :
            ModMap[i][j]=Map[i][j]*abs(np.sin(y[i]))
    return ModMap
        
#%%Test
if __name__=="__main__" :
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    Map=load_map("../resources/apertures/square_test.png")
    plt.figure()
    plt.imshow(Map,cmap=cm.gray)
    plt.figure()
    plt.imshow(x_sine_transmittance(Map),cmap=cm.gray)
    plt.figure()
    plt.imshow(y_sine_transmittance(Map),cmap=cm.gray)
    plt.show()