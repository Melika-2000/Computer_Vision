from __future__ import division
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bird.png',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude = 20*np.log(np.abs(fshift))

#creating bandreject filter
fL = 0.1
fH = 0.4
b = 0.08
N = int(np.ceil((4 / b)))
if not N % 2: N += 1  # Make sure that N is odd.
n = np.arange(N)
# Compute a low-pass filter with cutoff frequency fL.
hlpf = np.sinc(2 * fL * (n - (N - 1) / 2))
hlpf *= np.blackman(N)
hlpf /= np.sum(hlpf)
# Compute a high-pass filter with cutoff frequency fH.
hhpf = np.sinc(2 * fH * (n - (N - 1) / 2))
hhpf *= np.blackman(N)
hhpf /= np.sum(hhpf)
hhpf = -hhpf
hhpf[(N - 1) // 2] += 1
# Add both filters.
h = hlpf + hhpf

magnitude = np.convolve(magnitude, h)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude, cmap = 'gray')
plt.title('Magnitude'), plt.xticks([]), plt.yticks([])