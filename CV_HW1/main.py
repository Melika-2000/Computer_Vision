import math
import numpy as np
from PIL import Image

'''
adade RGB dar zarayeb monaseb zarb shode va jaigozin adad ghabli
mishavand. sepas meghdar max, min, avg ,var anha mohasebe mishavad.
tasvir gray scale shode namayesh dade mishavad
'''

numpydata = np.array(Image.open('alighapoo.jpg'))
min = 255
max = 0
sum = 0
for i in range(numpydata.shape[0]):
    for j in range(numpydata.shape[1]):
        scaling = 0.299 * numpydata[i][j][0] + 0.587 * numpydata[i][j][1] + 0.114 * numpydata[i][j][2]
        numpydata[i][j][0] = scaling
        numpydata[i][j][1] = scaling
        numpydata[i][j][2] = scaling
        if scaling < min:
            min = scaling
        if scaling > max:
            max = scaling
        sum += scaling
n = (numpydata.shape[0] * numpydata.shape[1])
avg = sum / n
variance = 0
for i in range(numpydata.shape[0]):
    for j in range(numpydata.shape[1]):
        variance += math.pow(numpydata[i][j][0] - avg, 2) / n

im = Image.fromarray(numpydata)
print('Max brightness:' + str(max))
print('min brightness:' + str(min))
print('brightness avg: %.2f' % avg)
print('brightness variance: %.2f' % variance)
Image._show(im)