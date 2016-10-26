import scipy as sp
import scipy.ndimage
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

img = mpimg.imread('results_L3.jpg')
imgplot = plt.imshow(img)