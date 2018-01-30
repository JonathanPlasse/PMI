#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from scipy import misc

def readPicture(pictureName):
    """Converts 'Image array' to binary array"""
    return misc.imread(pictureName)[:,:,0]/255

def savePicture(pictureName,D):
    """Converts 'Image array' to binary array"""
    D*=255
    P=[[[D[i,j],D[i,j],D[i,j]] for j in range(D.shape[1])] for i in range(D.shape[0])]
    misc.imsave(pictureName,P)
