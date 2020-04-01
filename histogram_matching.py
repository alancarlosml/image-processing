import matplotlib.pyplot as plt

from skimage import io
from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms
from pathlib import Path
from os import walk

ABSOLUTE_PATH = Path.cwd() 
print(ABSOLUTE_PATH)

reference = io.imread(str(ABSOLUTE_PATH) + '/images/rgb/test/102578_20150518001044021.jpg')

files = []
for (dirpath, dirnames, filenames) in walk(str(ABSOLUTE_PATH) + '/images/rgb/test/'):
    files.extend(filenames)
    break    


for f in files:

	print(str(ABSOLUTE_PATH) + '/images/rgb/test/' + f)
	image = io.imread(str(ABSOLUTE_PATH) + '/images/rgb/test/' + f)

	matched = match_histograms(image, reference, multichannel=True)

	io.imsave(str(ABSOLUTE_PATH) + '/images/histogram_matching/test/' + f, matched)
