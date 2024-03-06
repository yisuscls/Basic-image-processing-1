#!/bin/python
import numpy as np

from scipy import ndimage
import cv2
import numpy as np
import matplotlib.pyplot as plt
def interpolation_Bilinear(imArr, posX, posY):
	out = []

	#Get integer and fractional parts of numbers
	modXi = int(posX)
	modYi = int(posY)
	modXf = posX - modXi
	modYf = posY - modYi
	modXiPlusOneLim = min(modXi+1,imArr.shape[1]-1)
	modYiPlusOneLim = min(modYi+1,imArr.shape[0]-1)

	#Get pixels in four corners
	for chan in range(imArr.shape[2]):
		bl = imArr[modYi, modXi, chan]
		br = imArr[modYi, modXiPlusOneLim, chan]
		tl = imArr[modYiPlusOneLim, modXi, chan]
		tr = imArr[modYiPlusOneLim, modXiPlusOneLim, chan]
	
		#Calculate interpolation
		b = modXf * br + (1. - modXf) * bl
		t = modXf * tr + (1. - modXf) * tl
		pxf = modYf * t + (1. - modYf) * b
		out.append(int(pxf+0.5))

	return out


def resize(image,dpi,initial_dpi):
    enlargedShape = list(map(int, [image.shape[0]*dpi/initial_dpi, image.shape[1]*dpi/initial_dpi, image.shape[2]]))
    new_image = np.empty(enlargedShape, dtype=np.uint8)
    rowScale = float(image.shape[0]) / float(new_image.shape[0])
    colScale = float(image.shape[1]) / float(new_image.shape[1])
    counter=0
    for r in range(new_image.shape[0]):
        for c in range(new_image.shape[1]):
            v=(counter+1)/(new_image.shape[0]*new_image.shape[1])*100
            print(f"{v:.2f}%",end="\r")
            orir = r * rowScale 
            oric = c * colScale
            new_image[r, c] = interpolation_Bilinear(image, oric, orir)
            counter += 1
    print()
    return new_image
image = cv2.imread("./DIP3E_CH02_Original_Images/DIP3E_Original_Images_CH02/Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif")

image2= resize(image,100,1250)

image3= resize(image2,1250,100)
plt.figure(1)
plt.xticks([])
plt.yticks([])
plt.imshow(image)
plt.ylabel(""+str(image.shape[0]))
plt.xlabel(""+str(image.shape[1]))


plt.figure(2)
plt.xticks([])
plt.yticks([])
plt.imshow(image2)
plt.ylabel(""+str(image2.shape[0]))
plt.xlabel(""+str(image2.shape[1]))


plt.figure(3)
plt.xticks([])
plt.yticks([])
plt.imshow(image3)
plt.ylabel(""+str(image3.shape[0]))
plt.xlabel(""+str(image3.shape[1]))

plt.show()

