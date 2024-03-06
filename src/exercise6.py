import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
import cv2 
def filter_3x3(image, kernel):

    height, width = image.shape
    padded_image = np.pad(image, ((1, 1), (1, 1)),mode="constant", constant_values=0)
    output_image = np.zeros_like(image)
    counter = 0
    for y in range(height):
        for x in range(width):
            counter += 1
            v=(counter)/(height*width)*100
            print(f"{v:.2f}%",end="\r")
            output_image[y, x] = np.sum(padded_image[y:y+3, x:x+3] * kernel)
    print()
    return output_image

def fix_image(image):
    image= (image-image.min())/((image-image.min())).max()*255.0
    image = image.astype(np.uint8)
    return image
def laplacian(image,kernel):
    
    laplacian_image = filter_3x3(image, kernel)
    enhanced_image  = image - laplacian_image
    enhanced_image = fix_image(enhanced_image)
    return enhanced_image, laplacian_image
def unsharp_masking(image, kernel, k=1.5):
    low_pass_image = filter_3x3(image, kernel)
    high_boost_image = image + k * (image- low_pass_image)
    return fix_image(high_boost_image),low_pass_image

image = cv2.imread("./DIP3E_CH03_Original_Images/DIP3E_Original_Images_CH03/Fig0338(a)(blurry_moon).tif",cv2.IMREAD_GRAYSCALE)

if np.max(image) > 1:
    image = image / 255.0
laplacian_kernel = np.array([
                            [0, -1, 0],
                            [-1, 4, -1],
                            [0, -1, 0]
                            ])

enhanced_image, laplacian_image= laplacian(image,laplacian_kernel)

image2 = cv2.imread("./DIP3E_CH03_Original_Images/DIP3E_Original_Images_CH03/Fig0340(a)(dipxe_text).tif",cv2.IMREAD_GRAYSCALE)

if image2.dtype != np.uint8:
    image2 = (image2 / image2.max()) * 255
    image2 = image2.astype(np.uint8)
    
averaging_kernel = np.zeros((3, 3), np.float32)+ (1/ 9.0)

enhanced_image2, laplacian_image2= laplacian(image2,laplacian_kernel)
masking_image2, low_pass_image2= unsharp_masking(image2,laplacian_kernel,1.5)

#----------------------------------------------------------------
# Parte A
#----------------------------------------------------------------

plt.figure("Parte A",figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.xticks([])
plt.yticks([])
plt.imshow(image, cmap="gray")
plt.title("Original Image")

plt.subplot(1, 3, 2)
plt.xticks([])
plt.yticks([])
plt.imshow(laplacian_image, cmap="gray")
plt.title("Laplacian Filtered Image")

plt.subplot(1, 3, 3)
plt.xticks([])
plt.yticks([])
plt.imshow(enhanced_image , cmap="gray")
plt.title("Enhanced Image")

#----------------------------------------------------------------
# Parte B
#----------------------------------------------------------------

plt.figure("Parte B",figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.xticks([])
plt.yticks([])
plt.imshow(image2, cmap="gray")
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.xticks([])
plt.yticks([])
plt.imshow(laplacian_image2, cmap="gray")
plt.title("Laplacian Filtered Image")

plt.subplot(2, 2, 3)
plt.xticks([])
plt.yticks([])
plt.imshow(enhanced_image2 , cmap="gray")
plt.title("Enhanced Image")


plt.subplot(2, 2, 4)
plt.xticks([])
plt.yticks([])
plt.imshow(masking_image2 , cmap="gray")
plt.title("Enhanced Image")

plt.show()
