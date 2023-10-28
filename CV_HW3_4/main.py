import cv2
import imutils as imutils
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bird.png',0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude1 = 20*np.log(np.abs(fshift))

rotated_image = imutils.rotate(img, angle=45)
f2 = np.fft.fft2(rotated_image)
fshift2 = np.fft.fftshift(f2)
magnitude2 = 20*np.log(np.abs(fshift2))

M = np.float32([[1, 0, 20], [0, 1, 0]]) #translation matrix
(rows, cols) = img.shape[:2]
moved_image = cv2.warpAffine(img, M, (cols, rows))
f3 = np.fft.fft2(moved_image)
fshift3 = np.fft.fftshift(f3)
magnitude3 = 20*np.log(np.abs(fshift3))

plt.subplot(331),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(332),plt.imshow(magnitude1, cmap = 'gray')
plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
plt.subplot(334),plt.imshow(rotated_image, cmap ='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(335),plt.imshow(magnitude2, cmap = 'gray')
plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
plt.subplot(337),plt.imshow(moved_image, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(338),plt.imshow(magnitude3, cmap = 'gray')
plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
plt.show()

"""
2)
ba rotate tasvir be andaze 45 daraje, barkhi jahaye tasvir az kadr kharej shode
va barkhi jahaye digar an khali mimanad. behamin dalil engar labe haye vazehi dar
atrafe tasavir rotate shode darim. behamin dalil khat haye movarabi (amud bar labe
haye tasvir asli) dar tasvir furie ijad shode and.

3)
ba shift tasvir be andaze 20 pixel be samt rast, engar yek labe amudi dar ghesmat
chap tasvir ijad shode ast, behamin dalil khat ofoghi tabdil furie kami porrangtar
shode ast

"""