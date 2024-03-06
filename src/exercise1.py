import cv2
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------
# EXERCISE 1
#Write a program to quantize an 8-bit/pixel image and quantize it to 5 bits and 3 bits using a uniform quantizer. 
#(b) Apply it to image of Fig. 2.21(a) from the book web site (www.imageprocessingplace.com) and compare the mean square errors and their visual qualities.
#----------------------------------------------------------------

def quantize_images(image,bits):
    new_max_value = 2**bits - 1
    float_image = image.astype(np.float32)
    new_image = np.floor((float_image / 255) * new_max_value)
    new_image = np.uint8((new_image / new_max_value) * 255)
    return new_image
#----------------------------------------------------------------
# Read image
#----------------------------------------------------------------
image= cv2.imread("./DIP3E_CH02_Original_Images/DIP3E_Original_Images_CH02/Fig0221(a)(ctskull-256).tif")





#----------------------------------------------------------------
# show the results
#----------------------------------------------------------------
# 8 BITS
image_8_bits =quantize_images(image,8)
# 5 BITS
image_5_bits =quantize_images(image,5)
# 3 BITS
image_3_bits =quantize_images(image,3)

mse_5_bits = np.mean((image_5_bits.astype(np.float64) - image_8_bits.astype(np.float64)) ** 2)
mse_3_bits = np.mean((image_3_bits.astype(np.float64) - image_8_bits.astype(np.float64)) ** 2)

print(f"\n5 BITS\nMean Squared Error: {mse_5_bits}")
print(f"\n3 BITS\nMean Squared Error: {mse_3_bits}")
plt.figure("8 BITS")
plt.xticks([])
plt.yticks([])
plt.imshow(image_8_bits)

plt.figure("5 BITS")
plt.xticks([])
plt.yticks([])
plt.imshow(image_5_bits)


plt.figure("3 BITS")
plt.xticks([])
plt.yticks([])
plt.imshow(image_3_bits)

plt.show()