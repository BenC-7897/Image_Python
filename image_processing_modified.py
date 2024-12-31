# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:18:23 2024
@author: bencr
"""
from skimage import data, io, filters
from skimage import io, transform
from skimage.color import rgb2gray 
from skimage.util import random_noise 
from skimage import feature
import matplotlib.pyplot as plt 
import os 
os.chdir('C:/Users/bencr/OneDrive/Pictures/Screenshots')
img = io.imread(os.path.join('C:/Users/bencr/OneDrive/Pictures/Screenshots', 'IMG_3069.jpg')) 
dimension = (512,512) 
resized_img = transform.resize(img, dimension)  
io.imshow(resized_img) 
greyscale_img = rgb2gray(resized_img)
io.imshow(greyscale_img)
print("Shape", greyscale_img.shape)
print("Minimum/Maximum/Mean:", greyscale_img.min(), greyscale_img.max(), greyscale_img.mean())
noisy_img = random_noise(greyscale_img, mode = 'gaussian', mean = 0.0, var = 0.01)
figures, axes = plt.subplots(ncols=3, figsize=(24, 9))
axes[0] = plt.subplot(1,3,1) 
axes[1] = plt.subplot(1,3,2) 
axes[2] = plt.subplot(1,3,3, sharex = axes[0], sharey = axes[0])
axes[0].imshow(resized_img, cmap=plt.cm.gray) 
axes[0].set_title('Resized Image')
axes[0].axis('off')
axes[1].imshow(greyscale_img, cmap=plt.cm.gray)
axes[1].set_title('Grayscale Image')
axes[1].axis('off')
axes[2].imshow(noisy_img, cmap=plt.cm.gray)
axes[2].set_title('Noisy Image')
axes[2].axis('off') 
figures.tight_layout() 
plt.show() 
