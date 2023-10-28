from PIL import Image
from numpy import *
import numpy as np

'''
har pixel besurat binary namayesh dade mishe, bar asas inke
kodum plane haro mikhaim un bit ha hefz shode va sayer bitha
meghdar 0 migirand (az tarigh tabe changeBinaryDigits). sepas
tasvir taghir karde namayesh dade mishavad
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

numpydata = np.array(Image.open('charli.jpeg'))

#namayesh plane 6,7,8
newData = numpydata.copy()
for i in range(numpydata.shape[0]):
    for j in range(numpydata.shape[1]):
        bNum = decimalToBinary(newData[i][j])
        newData[i][j] = binaryToDecimal(changeBinaryDigits(bNum,[6,7,8]))
im = Image.fromarray(newData)
Image._show(im)

#namayesh plane 7,8
newData = numpydata.copy()
for i in range(numpydata.shape[0]):
    for j in range(numpydata.shape[1]):
        bNum = decimalToBinary(newData[i][j])
        newData[i][j] = binaryToDecimal(changeBinaryDigits(bNum,[7,8]))
im = Image.fromarray(newData)
Image._show(im)

#namayesh plane 1,2,3,4
newData = numpydata.copy()
for i in range(numpydata.shape[0]):
    for j in range(numpydata.shape[1]):
        bNum = decimalToBinary(newData[i][j])
        newData[i][j] = binaryToDecimal(changeBinaryDigits(bNum,[1,2,3,4]))
im = Image.fromarray(newData)
Image._show(im)







