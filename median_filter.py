from pathlib import Path
from os import walk
import cv2

ABSOLUTE_PATH = Path.cwd() 
print(ABSOLUTE_PATH)

files = []
for (dirpath, dirnames, filenames) in walk('F:/Alan/Documentos/Doutorado/Retina/images/rgb/val/'):
    files.extend(filenames)
    break    


for f in files:

	print('F:/Alan/Documentos/Doutorado/Retina/images/rgb/val/' + f)
	image = cv2.imread('F:/Alan/Documentos/Doutorado/Retina/images/rgb/val/' + f)
	# convert the YUV image back to RGB format
	img_output = cv2.medianBlur(image, 5)

	cv2.imwrite('F:/Alan/Documentos/Doutorado/Retina/images/median_filter/val/' + f, img_output)
