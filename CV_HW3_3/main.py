import numpy as np
import random
from PIL import Image
from matplotlib import pyplot as plt
import cv2
numpydata = np.array(Image.open('bird.png'))

#marahel ijad noise
noiseN = 10000
for i in range(noiseN):
    x = random.randint(0, numpydata.shape[1]-1)
    y = random.randint(0, numpydata.shape[0]-1)
    numpydata[y][x] = 0
    x = random.randint(0, numpydata.shape[1]-1)
    y = random.randint(0, numpydata.shape[0]-1)
    numpydata[y][x] = 255
img = Image.fromarray(numpydata)

#bordan aks be hoze ferequance
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
magNPArr = np.array(magnitude_spectrum)

#filter median
medianFilter = cv2.medianBlur(numpydata,5)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('noise Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(medianFilter, cmap = 'gray')
plt.title('result'), plt.xticks([]), plt.yticks([])
plt.show()





