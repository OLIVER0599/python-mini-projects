from PIL import Image as im


xx = im.open('zebr3a.jpg')

yy = im.new('L', [3 * xx.size[0], 3* xx.size[1]], 0)

xpix = xx.load()
ypix = yy.load()


for j in range(yy.size[1]):
    for i in range(yy.size[0]):
        ypix[i,j] = xpix[int(i/3), int(j/3)]

yy.save('zebraZOH.jpg')
#############################################
import numpy as np
from scipy.signal import convolve2d

f = np.array([1/3, 2/3, 1, 2/3, 1/3])
F = np.outer(f, f)

yy_array = np.array(yy, dtype=float)

Y_interp = convolve2d(yy_array, F, mode='same')

import matplotlib.pyplot as plt

plt.imshow(Y_interp, cmap='gray')
plt.title("Linearly Interpolated Image")
plt.axis('off')
plt.show()

