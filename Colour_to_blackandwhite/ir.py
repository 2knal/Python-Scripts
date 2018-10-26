import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

def threshold(imarray):
    balancear = []
    newar = imarray
    #eachpix is a 1d array with 4 elements - the r,g,b,alpha values for png image 
    #eachpix is a 1d array with 3 elements for jpg, jpeg files
    for eachrow in imarray:
        for eachpix in eachrow:
            avg = np.sum(eachpix[:3])/3
            balancear.append(avg)
    balance = np.sum(balancear)//len(balancear)
    #print(balance)
    for eachrow in newar:
        for eachpix in eachrow:
            if np.sum(eachpix[:3])//3 > balance:
                eachpix[:] = 255
            else:
                eachpix[0:3] = 0
                #eachpix[3] = 255 
    return newar


i = Image.open('me2.jpeg')
iar = np.array(i)
print(np.shape(iar))
iar = threshold(iar)
plt.imshow(iar)
plt.show()