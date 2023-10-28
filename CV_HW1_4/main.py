import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
'''
pixel be pixel tasvir peimayesh mishavad. dar araye hData tedade har
grayScale zakhire shode sepas in dade ha besurat nemudar namayesh
dade mishavad. dar bakhsh 2 az meghdar sath khakestari har pixel 30
vahed kam shode va mojadadan histogram on namayesh dade mishavad. 
dar akhar plane 6,7,8 mohasebe shode va histogram an namayesh dade
mishavad
'''
def decimalToBinary(a):

    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
    return x[::-1]

def binaryToDecimal(n):
    return int(n,2)

def changeBinaryDigits(bNum, l):
    for i in range(8):
        if 7-i in l:
            continue
        else:
            tmp = list(bNum)
            tmp[i] = '0'
            bNum = "".join(tmp)
    return bNum


numpydata = np.array(Image.open('histogram.jpeg'))
x = []
for i in range(255):
    x.append(i)

hData = [0] * 255
hData2 = [0] * 255
for i in range(numpydata.shape[0]):
    for j in range(numpydata.shape[1]):
        #maghadir histogram 1
        hData[numpydata[i][j][0]] += 1
        #maghadir histogram 2
        if numpydata[i][j][0] - 30 >=0:
            hData2[numpydata[i][j][0] - 30] += 1
        else:
            hData2[0] += 1

#namayesh plane 6,7,8
for i in range(numpydata.shape[0]):
    for j in range(numpydata.shape[1]):
        bNum = decimalToBinary(numpydata[i][j][0])
        numpydata[i][j] = binaryToDecimal(changeBinaryDigits(bNum,[6,7,8]))
im = Image.fromarray(numpydata)
Image._show(im)

#maghadir histogram 3
hData3 = [0] * 255
for i in range(numpydata.shape[0]):
    for j in range(numpydata.shape[1]):
        hData3[numpydata[i][j][0]] += 1

plt.plot(x, hData, label = "histogram 1")
plt.plot(x, hData2, label = "histogram 2")

plt.legend()
plt.xlabel('intensity')
plt.ylabel('count')
plt.show()

plt.plot(x, hData3, label = "histogram 3")
plt.legend()
plt.xlabel('intensity')
plt.ylabel('count')
plt.show()

'''
4.1
contrast histogram paiin ast zira shahede tajamoe sotuhe khakestari dar
yek mahdude kuchik hastim
4.2
tabe 30 vahed be chap montaghel shode
4.3
histigram taghir ziadi mikonad. tedade barkhi sotuh khakestari chandin
barabar shode dar hali ke tedad barkhi digar 0
'''
