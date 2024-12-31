from skimage import data, io, filters
from skimage import io, transform
from skimage.color import rgb2gray 
import matplotlib.pyplot as plt 
import os 
os.chdir('C:/Users/bencr/OneDrive/Pictures/Screenshots')
img = io.imread(os.path.join('C:/Users/bencr/OneDrive/Pictures/Screenshots', 'IMG_3069.jpg'))
grayscale = rgb2gray(img)
print("Shape", grayscale.shape)
print("Minimum/Maximum/Mean:", grayscale.min(), grayscale.max(), grayscale.mean())
figures, axes = plt.subplots(ncols=2, figsize=(15, 5))
axes[0] = plt.subplot(1,2,1) 
axes[1] = plt.subplot(1,2,2, sharex=axes[0], sharey=axes[0])
axes[0].imshow(img, cmap=plt.cm.gray)
axes[0].set_title('Coloured Image:')
axes[0].axis('off')
axes[1].imshow(grayscale, cmap=plt.cm.gray)
axes[1].set_title('Greyscale Image:')
axes[1].axis('off')
figures.tight_layout() 
plt.show() 
