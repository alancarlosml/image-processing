from pylab import *
import cv2
import os, sys

image_in = cv2.cvtColor(cv2.imread("102565_20150519001037013.jpg"), cv2.COLOR_BGR2RGB); # Load the glared image
h, s, v = cv2.split(cv2.cvtColor(image_in, cv2.COLOR_RGB2HSV)) # split into HSV components

'''
subplot(1,4,1); _imshow(image_in, "original")
subplot(1,4,2); _imshow(h, "Hue")
subplot(1,4,3); _imshow(s, "Saturation")
subplot(1,4,4); _imshow(v, "Brightness")
'''


nonSat = s < 180 # Find all pixels that are not very saturated

# Slightly decrease the area of the non-satuared pixels by a erosion operation.
disk = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
nonSat = cv2.erode(nonSat.astype(np.uint8), disk)

# Set all brightness values, where the pixels are still saturated to 0.
v2 = v.copy()
v2[nonSat == 0] = 0;

'''
subplot(1,3,1); _imshow(nonSat, "s > 180")
subplot(1,3,2); _imshow(v, "Original\nBrightness")
subplot(1,3,3); _imshow(v2, "Masked\nBrightness")
'''
'''
subplot(1,2,1); hist(v2.flatten(), bins=50);  # draw the histogram of pixel brightnesses
xlabel("Brightness value");
ylabel("Frequency");
title("Brightness histogram")
'''

glare = v2 > 200;    # filter out very bright pixels.
# Slightly increase the area for each pixel
glare = cv2.dilate(glare.astype(np.uint8), disk);  
glare = cv2.dilate(glare.astype(np.uint8), disk);
#subplot(1,2,2); _imshow(glare);
title("Glare mask");

corrected = cv2.inpaint(image_in, glare, 5, cv2.INPAINT_NS)
cv2.imwrite('teste.jpg', corrected)
'''
subplot(1,3,1); _imshow(image_in, "Original")
subplot(1,3,2); _imshow(glare, "Glare Mask")
subplot(1,3,3); _imshow(corrected, "Corrected");
'''