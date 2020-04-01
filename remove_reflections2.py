import cv2
import numpy as np
import numpy.linalg as la
import os
from pathlib import Path
from os import walk

ABSOLUTE_PATH = Path.cwd() / 'test'
print(ABSOLUTE_PATH)

files = []
for (dirpath, dirnames, filenames) in walk(ABSOLUTE_PATH):
    files.extend(filenames)
    break    

imgs= []

#read input
for f in files:
    if 'jpg' in f and 'background' not in f:
        imgs.append(cv2.imread(str(ABSOLUTE_PATH) + '/' + f))


#generate output
h, w = imgs[0].shape[:2]
img_out = np.zeros((h, w, 3), np.uint8)
num = len(imgs)

for i in range(h): 
    for j in range(w):
        r = g = b = 0
        
        for img in imgs:
            r = r + img[i, j][0]
            g = g + img[i, j][1]
            b = b + img[i, j][2]
#            print "original: ", img[i, j]

        img_out[i, j] = [r/num, g/num, b/num]        
#        print "background: ", img_out[i, j]

cv2.imwrite('backgroud_algo1.png', img_out)