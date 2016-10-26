%matplotlib inline
import scipy as sp
import scipy.ndimage as nd
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

img = nd.imread('results_L3.jpg', mode = 'L')
imgplot = plt.imshow(img, cmap='Greys_r')