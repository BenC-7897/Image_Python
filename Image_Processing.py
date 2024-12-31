from skimage import data, io, filters
from skimage import io, transform
from skimage.color import rgb2gray 
import matplotlib.pyplot as plt 
import os 

# Change the working directory to the folder containing the image
os.chdir('C:/Users/bencr/OneDrive/Pictures/Screenshots')

# Load the image from the specified path
img = io.imread(os.path.join('C:/Users/bencr/OneDrive/Pictures/Screenshots', 'IMG_3069.jpg'))

# Convert the image to grayscale
grayscale = rgb2gray(img)

# Print shape and statistics of the grayscale image
print("Shape", grayscale.shape)
print("Minimum/Maximum/Mean:", grayscale.min(), grayscale.max(), grayscale.mean())

# Create a figure with two subplots for displaying the images
figures, axes = plt.subplots(ncols=2, figsize=(15, 5))

# Define the first subplot
axes[0] = plt.subplot(1, 2, 1)
# Define the second subplot and share x and y axes with the first
axes[1] = plt.subplot(1, 2, 2, sharex=axes[0], sharey=axes[0])

# Display the original colored image in the first subplot
axes[0].imshow(img, cmap=plt.cm.gray)
axes[0].set_title('Coloured Image:')
axes[0].axis('off')  # Turn off the axes for a cleaner display

# Display the grayscale image in the second subplot
axes[1].imshow(grayscale, cmap=plt.cm.gray)
axes[1].set_title('Greyscale Image:')
axes[1].axis('off')  # Turn off the axes for a cleaner display

# Adjust the layout of the figure for better spacing
figures.tight_layout()

# Show the plotted images
plt.show()
