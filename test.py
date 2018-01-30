#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.fftpack import fft,fftshift,fftfreq
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

a=1 #m
z=100 #m
lamb=2 #m
k=2*np.pi/lamb
A0=1

def distrib(x):
    if abs(x)<=a:
        return 1
    else:
        return 0

size=a*20
ech=1000
xi = np.linspace(-size,size,ech)

D=np.array([distrib(xi[i]) for i in range(ech)])
I=fftshift(fft(D))
F=np.linspace(-(ech-1)/4/size,(ech-1)/4/size,ech)

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(xi,D)
ax2.plot(F*z*lamb,abs(I))
plt.show()
