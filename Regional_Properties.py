import matplotlib.pyplot as plt # To plot the results
import os # To allow for operating systems
from skimage import io, color, measure, segmentation, morphology
from skimage.filters import threshold_otsu

# Load image and convert to grayscale
os.chdir('C:/Users/bencr/OneDrive/Pictures')
image = io.imread('raisins.jpg')  
grey_image = color.rgb2gray(image)

# Thresholding to convert the image to binary
threshold = threshold_otsu(grey_image)
binary_image = grey_image < threshold

# Remove small objects (noise) and objects touching the boundary
binary_image = morphology.remove_small_objects(binary_image, min_size=500)
clear_image = segmentation.clear_border(binary_image)

# Label connected components (raisins)
labelled_raisins = measure.label(clear_image)

# Measure region properties
raisin_regions = measure.regionprops(labelled_raisins)

# Filter out regions touching the boundary
filtered_raisin_regions = [region for region in raisin_regions if not region.bbox[0] == 0 and not region.bbox[1] == 0 and not region.bbox[2] == labelled_raisins.shape[0] and not region.bbox[3] == labelled_raisins.shape[1]]

# Count the number of raisins (excluding boundary objects)
no_raisins = len(filtered_raisin_regions)
print(f"Total number of raisins (excluding boundary): {no_raisins}")

# Display the original and labelled images
figure, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image)
axes[0].set_title("Original Image")
axes[1].imshow(labelled_raisins, cmap='grey')
axes[1].set_title("Labelled Raisins")
plt.show()
