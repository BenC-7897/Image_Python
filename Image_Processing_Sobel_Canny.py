from skimage import data, io, filters
from skimage import transform
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

# Display the resized image (optional visualization step)
io.imshow(resized_img)

# Convert the resized image to grayscale
greyscale_img = rgb2gray(resized_img)

# Display the grayscale image (optional visualization step)
io.imshow(greyscale_img)

# Print the shape and statistics of the grayscale image
print("Shape", greyscale_img.shape)
print("Minimum/Maximum/Mean:", greyscale_img.min(), greyscale_img.max(), greyscale_img.mean())

# Add Gaussian noise to the grayscale image
noisy_img = random_noise(greyscale_img, mode='gaussian', mean=0.0, var=0.01)

# Apply the Sobel filter to detect edges in the noisy image
sobel_image = filters.sobel(noisy_img)

# Apply the Canny edge detection method to the noisy image
canny_image = feature.canny(noisy_img, sigma=0.75)

# Create a figure with two subplots for displaying the edge-detected images
figure, axe = plt.subplots(ncols=2, figsize=(18, 6))

# Define the first subplot for the Sobel edge-detected image
axe[0] = plt.subplot(1, 2, 1)

# Define the second subplot for the Canny edge-detected image, sharing axes with the first
axe[1] = plt.subplot(1, 2, 2, sharex=axe[0], sharey=axe[0])

# Display the Sobel edge-detected image in the first subplot
axe[0].imshow(sobel_image, cmap=plt.cm.gray)
axe[0].set_title('Sobel Edge Image')
axe[0].axis('off')  # Turn off the axes for a cleaner display

# Display the Canny edge-detected image in the second subplot
axe[1].imshow(canny_image, cmap=plt.cm.gray)
axe[1].set_title('Canny Edge Image')
axe[1].axis('off')  # Turn off the axes for a cleaner display

# Adjust the layout of the figure for better spacing
figure.tight_layout()

# Save the resulting figure as an image file in the specified path
plt.savefig(os.path.join('C:/Users/bencr/OneDrive/Pictures/Screenshots', 'output_photo_2.jpg'))

# Show the plotted images
plt.show()
