# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:46:46 2024
@author: bencr
"""
from skimage import data, io, filters
from skimage import transform
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
sobel_image = filters.sobel(noisy_img) 
canny_image = feature.canny(noisy_img, sigma=0.75)
figure, axe = plt.subplots(ncols=2,figsize=(18,6))
axe[0] = plt.subplot(1,2,1) 
axe[1] = plt.subplot(1,2,2, sharex = axe[0], sharey = axe[0])
axe[0].imshow(sobel_image, cmap=plt.cm.gray)
axe[0].set_title('Sobel Edge Image')
axe[0].axis('off')
axe[1].imshow(canny_image, cmap=plt.cm.gray)
axe[1].set_title('Canny Edge Image')
axe[1].axis('off')
figure.tight_layout() 
plt.savefig(os.path.join('C:/Users/bencr/OneDrive/Pictures/Screenshots', 'output_photo_2.jpg'))
plt.show() 
