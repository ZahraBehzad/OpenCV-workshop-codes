import numpy as np
from matplotlib import pyplot as plt
import cv2

# Load an image 
img = cv2.imread("flower.jpg", cv2.IMREAD_COLOR)
# Equivalent to: cv2.imread("image.jpg", 1)
print(img.shape) # Output: (height, width, channels)
cv2.imshow('image', img)

# Load an color image in grayscale
image_gray = cv2.imread("flower.jpg", cv2.IMREAD_GRAYSCALE)
# Equivalent to: cv2.imread("image.jpg", 0)
print(image_gray.shape)  # Output: (height, width)
cv2.imshow('image', image_gray)

# Load an image with all channels
image_unchanged = cv2.imread("/Test.png", cv2.IMREAD_UNCHANGED)
# Equivalent to: cv2.imread("image.png", -1)
print(image_unchanged.shape)  # Output: (height, width, 4) for PNG with alpha
cv2.imshow('image', image_unchanged)

cv2.waitKey(0)
cv2.destroyWindow()

# Saving the image
image_gray = cv2.imread("flower.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite('gray.jpg', image_gray)

# Doing different functions based on the key that user presses
img = cv2.imread("flower.jpg", 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('savedImage.jpg', img)
    cv2.destroyAllWindows()

# Show image using matplotlib
img = cv2.imread("flower.jpg", 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
