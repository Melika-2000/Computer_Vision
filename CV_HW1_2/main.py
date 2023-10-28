import numpy as np
from PIL import Image

'''
ebteda tasavir tabdil be grayscale mishavad sepas az 
tarigh filter labe yab sobel va laplasian labe ha tashkhis
dade mishavand.
'''
numpydata = np.array(Image.open('alighapoo.jpg'))
for i in range(numpydata.shape[0]):
    for j in range(numpydata.shape[1]):
        scaling = 0.299 * numpydata[i][j][0] + 0.587 * numpydata[i][j][1] + 0.114 * numpydata[i][j][2]
        numpydata[i][j][0] = scaling
        numpydata[i][j][1] = scaling
        numpydata[i][j][2] = scaling

vEdgeData = numpydata.copy()
hEdgeData = numpydata.copy()
vhEdgesData = numpydata.copy()
dEdgesDate = numpydata.copy()

for i in range(1, numpydata.shape[0] - 1):
    for j in range(1, numpydata.shape[1] - 1):
        # labe haye amudi
        value1 = numpydata[i - 1][j - 1][0] - numpydata[i - 1][j + 1][0] + 2 * numpydata[i][j - 1][0] - \
                 2 * numpydata[i][j + 1][0] + numpydata[i + 1][j - 1][0] - numpydata[i + 1][j + 1][0]

        # labe haye ofoghi
        value2 = numpydata[i - 1][j - 1][0] - numpydata[i + 1][j - 1][0] + 2 * numpydata[i - 1][j][0] - \
                 2 * numpydata[i + 1][j][0] + numpydata[i - 1][j + 1][0] - numpydata[i + 1][j + 1][0]

        # labe haye ofoghi va amudi
        value3 = 4*numpydata[i][j][0] - numpydata[i-1][j][0] - numpydata[i+1][j][0] - \
                 numpydata[i][j-1][0] - numpydata[i][j+1][0]

        # labe haye ghotri
        value4 = 4*numpydata[i][j][0] - numpydata[i-1][j-1][0] - numpydata[i-1][j+1][0] - \
                 numpydata[i+1][j-1][0] - numpydata[i+1][j+1][0]

        if value1 < -50: value1 = 0
        else: value1 = 255
        if value2 < -50: value2 = 0
        else: value2 = 255
        if value3 < 0: value2 = 0
        else: value3 = 255
        if value4 < 0: value2 = 0
        else: value4 = 255

        vEdgeData[i][j] = value1
        hEdgeData[i][j] = value2
        vhEdgesData[i][j] = value3
        dEdgesDate[i][j] = value4

im = Image.fromarray(hEdgeData)
Image._show(im)
im = Image.fromarray(vEdgeData)
Image._show(im)
im = Image.fromarray(vhEdgesData)
Image._show(im)
im = Image.fromarray(dEdgesDate)
Image._show(im)

'''
#soal 2-1

dar halate koli hardo ravesh labe hara taghviat mikonand ama be dalil
tafavot zarayeb filter laplasian ba filter labe yab natije kami tafavot 
darad. dar filter laplasian tasvir vazeh tar ast

'''