import math
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bird.png',0)
imgCopy = cv2.imread('bird.png',0)
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        img[i][j] = math.sin(0.1*i) + math.sin(0.2*i) + math.cos(0.4*i) + \
                    math.sin(math.sqrt(i*i + j*j) * 0.15) + math.sin(math.sqrt(i*i + j*j) * 0.35)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
phase_spectrum = np.angle(fshift)
plt.subplot(232),plt.imshow(imgCopy, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(img, cmap = 'gray')
plt.title('Changed Image'), plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(phase_spectrum, cmap = 'gray')
plt.title('Phase'), plt.xticks([]), plt.yticks([])
plt.show()
