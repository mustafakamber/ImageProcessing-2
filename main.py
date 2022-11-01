import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('image.jpg', 0)
cv2.imshow("original", image)

[h, w] = image.shape
new_image = np.zeros([h, w], dtype=np.uint8)

for i in range(h):
    for j in range(w):
        new_image[i, j] = 255 - image[i, j]

print(image[0, 0])
cv2.imshow("inverted", new_image)
cv2.waitKey()