import numpy as np
import cv2

cap = cv2.VideoCapture('C:\\Users\\HP\\Desktop\\COLLEGE\\Vision-AI-TaskPhase\\Task 2\\Open CV\\Background Reduction\\people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("Output.avi",fourcc,20.0,(640,480))
while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    if cv2.waitKey(30) & 0xff == ord('q'):
    
        break
    
cap.release()
cv2.destroyAllWindows()