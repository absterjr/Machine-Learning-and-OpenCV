import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('watch.png', cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]
px = img[55,55]
print(px)

#ROI
px = img[100:150, 100:150] = [255,255,255]
print(px)

#characteristics
print(img.shape)
print(img.size)
print(img.dtype)


watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

print(img.shape)
print(img.size)
print(img.dtype)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('operatedwatch.png',img)