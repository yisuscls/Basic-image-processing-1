import cv2
import numpy as np
import matplotlib.pyplot as plt

    
def arithmetic_operations(image):
    height, width, channels = image.shape
    
    add =  np.zeros((height, width, channels), dtype=np.uint8)
    sub =  np.zeros((height, width, channels), dtype=np.uint8)
    mult =  np.zeros((height, width, channels), dtype=np.uint8)
    mult_constant =  np.zeros((height, width, channels), dtype=np.uint8)
    div =  np.zeros((height, width, channels), dtype=np.uint8)
    counter=0
    for y in range(height):
        for x in range(width):
            counter += 1
            v=(counter)/(height*width)*100
            print(f"{v:.2f}%",end="\r")
            add[y, x,:] =image[y, x,:] + image[y, x,:]  
            sub[y, x,:] = image[y, x,:]-image[y, x,:]
            mult[y, x,:] = image[y, x,:] * image[y, x,:]
            mult_constant[y, x,:] = image[y, x,:] * 2
            for k in range(2):
                if image[y, x,k] != 0 :  # Avoid division by zero
                    div[y, x,k] = image[y, x,k] / image[y, x,k]
                else:
                    div[y, x,k] =0;
                
    return (add, sub,mult,mult_constant,div)

image = cv2.imread("./DIP3E_CH02_Original_Images/DIP3E_Original_Images_CH02/Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif")

addition,substraction, multiplication, multiplication_k, division = arithmetic_operations(image)

plt.figure("Original Image")
plt.xticks([])
plt.yticks([])
plt.imshow(image)
plt.ylabel(""+str(image.shape[0]))
plt.xlabel(""+str(image.shape[1]))

plt.figure("Addition")
plt.xticks([])
plt.yticks([])
plt.imshow(addition)
plt.ylabel(""+str(image.shape[0]))
plt.xlabel(""+str(image.shape[1]))

plt.figure("Substraction")
plt.xticks([])
plt.yticks([])
plt.imshow(substraction)
plt.ylabel(""+str(image.shape[0]))
plt.xlabel(""+str(image.shape[1]))

plt.figure("Multiplication")
plt.xticks([])
plt.yticks([])
plt.imshow(multiplication)
plt.ylabel(""+str(image.shape[0]))
plt.xlabel(""+str(image.shape[1]))

plt.figure("Multiplication constant")
plt.xticks([])
plt.yticks([])
plt.imshow(multiplication_k)
plt.ylabel(""+str(image.shape[0]))
plt.xlabel(""+str(image.shape[1]))

plt.figure("Division")
plt.xticks([])
plt.yticks([])
plt.imshow(division)
plt.ylabel(""+str(image.shape[0]))
plt.xlabel(""+str(image.shape[1]))


plt.show()