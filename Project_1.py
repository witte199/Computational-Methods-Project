# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:43:55 2017

@author: Libby
"""

#Make python work like matlab:
    #http://matplotlib.org/users/pyplot_tutorial.html

#1_channelmap -> Create binary maps of "wet" and "dry"

#Channel map variables
    #learn how to create variables in python
        #in channelmap_vars.m
        
##Use functions and classes to go through all photos, save them somewhere else 

#2_overlap ->
#3_changerate ->
#4_rework ->
#5_plotting ->

#CHANNEL MAP

from PIL import Image

import numpy as np
import scipy as sp
from scipy import ndimage
#from numpy import ndarray


import shutil
import matplotlib.image as mpimg
import os
import matplotlib
import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter




##define directory for accessing image
#os.chdir("https://github.com/witte199/Computational-Methods-Project")



#Open directory
#a = open("C:\Users\Libby\Desktop\Binary_Images")

##allows all photos in directory to be turned into binary images
for x in range(10):
    i=0

    #identify files
    filename = 'Img' + str(x+1) + ".jpg"

    ##define image
    im = mpimg.imread(filename)
    #im = Image.open(filename)
    
    ##Identify shape of image
    print im.shape

    ##Identify size of image
    print im.size

    ##create pixelized image out of original image
    mask = (im > im.mean()).astype(np.float)
    label_im, nb_labels = ndimage.label(mask)

    ##plot pixelized image
    plt.imshow(label_im)

    ##Separate "River" from "Not river"
    hsv = matplotlib.colors.rgb_to_hsv(im)
    river = hsv[:,:,0]-hsv[:,:,1] <-.5
    river = hsv[:,:,1] > .55

    ##Save data in folder
    np.savetxt(str(filename) + ".txt", river, fmt = '%d')

    
