import matplotlib.pyplot as plt

from skimage import io
from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms
from pathlib import Path
from os import walk
import cv2
import math 

ABSOLUTE_PATH = Path.cwd() 
print(ABSOLUTE_PATH)

files = []
for (dirpath, dirnames, filenames) in walk(str(ABSOLUTE_PATH) + '/images/rgb/test/'):
    files.extend(filenames)
    break    


for f in files:

	print(str(ABSOLUTE_PATH) + '/images/rgb/test/' + f)
	image = cv2.imread(str(ABSOLUTE_PATH) + '/images/rgb/test/' + f)

	b, g, r = cv2.split(image)

	o2 = ((r+g)-2*b)/math.sqrt(6)

	cv2.imwrite(str(ABSOLUTE_PATH) + '/images/opposite_o2/test/' + f, o2)
