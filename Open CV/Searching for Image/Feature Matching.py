import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('C:\\Users\\HP\\Desktop\\COLLEGE\\Vision-AI-TaskPhase\\Task 2\\Open CV\\Searching for Image\\opencv-feature-matching-template.jpg',0)
img2 = cv2.imread('C:\\Users\\HP\\Desktop\\COLLEGE\\Vision-AI-TaskPhase\\Task 2\\Open CV\\Searching for Image\\opencv-feature-matching-image.jpg',0)

orb = cv2.ORB_create()

#detector
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

#key points
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

#BfMatcher
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()
plt.savefig('found.png')