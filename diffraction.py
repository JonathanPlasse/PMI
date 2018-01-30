#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Fonction pour la TF 2D
from scipy.fftpack import fft2,fftshift
#Module pour l'affichage
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#Module pour le calcul
import numpy as np

#Déclaration des subplots
f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

#Constantes de modélisation
a=1 #m
z=100 #m
lamb=2 #m
k=2*np.pi/lamb

ech=200 #Nombre de pixels de côté des plans
size=a*20 #Demi-taille du plan de diffraction
isize = (ech-1)/4/size*lamb*z #Demi-taille de l'écran

X = np.linspace(-size,size,ech) #Abscisses du plan de diffraction
Y = np.linspace(-size,size,ech) #Ordonnées du plan de diffraction

x = np.linspace(-isize,isize,ech) #Abscisses de l'écran
y = np.linspace(-isize,isize,ech) #Ordonnées de l'écran

oaxis = np.array([-size,size,-size,size]) #Valeurs min/max des axes du plan de diffraction
iaxis = np.array([-isize,isize,-isize,isize]) # Valeurs min/max des axes de l'écran

#Distribution de l'amplitude lumineuse sur le plan de diffraction
def distribc(x,y):
    if abs(x)<=a and abs(y)<=a:
        return 1
    else:
        return 0

#Fonction théorique de la figure de diffraction
def fc(x,y):
    return np.sinc(2*x*a/(z*lamb))**2*np.sinc(2*y*a/(z*lamb))**2

#Fonction générant la figure de diffraction théorique
def Ic():
    return np.array([[fc(x[i],y[j]) for j in range(ech)] for i in range(ech)])


print("echelle genere")

#Génération des figures de diffractions obtenus avec la fft et théoriquement
D=np.array([[distribc(X[i],Y[j]) for j in range(ech)] for i in range(ech)])
I=abs(fftshift(fft2(D)))**2

Iana=Ic()

#Affichage
print("carre genere")
ax1.imshow(D, extent=oaxis)
ax2.imshow(I, extent=iaxis)
ax3.imshow(Iana, extent=iaxis)
ax1.axis(oaxis)
ax2.axis(iaxis)
ax3.axis(iaxis)

#Normalisation des figures de diffraction
In=I/np.linalg.norm(I)
Ianan=Iana/np.linalg.norm(Iana)

plt.imshow((In-Ianan)/Ianan, extent=iaxis)
plt.colorbar()

plt.show()
