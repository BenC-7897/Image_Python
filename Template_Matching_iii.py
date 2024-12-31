import numpy as np
import matplotlib.pyplot as plt
import os 
from skimage import io, color, feature, data  
from skimage.feature import match_template
from skimage.transform import rotate
os.chdir('C:/Users/bencr/OneDrive/Pictures')
source_img = io.imread('tie.jpg')
template_img = io.imread('template_tie.jpg')
source_grey = color.rgb2gray(source_img) 
template_grey = color.rgb2gray(template_img)
def best_match(source_image, template_image):
    best_score = -1
    best_angle = 0
    best_result = None
    for a in range(0, 360, 15):
        rotated_source = rotate(source_image, a)
        image_result = match_template(rotated_source, template_image)
        maximum_score = np.max(image_result)
        if maximum_score > best_score:
            best_score = maximum_score
            best_angle = a
            best_result = image_result 
    return best_result, best_angle
image_result, best_angle = best_match(source_grey, template_grey)
rotated_source_grey = rotate(source_grey, best_angle)
ij = np.unravel_index(np.argmax(image_result), image_result.shape)
x, y = ij[::-1]
figure, (axe1, axe2) = plt.subplots(1, 2, figsize=(10, 5))
axe1.imshow(template_grey, cmap=plt.cm.gray)
axe1.set_axis_off()
axe1.set_title('Template')
axe2.imshow(rotated_source_grey, cmap=plt.cm.gray)
axe2.set_axis_off()
axe2.set_title('Matched Image')
height, width = template_grey.shape 
rectangle = plt.Rectangle((x,y), width, height, edgecolor='r', facecolor='none')
axe2.add_patch(rectangle)
plt.figtext(0.5, 0.01, f'Best matching angle: {best_angle} degrees', ha='center', fontsize=12, color='black')
plt.show() 

