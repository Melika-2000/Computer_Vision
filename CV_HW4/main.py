import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open('park.png')
img = cv2.imread('park.png')

print("picture type: "+image.mode) #color space of the pic
img =  cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
cv2.imshow('image', img)
cv2.waitKey(0)

# The transformation from RGB to HSI is called CV_RGB2HLS in OpenCV.
img2 =  cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
cv2.imshow('image', img2)
cv2.waitKey(0)


imgArr = np.array(img)
img2Arr = np.array(img2)

rData = [0] * 256
gData = [0] * 256
bData = [0] * 256
hData = [0] * 256
sData = [0] * 256
iData = [0] * 256

x = []
for i in range(256):
    x.append(i)

for i in range(imgArr.shape[0]):
    for j in range(imgArr.shape[1]):
        rData[imgArr[i][j][0]] += 1
        gData[imgArr[i][j][1]] += 1
        bData[imgArr[i][j][2]] += 1

        hData[img2Arr[i][j][0]] += 1
        sData[img2Arr[i][j][1]] += 1
        iData[img2Arr[i][j][2]] += 1

# plt.plot(x, rData, label = "Red color histogram")
# plt.plot(x, gData, label = "Green color histogram")
# plt.plot(x, bData, label = "Blue color histogram")
# plt.plot(x, hData, label = "Hue histogram")
# plt.plot(x, sData, label = "saturation histogram")
plt.plot(x, iData, label = "intensity histogram")

plt.legend()
plt.show()

'''
bakhsh ziadi az R G B meghdar 0 daran.
dar inja mibinim kholus rang (saturation), aksaran nazdik be sefre yani sefidi bishtari
dar tasvir darim. dar histogram shedat roshanyi (intensity) mibinim maghadir motevaset va
blaye ziadi darim. inha contraste kame tasvir ra tojih mikonan

'''
