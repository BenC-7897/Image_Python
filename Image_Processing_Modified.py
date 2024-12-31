from skimage import data, io, filters
from skimage import io, transform
from skimage.color import rgb2gray 
from skimage.util import random_noise 
from skimage import feature
import matplotlib.pyplot as plt 
import os 

# Change the working directory to the folder containing the image
os.chdir('C:/Users/bencr/OneDrive/Pictures/Screenshots')

# Load the image from the specified path
img = io.imread(os.path.join('C:/Users/bencr/OneDrive/Pictures/Screenshots', 'IMG_3069.jpg'))

# Define new dimensions for resizing the image
dimension = (512, 512)

# Resize the image to the specified dimensions
resized_img = transform.resize(img, dimension)

# Display the resized image (will display in a new window when executed)
io.imshow(resized_img)

# Convert the resized image to grayscale
greyscale_img = rgb2gray(resized_img)

# Display the grayscale image
io.imshow(greyscale_img)

# Print shape and statistics of the grayscale image
print("Shape", greyscale_img.shape)
print("Minimum/Maximum/Mean:", greyscale_img.min(), greyscale_img.max(), greyscale_img.mean())

# Add Gaussian noise to the grayscale image
noisy_img = random_noise(greyscale_img, mode='gaussian', mean=0.0, var=0.01)

# Create a figure with three subplots for displaying the images
figures, axes = plt.subplots(ncols=3, figsize=(24, 9))

# Define the first subplot for the resized image
axes[0] = plt.subplot(1, 3, 1)
# Define the second subplot for the grayscale image
axes[1] = plt.subplot(1, 3, 2)
# Define the third subplot for the noisy image, sharing x and y axes with the first
axes[2] = plt.subplot(1, 3, 3, sharex=axes[0], sharey=axes[0])

# Display the resized image in the first subplot
axes[0].imshow(resized_img, cmap=plt.cm.gray)
axes[0].set_title('Resized Image')
axes[0].axis('off')  # Turn off the axes for a cleaner display

# Display the grayscale image in the second subplot
axes[1].imshow(greyscale_img, cmap=plt.cm.gray)
axes[1].set_title('Grayscale Image')
axes[1].axis('off')  # Turn off the axes for a cleaner display

# Display the noisy image in the third subplot
axes[2].imshow(noisy_img, cmap=plt.cm.gray)
axes[2].set_title('Noisy Image')
axes[2].axis('off')  # Turn off the axes for a cleaner display

# Adjust the layout of the figure for better spacing
figures.tight_layout()

# Show the plotted images
plt.show()
