import numpy as np
import cv2

def show_images(imgs):
    i=0
    for img in imgs:
        i = i+1
        img=cv2.pyrDown(img)
        img=cv2.pyrDown(img)
        cv2.imshow('slika' + str(i),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def my_function(img):
#------------------------Challenge 6-------------------------------
    blur = cv2.medianBlur(img,25)

    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,30,param1=200,param2=30,minRadius=10,maxRadius=100)

    if circles is None:
        return 0

    '''#Show circles
    for circle in circles[0]:
        cv2.circle(img,(circle[0],circle[1]),circle[2],(0,255,0),2)
        cv2.circle(img,(circle[0],circle[1]),3,(0,0,255),3)
    show_images([img])
    '''
    return circles.shape[1]
