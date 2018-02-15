#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:41:55 2018

@author: ROHR Julien, ROUSSEL Loïc, PLASSE Jonathan, NAILI Kamel
"""

import matplotlib
matplotlib.use('TkAgg')     #necessary to show plots at the same time as the GUI

import sys

import tkinter as tk
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkmb
import tkinter.simpledialog as tksd

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from imageio import imsave
from aperture_func import load_map,x_sine_transmittance,y_sine_transmittance
from ft_diff import ft_diffpattern


#%%Variables
z=1  #distance between the aperture plane and the screen where the diffraction pattern shows in meters
lamb=500e-9 #wavelength in meters
a=1 #sidelength of the square image containing the aperture in meters
nbpx=201

#%%Window creation    
window=tk.Tk() 

#%%Dividing window space
ApeOptionsFrame=tk.LabelFrame(window, text="Aperture options")
ApeOptionsFrame.pack(fill="both", expand="yes")

ShowOptionsFrame=tk.LabelFrame(window, text="Show options")
ShowOptionsFrame.pack(fill="both", expand="yes")

DimOptionsFrame=tk.LabelFrame(window, text="Dimensions (click buttons to update)")
DimOptionsFrame.pack(fill="both", expand="yes")

#%%Aperture options callbacks
#Square aperture
def ESquare(x,y,sidelength) :
    """Returns 1 if the coordinates given are inside of the square centered on 0 and which sidelength
    is passed as an argument, 0 otherwise."""
    if abs(x)<=sidelength/2 and abs(y)<=sidelength/2 :
        return(1)
    else :
        return(0)

def SquareApertureCallBack() :
    global nbpx
    global a
    filepath=tkfd.asksaveasfile(defaultextension=".png")
    if filepath.name :
        square=np.zeros([nbpx,nbpx])
        squaresidelength=tksd.askinteger(title="Aperture size", prompt="Enter the size of the aperture")
        x=np.linspace(-nbpx,nbpx,nbpx) #used to 'transform' image array indices into usual coordinates, with the origin at the center of the image
        y=np.linspace(-nbpx,nbpx,nbpx) #used to 'transform' image array indices into usual coordinates, with the origin at the center of the image
        for i in range(nbpx) :
            for j in range(nbpx) :
                square[i][j]=ESquare(x[i],y[j],squaresidelength)
        apertureaxis = np.array([-a,a,-a,a])
        plt.figure()
        plt.imshow(square,cmap=cm.gray,extent=apertureaxis)
        yn=tkmb.askyesno(title="Save?", message="Do you want to save this figure ?")
        if yn :
            squareimg=np.zeros([nbpx,nbpx,3],dtype=np.uint8)
            for i in range(nbpx) :
                for j in range(nbpx) :
                    for k in range(3) :
                       squareimg[i][j][k]=int(square[i][j]*255)
            imsave(filepath.name,squareimg)
        plt.close()
        
#Rectangle aperture
def ERect(x,y,sidea,sideb) :
    """Returns 1 if the coordinates given are inside of the rectangle centered on 0 and which sidelengths
    are passed as arguments, 0 otherwise."""
    if abs(x)<=sidea/2 and abs(y)<=sideb/2 :
        return(1)
    else :
        return(0)

def RectApertureCallBack() :
    global nbpx
    global a
    filepath=tkfd.asksaveasfile(defaultextension=".png")
    if filepath.name :
        rectangle=np.zeros([nbpx,nbpx])
        rectsidea=tksd.askinteger(title="Aperture size", prompt="Enter the height of the aperture")
        rectsideb=tksd.askinteger(title="Aperture size", prompt="Enter the width of the aperture")
        x=np.linspace(-nbpx,nbpx,nbpx) #used to 'transform' image array indices into usual coordinates, with the origin at the center of the image
        y=np.linspace(-nbpx,nbpx,nbpx) #used to 'transform' image array indices into usual coordinates, with the origin at the center of the image
        for i in range(nbpx) :
            for j in range(nbpx) :
                rectangle[i][j]=ERect(x[i],y[j],rectsidea,rectsideb)
        apertureaxis = np.array([-a,a,-a,a])
        plt.figure()
        plt.imshow(rectangle,cmap=cm.gray,extent=apertureaxis)
        yn=tkmb.askyesno(title="Save?", message="Do you want to save this figure ?")
        if yn :
            rectimg=np.zeros([nbpx,nbpx,3],dtype=np.uint8)
            for i in range(nbpx) :
                for j in range(nbpx) :
                    for k in range(3) :
                        rectimg[i][j][k]=int(rectangle[i][j]*255)
            imsave(filepath.name,rectimg)
        plt.close()
    
#Circular aperture
def ECirc(x,y,r) :
    """Returns 1 if the coordinates given are inside of the circle centered on 0 and which radius
    is passed as an argument, 0 otherwise."""
    if x**2+y**2<=r**2 :
        return(1)
    else :
        return(0)

def CircleApertureCallBack() :
    global nbpx
    global a
    filepath=tkfd.asksaveasfile(defaultextension=".png")
    if filepath.name :
        circle=np.zeros([nbpx,nbpx])
        radius=tksd.askinteger(title="Aperture size", prompt="Enter the radius of the aperture")
        x=np.linspace(-nbpx,nbpx,nbpx) #used to 'transform' image array indices into usual coordinates, with the origin at the center of the image
        y=np.linspace(-nbpx,nbpx,nbpx) #used to 'transform' image array indices into usual coordinates, with the origin at the center of the image
        for i in range(nbpx) :
            for j in range(nbpx) :
                circle[i][j]=ECirc(x[i],y[j],radius)
        apertureaxis = np.array([-a,a,-a,a])
        plt.figure()
        plt.imshow(circle,cmap=cm.gray,extent=apertureaxis)
        yn=tkmb.askyesno(title="Save?", message="Do you want to save this figure ?")
        if yn :
            circleimg=np.zeros([nbpx,nbpx,3],dtype=np.uint8)
            for i in range(nbpx) :
                for j in range(nbpx) :
                    for k in range(3) :
                        circleimg[i][j][k]=int(circle[i][j]*255)
            imsave(filepath.name,circleimg)
        plt.close()
    
#Asking for aperture imagefile
def LoadImgCallBack() :
    """Called when the 'Load Aperture' Button is clicked. Allows user to select a .png file."""
    global nbpx
    global Amap
    filepath=tkfd.askopenfilename(title="Select an image",filetypes=[('png files','.png')])
    Amap=load_map(filepath)
    nbpx=Amap.shape[0]

#Modulate transmittance
def ModTransmittanceCallBack() :
    """Called when the 'Mod Transmittance' Button is clicked. Allows user to modify the transmittance of the aperture
    on either vertical or horizontal axis."""
    global Amap
    yn=tkmb.askyesno(title="Modulate ?", message="Do you want to modulate transmittance on the vertical axis ?")
    if yn :
        Amap=y_sine_transmittance(Amap)
    yn=tkmb.askyesno(title="Modulate ?", message="Do you want to modulate transmittance on the horizontal axis ?")
    if yn :
        Amap=x_sine_transmittance(Amap)

#%%Show options callbacks
#Show diffraction figure
def ShowFTDiffCallBack() :
    """Called when the 'Show FT Diffraction Pattern' Button is clicked. 
    Displays diffraction pattern of current aperture with matplotlib."""
    global a
    global lamb
    global z
    global Amap
    ft_diffpattern(Amap)
    
#Close diffraction figure
def CloseWindowCallBack() :
    """Called when the 'Close Current Window' Button is clicked. Closes the current matplotlib figure."""
    plt.close()

#Show aperture
def ShowApertureCallBack():
    """Called when the 'Show Aperture' Button is clicked. Displays aperture with matplotlib."""
    global a
    global Amap
    apertureaxis = np.array([-a,a,-a,a])
    plt.figure()
    plt.imshow(Amap,cmap=cm.gray,extent=apertureaxis)
    plt.show()
    
def ShowVarCallBack() :
    """Called when the 'Show Variables' Button is clicked. 
    Displays the wavelength, distance to screen, image size in meters and image size in pixels."""
    global lamb,a,z,nbpx
    VarTxt="Wavelength : "+str(lamb)+"\nSize in meters : "+str(a)+"\nDistance to screen : "+str(z)+"\nSize in pixels : "+str(nbpx)
    tkmb.showinfo(title='Variables', message=VarTxt)

#%%Variables input callbacks
#Update wavelength according to user input
def Updatelamb() :
    """Updates the value of 'lamb' with the value from the LambEntry widget"""
    global lamb
    lamb=float(LambEntry.get())
    print("Wavelength in meters :",lamb)

#Update image size according to user input
def Updatea() :
    """Updates the value of 'a' with the value from the ImageSizeEntry widget"""
    global a
    a=float(ImageSizeEntry.get())
    print("Size in meters :",a)

#Update distance to screen according to user input
def Updatez() :
    """Updates the value of 'z' with the value from the Dist2ScreenEntry widget"""
    global z
    z=float(Dist2ScreenEntry.get())
    print("Distance to screen :",z)

#Update size of image in pixels (only for image creation)
def Updatenbpx() :
    """Updates the value of 'nbpx' with the value from the NbPxEntry widget"""
    global nbpx
    nbpx=int(NbPxEntry.get())
    print("Size in pixels :",nbpx)
    
#%%GUI widgets
#Aperture options
SquareButton=tk.Button(ApeOptionsFrame, text ='Square Aperture', command=SquareApertureCallBack).pack(fill="both")
RectangleButton=tk.Button(ApeOptionsFrame, text ='Rectangle Aperture', command=RectApertureCallBack).pack(fill="both")
CircleButton=tk.Button(ApeOptionsFrame, text ='Circular Aperture', command=CircleApertureCallBack).pack(fill="both")
LoadButton=tk.Button(ApeOptionsFrame, text ='Load Aperture', command=LoadImgCallBack).pack(fill="both")
ModTransmittanceButton=tk.Button(ApeOptionsFrame, text = 'Modulate transmittance', command=ModTransmittanceCallBack).pack(fill="both")
#Show Options
PreviewApertureButton=tk.Button(ShowOptionsFrame, text='Show Aperture', command=ShowApertureCallBack).pack(fill="both")
ShowFTDiffButton=tk.Button(ShowOptionsFrame, text ='Show FT Diffraction Pattern', command=ShowFTDiffCallBack).pack(fill="both")
CloseWindowButton=tk.Button(ShowOptionsFrame, text ='Close Current Window', command=CloseWindowCallBack).pack(fill="both")
ShowVarButton=tk.Button(ShowOptionsFrame, text ='Show variables', command=ShowVarCallBack).pack(fill="both")
#Dimensions options
LambButton=tk.Button(DimOptionsFrame, text ='Wavelength (m)', command=Updatelamb).pack(fill="both")
LambEntry=tk.Entry(DimOptionsFrame)
LambEntry.pack(fill="both")
ImageSizeButton=tk.Button(DimOptionsFrame, text ='Image real size (m)', command=Updatea).pack(fill="both")
ImageSizeEntry=tk.Entry(DimOptionsFrame)
ImageSizeEntry.pack(fill="both")
Dist2ScreenButton=tk.Button(DimOptionsFrame, text ='Distance between aperture and screen (m)', command=Updatez).pack(fill="both")
Dist2ScreenEntry=tk.Entry(DimOptionsFrame)
Dist2ScreenEntry.pack(fill="both")
NbPxButton=tk.Button(DimOptionsFrame, text ='Size of image in pixels (for creation)', command=Updatenbpx).pack(fill="both")
NbPxEntry=tk.Entry(DimOptionsFrame)
NbPxEntry.pack(fill="both")

#%%Exit GUI
def ExitButtonCallBack():
    plt.close('all') #close all plt plots
    window.destroy() #quit tkinter interface
    sys.exit() #force quit if the process freezes
    
ExitButton=tk.Button(window, text ='Close all plots and exit',fg='red', command=ExitButtonCallBack).pack(side=tk.BOTTOM,fill="both")

#%%ALWAYS AT THE BOTTOM
window.mainloop()