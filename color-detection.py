# Python program for Detection of a  
# specific color(blue here) using OpenCV with Python 
import cv2 
import numpy as np  
  
# Webcamera no 0 is used to capture the frames 
cap = cv2.VideoCapture(0)  
  
# This drives the program into an infinite loop. 
while(1):        
    # Captures the live stream frame-by-frame 
    _, frame = cap.read()  
    # Converts images from BGR to HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([15,15,100]) 
    upper_red = np.array([55,55,200]) 

    lower_green = np.array([15, 100, 15])
    upper_green = np.array([55, 200, 55])

    lower_blue = np.array([50, 50, 110])
    upper_blue = np.array([255, 255, 130])

    
    
    # Here we are defining range of bluecolor in HSV 
    # This creates a mask of blue coloured  
    # objects found in the frame. 
    mask = cv2.inRange(hsv, lower_red, upper_red) 
    
    # The bitwise and of the frame and mask is done so  
    # that only the blue coloured objects are highlighted  
    # and stored in res 
    res = cv2.bitwise_and(frame,frame, mask= mask) 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res) 
    
    # This displays the frame, mask  
    # and res which we created in 3 separate windows. 
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
  
# Destroys all of the HighGUI windows. 
cv2.destroyAllWindows() 
    
# release the captured frame 
cap.release() 
