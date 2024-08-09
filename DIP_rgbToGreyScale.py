import cv2 as cv
import numpy as np

img = cv.imread("Image.jpg")
cv.imshow("a", img)
print(img)
g = img.astype(np.float32)
grm = (g[:, :, 0] + g[:, :, 1] + g[:, :, 2]) / 3
grm = grm.astype(np.uint8)
cv.imshow("g", grm)
n = cv.waitKey(0)
