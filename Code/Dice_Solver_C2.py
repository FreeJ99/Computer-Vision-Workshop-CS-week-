import numpy as np
import cv2

def show_images(imgs):
    i=0
    for img in imgs:
        i = i+1
        cv2.imshow('slika' + str(i),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def my_function(img):
#------------------------Challenge 2-------------------------------
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)

    kernel = np.ones((5,5),np.uint8)

    thresh = cv2.erode(thresh,kernel,iterations = 6)
    thresh = cv2.dilate(thresh,kernel,iterations = 5)

    thresh=cv2.pyrDown(thresh)
    thresh=cv2.pyrDown(thresh)

    #show_images([thresh])

    mask=np.zeros((thresh.shape[0]+2, thresh.shape[1]+2),np.uint8)

    counter = 0
    for i in range(thresh.shape[0]):
        for j in range(thresh.shape[1]):
            if thresh[i][j]==255 and mask[i][j]==0:
                counter+=1
                cv2.floodFill(thresh, mask,(j,i), 150)

    return counter
