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

import numpy as np
import scipy as sp
from scipy import ndimage
from numpy import ndarray


##f = misc.face()

##plt.imshow(f)

##n = 10
##l = 256
##im = np.zeros((l, l))
##points = l*np.random.random((2, n**2))
##im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
##im = ndimage.gaussian_filter(im, sigma=l/(4.*n))
##mask = im > im.mean()

import matplotlib.image as mpimg
import os
#import matplotlib.pyplot as mpplt
import matplotlib.pyplot as plt
#import plotly

os.chdir("\Users\Libby\Documents\Spring 2017\Comp_Methods")

im = mpimg.imread("Img2016-09-29 15.01.40.JPG")

#from Andy's code
#mask=logical(imread(maskname))+0

mask = (im > im.mean()).astype(np.float)

label_im, nb_labels = ndimage.label(mask)
#nb_labels # how many regions?
#16
plt.imshow(label_im)

#from PIL import Image
#image_file = "Img2016-09-29 15.01.40.JPG"
#i = Image.open(image_file).convert('L')
#a = np.array(i.convert('L'))
#a.shape
#b = a.sum(0)
#b.shape
#histo = image.histogram()
#histo_string = ''

#for i in histo:
 #   histo_string += str(i) + "\n"
    
#print(histo_string)

#plt.imshow(b.shape)
#plt.imshow(hist)