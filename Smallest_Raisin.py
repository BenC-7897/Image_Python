import matplotlib.pyplot as plt
import os 
from skimage import io, color, measure, segmentation, morphology
from skimage.filters import threshold_otsu

# Load image and convert to grayscale
os.chdir('C:/Users/bencr/OneDrive/Pictures')
img = io.imread('raisins.jpg')  
grey_img = color.rgb2gray(img)

# Thresholding to convert the image to binary
threshold = threshold_otsu(grey_img)
binary_img = grey_img < threshold

# Remove small objects (noise) and objects touching the boundary
binary_img = morphology.remove_small_objects(binary_img, min_size=500)
clear_img = segmentation.clear_border(binary_img)

# Label connected components (raisins)
labelled = measure.label(clear_img)

# Measure region properties
regions = measure.regionprops(labelled)

# Filter out regions touching the boundary
filtered_regions = [region for region in regions if not region.bbox[0] == 0 and not region.bbox[1] == 0 and not region.bbox[2] == labelled.shape[0] and not region.bbox[3] == labelled.shape[1]]

# Find the smallest raisin
smallest_raisin = min(filtered_regions, key=lambda r: r.area)

# Highlight the smallest raisin in the image
highlighted_image = img.copy()
minr, minc, maxr, maxc = smallest_raisin.bbox
highlighted_image[minr:maxr, minc:maxc] = [255, 0, 0]  # Highlight with red color

# Display the results
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(img)
ax[0].set_title('Original Image')
ax[1].imshow(highlighted_image)
ax[1].set_title('Smallest Raisin')
plt.show()

# Print the area and centroid of the smallest raisin
print(f"Smallest raisin area: {smallest_raisin.area}")
print(f"Smallest raisin centroid: {smallest_raisin.centroid}")
