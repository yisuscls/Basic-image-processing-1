import cv2
import numpy as np
import matplotlib.pyplot as plt
#----------------------------------------------------------------
# EXERCISE 2
#(a) Write a computer program capable of zooming and shrinking an image by pixel replication. Assume that the desired zoom/shrink factors are integers.    
#(b) Download Fig. 2.20(a) from the book web site and use your program to shrink the image by a factor of 10.
#(c) Use your program to zoom the image in (b) back to the resolution of the original.  Explain the reasons for their differences

#----------------------------------------------------------------
image=cv2.imread("./DIP3E_CH02_Original_Images/DIP3E_Original_Images_CH02/Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif")


def shrink(image ,factor):
    height, width, channels = image.shape
    height, width = (height // factor, width // factor,)
    new_image = np.zeros((height, width, channels), dtype=np.uint8)
    for x in range(height):
        for y in range(width):
            new_image[x, y, :] = image[x*factor, y*factor, :]
    return new_image

def zoom(image,factor):
    height, width, channels = image.shape
    height, width = (height * factor, width * factor,)
    new_image = np.zeros((height, width, channels), dtype=np.uint8)
    for x in range(height):
        for y in range(width):
            new_image[x, y, :] = image[x//factor, y//factor, :]
    return new_image

shrink_image=shrink(image,10)
zoom_image=zoom(shrink_image,10)


#----------------------------------------------------------------
# show the results
#----------------------------------------------------------------

#original image
plt.figure(1)
plt.xticks([])
plt.yticks([])
plt.imshow(image)
plt.ylabel(""+str(image.shape[0]))
plt.xlabel(""+str(image.shape[1]))

#shrinking  image
plt.figure(2)
plt.xticks([])
plt.yticks([])
plt.imshow(shrink_image)
plt.ylabel(""+str(shrink_image.shape[0]))
plt.xlabel(""+str(shrink_image.shape[1]))
# zooming image
plt.figure(3)
plt.xticks([])
plt.yticks([])
plt.imshow(zoom_image)
plt.ylabel(""+str(zoom_image.shape[0]))
plt.xlabel(""+str(zoom_image.shape[1]))
plt.show()

