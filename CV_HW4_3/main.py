from PIL import Image, ImageEnhance
import cv2
import numpy as np
import torchvision.transforms.functional as F

def gammaCorrection(src, gamma):
    invGamma = 1 / gamma
    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    return cv2.LUT(src, table)

#gama correction
img = cv2.imread('lena.bmp')
gammaImg = gammaCorrection(img, 0.7)

cv2.imshow('Original image', img)
cv2.imshow('Gamma corrected image', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#saturation correction
img = Image.open("lena.bmp")
converter = ImageEnhance.Color(img)
img2 = converter.enhance(1.2)
img2.show()

#hue shifting
img = Image.open('lena.bmp')
img = F.adjust_hue(img, 0.3)
img.show()