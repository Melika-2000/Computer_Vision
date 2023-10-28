import numpy as np
from PIL import Image

'''
aks be surat satri peimayesh mishe. baraye x barabar kardan tule aks
har pixel x bar dar araye tmp rikhte mishe. baraye y barabar kardan arz,
dar for biruni y bar tmp be im2 ezafe mishe.
'''

numpydata = np.array(Image.open('alighapoo.jpg'))

#2 barabar kardan tasvir
im2 = np.array([])
for i in range(numpydata.shape[0]):
    tmp = np.array([])
    for j in range(numpydata.shape[1]):
        tmp = np.append(tmp, numpydata[i][j]).astype(np.uint8)
        tmp = np.append(tmp, numpydata[i][j]).astype(np.uint8)
    im2 = np.append(im2,tmp).astype(np.uint8)
    im2 = np.append(im2,tmp).astype(np.uint8)

im2 = im2.reshape(2*numpydata.shape[0],2*numpydata.shape[1],3)
im = Image.fromarray(im2)
Image._show(im)

#keshidegi ofoghi
im2 = np.array([])
for i in range(numpydata.shape[0]):
    tmp = np.array([])
    for j in range(numpydata.shape[1]):
        tmp = np.append(tmp, numpydata[i][j]).astype(np.uint8)
        tmp = np.append(tmp, numpydata[i][j]).astype(np.uint8)
    im2 = np.append(im2,tmp).astype(np.uint8)
im2 = im2.reshape(numpydata.shape[0],2*numpydata.shape[1],3)
im = Image.fromarray(im2)
Image._show(im)

#keshidegi amudi
im2 = np.array([])
for i in range(numpydata.shape[0]):
    tmp = np.array([])
    for j in range(numpydata.shape[1]):
        tmp = np.append(tmp, numpydata[i][j]).astype(np.uint8)
    im2 = np.append(im2,tmp).astype(np.uint8)
    im2 = np.append(im2,tmp).astype(np.uint8)
im2 = im2.reshape(2*numpydata.shape[0],numpydata.shape[1],3)
im = Image.fromarray(im2)
Image._show(im)

#aks dar rastaye amudi 2 barabar rasta ofoghi keshide mishavad
im2 = np.array([])
for i in range(numpydata.shape[0]):
    tmp = np.array([])
    for j in range(numpydata.shape[1]):
        tmp = np.append(tmp, numpydata[i][j]).astype(np.uint8)
        tmp = np.append(tmp, numpydata[i][j]).astype(np.uint8)
    im2 = np.append(im2,tmp).astype(np.uint8)
    im2 = np.append(im2,tmp).astype(np.uint8)
    im2 = np.append(im2,tmp).astype(np.uint8)
    im2 = np.append(im2,tmp).astype(np.uint8)

im2 = im2.reshape(4*numpydata.shape[0],2*numpydata.shape[1],3)
im = Image.fromarray(im2)
Image._show(im)


