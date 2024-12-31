import matplotlib.pyplot as plt # To plot the results
import os # To allow for operating systems
from skimage import io, color, measure, segmentation, morphology # To enable object detection
from skimage.filters import threshold_otsu # To implement the otsu threshold
from scipy import ndimage # Multidimensional image processing 

# Change the directory and upload the raisins image 
os.chdir('C:/Users/bencr/OneDrive/Pictures')
original_image = io.imread('raisins.jpg')  

# Function to process the image and count raisins
def raisin_numbers (image):
    grey_image = color.rgb2gray(image)
    threshold = threshold_otsu(grey_image)
    binary_image = grey_image < threshold
    binary_image = morphology.remove_small_objects(binary_image, min_size=500)
    cleared_image = segmentation.clear_border(binary_image)
    labelled_image = measure.label(cleared_image)
    r_regions = measure.regionprops(labelled_image)
    filtered_r_regions = [region for region in r_regions if not region.bbox[0] == 0 and not region.bbox[1] == 0 and not region.bbox[2] == labelled_image.shape[0] and not region.bbox[3] == labelled_image.shape[1]]
    return len(filtered_r_regions)

# Define rotation angles
angles = [0, 45, 90, 135, 180, 225, 270, 315, 360]

# Perform the experiment
raisin_counts = []
for angle in angles:
    rotated_image = ndimage.rotate(original_image, angle, reshape=False)
    count = raisin_numbers(rotated_image)
    raisin_counts.append(count)
    print(f"Total number of raisins at {angle}°: {count}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(angles, raisin_counts, marker='o')
plt.title('Raisin Count vs. Rotation Angle')
plt.xlabel('Rotation Angle (°)')
plt.ylabel('Raisin Count')
plt.grid(True)
plt.show()
