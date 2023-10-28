import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
dar tasvir Magnetude khat hayii ke namayan mishavand amud bar khat haye
tasvir asli ast. behamin dalil ebteda yek elamat mosbat bozorg moshahede
mikonim ke bekhater khat haye amudi va ofoghie marpelas. khat haye zavie
dar ham bekhater nardebun ha va mar haye tasvir asli bevujud amadan.
'''

img = cv2.imread('pic.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
plt.show()
