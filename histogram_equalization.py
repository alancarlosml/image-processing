import matplotlib.pyplot as plt

from skimage import io
from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms
from pathlib import Path
from os import walk
import cv2

ABSOLUTE_PATH = Path.cwd() 
print(ABSOLUTE_PATH)

files = []
for (dirpath, dirnames, filenames) in walk(str(ABSOLUTE_PATH) + '/images/rgb/test/'):
    files.extend(filenames)
    break    


for f in files:

	print(str(ABSOLUTE_PATH) + '/images/rgb/test/' + f)
	image = cv2.imread(str(ABSOLUTE_PATH) + '/images/rgb/test/' + f)

	img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

	# equalize the histogram of the Y channel
	img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

	# convert the YUV image back to RGB format
	img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

	cv2.imwrite(str(ABSOLUTE_PATH) + '/images/histogram_equalization/test/' + f, img_output)
