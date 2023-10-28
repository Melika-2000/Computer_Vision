import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('painting.jpg')
image2 = cv2.imread('painting.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
imgArr = np.array(image)
cv2.imshow('image', image)
cv2.waitKey(0)

low_red = np.array([170, 155, 84])
high_red = np.array([179, 255, 255])
mask = cv2.inRange(image, low_red, high_red)
image2 = cv2.bitwise_and(image2, image2, mask=mask)
img2Arr = np.array(image2)
cv2.imshow('red parts', image2)
cv2.waitKey()


rData = [0] * 256
gData = [0] * 256
bData = [0] * 256
r2Data = [0] * 256
g2Data = [0] * 256
b2Data = [0] * 256

x = []
for i in range(256):
    x.append(i)
c =0
for i in range(imgArr.shape[0]):
    for j in range(imgArr.shape[1]):
        rData[imgArr[i][j][0]] += 1
        gData[imgArr[i][j][1]] += 1
        bData[imgArr[i][j][2]] += 1

        r2Data[img2Arr[i][j][0]] += 1
        g2Data[img2Arr[i][j][1]] += 1
        b2Data[img2Arr[i][j][2]] += 1

#chon maghadir 0 dar tasvir ziad ast baraye namayesh behtare histogram
#an meghdari az tedade an kam mikonim
r2Data[0] = r2Data[0] - 758000

#plt.plot(x, rData, label = "histogram")
plt.plot(x, r2Data, label = "histogram")

plt.legend()
plt.show()

'''
ba tavajoh ba mask gharar dade shode moshahede mishavad maghadir R dar aksar pixel
ha 0 shode va dar ye range khasi maghari R bishtari darim
'''