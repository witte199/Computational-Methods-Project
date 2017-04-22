# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 23:13:11 2017

@author: Libby
"""

#This is Project 1.2

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
##identify files
filename ='Img' + str(x+1) + ".jpg"

class project_1(object):
    def __init__(self, name):
        self.name = name
    ##convert files to binary text files
    def ficonvert(object):
        for x in range(10):
            ##identify files within loop
            filename = 'Img' + str(x+1) + ".jpg"
            ##define image
            im = mpimg.imread(filename)
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

        
newlist = project_1("Img1_Img10")
newlist.ficonvert()    
