import cv2
import numpy as np
import numpy.linalg as la
import os
from pathlib import Path
from os import walk
import numpy
import cv2

ABSOLUTE_PATH = Path.cwd() / 'test'
print(ABSOLUTE_PATH)

files = []
for (dirpath, dirnames, filenames) in walk(ABSOLUTE_PATH):
    files.extend(filenames)
    break    

x = 1396
y = 958
w = 100
thresh = 0.9

#read input
for f in files:
    if 'jpg' in f and 'background' not in f:
        im = cv2.imread(str(ABSOLUTE_PATH) + '/' + f, 0)

        print(im.shape)

        # generate binary image mask - dilated circles around the saturated bright spots at the center
        temp = im[y-w:y+w, x-w:x+w,1]  # single channel
        ret, temp_mask = cv2.threshold(temp, thresh*256, 255, cv2.THRESH_BINARY)
        kernel = numpy.ones((25,25), 'uint8')
        temp_mask = cv2.dilate(temp_mask, kernel)

        # perform the inpainting...
        im[y-w:y+w, x-w:x+w,:] = cv2.inpaint(im[y-w:y+w, x-w:x+w,:], temp_mask, 1, cv2.INPAINT_TELEA)

        # return file
        cv2.imwrite(str(ABSOLUTE_PATH) + '/reflexao/' + f, im)