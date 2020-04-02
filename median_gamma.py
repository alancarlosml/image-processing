from pathlib import Path
from os import walk
import numpy as np 
import cv2

ABSOLUTE_PATH = Path.cwd() 
print(ABSOLUTE_PATH)

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

files = []
for (dirpath, dirnames, filenames) in walk('F:/Alan/Documentos/Doutorado/Retina/images/rgb/test/'):
    files.extend(filenames)
    break    


for f in files:

	print('F:/Alan/Documentos/Doutorado/Retina/images/rgb/test/' + f)
	image = cv2.imread('F:/Alan/Documentos/Doutorado/Retina/images/rgb/test/' + f)
	# convert the YUV image back to RGB format
	img_output = adjust_gamma(image, 0.5)
	img_output = cv2.medianBlur(img_output, 5)

	cv2.imwrite('F:/Alan/Documentos/Doutorado/Retina/images/median_gamma/test/' + f, img_output)
