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
#Andy: "Use greater-than/ less-than operator"

#2_overlap ->
#3_changerate ->
#4_rework ->
#5_plotting ->

#CHANNEL MAP

from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering

from PIL import Image

import numpy as np
import scipy as sp
from scipy import ndimage
#from numpy import ndarray



import matplotlib.image as mpimg
import os
#import matplotlib.pyplot as mpplt
import matplotlib.pyplot as plt
#import plotly

from scipy.ndimage import gaussian_filter




##define directory for accessing image
os.chdir("\Users\Libby\Documents\Spring 2017\Comp_Methods")

##define image
im = mpimg.imread("Img2016-09-29 15.01.40.JPG")

##plot image
plt.imshow(im)



#def color_mask(red, other):
    #red = (RGB value)
    #other = (literally any other RGB value)
    #Read pixel
    #if red :
     #   then (replace with white)
    #else:
     #  then (replace with black)
    
    
#----------- 
##create pixelized image out of original image
mask = (im > im.mean()).astype(np.float)
label_im, nb_labels = ndimage.label(mask)

##plot pixelized image
plt.imshow(label_im)

#------------

#rows = 2848
#columns = 4288
#image = [[0 for x in range(columns)] for x in range (rows)]
          for i in range(rows):
              for j in range(columns):
                  

#from skimage import data
#from skimage import filters

##Identify shape of image
print im.shape

##Identify size of image
print im.size

##Find value of pixel at orientation [10,100]
print im[10,100]





