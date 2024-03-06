import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(image):
    height, width = image.shape
    histogram = np.zeros(image.max()+1)
    counter =0
    for y in range(height):
        for x in range(width):
            counter += 1
            v=(counter)/(height*width)*100
            print(f"{v:.2f}%",end="\r")
            histogram[image[y,x]] +=1
    print()
    return histogram/(height*width)
def equalization(image,histogram):
    height, width = image.shape
    new_image = image
    new_histogram = histogram*0
    cdf = np.cumsum(histogram) * 255
    plt.figure("histogram")
    plt.plot(cdf)
    counter = 0
    for y in range(height):
        for x in range(width):
            counter += 1
            v=(counter)/(height*width)*100
            print(f"{v:.2f}%",end="\r")
            new_image[y,x] =round(cdf[image[y, x]] )
            new_histogram[new_image[y, x]] +=1
    print()
    return new_image, new_histogram
image= cv2.imread("./DIP3E_CH03_Original_Images/DIP3E_Original_Images_CH03/Fig0308(a)(fractured_spine).tif",cv2.IMREAD_GRAYSCALE)

his=histogram(image)




plt.figure("Original Image")
plt.xticks([])
plt.yticks([])
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.ylabel(""+str(image.shape[0]))
plt.xlabel(""+str(image.shape[1]))
plt.subplot(122)

plt.stem(his,markerfmt=' ', basefmt=" ")
plt.yscale('log')

equalization_image, new_his=equalization(image, his)
plt.figure("Equalization Image")
plt.xticks([])
plt.yticks([])
plt.subplot(121)
plt.imshow(equalization_image, cmap='gray')
plt.ylabel(""+str(image.shape[0]))
plt.xlabel(""+str(image.shape[1]))
plt.subplot(122)

plt.stem(new_his,markerfmt=' ', basefmt=" ")
plt.yscale('log')


plt.show()