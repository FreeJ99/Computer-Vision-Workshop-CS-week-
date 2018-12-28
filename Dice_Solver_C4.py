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
#------------------------Challenge 4-------------------------------
    blur = cv2.GaussianBlur(img,(31,31),0)
    blur= cv2.medianBlur(img,25)

    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    gray=cv2.pyrDown(gray)
    gray=cv2.pyrDown(gray)

    thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,31,30)

    kernel = np.ones((5,5),np.uint8)
    kernel2 = np.ones((3,3),np.uint8)

    thresh = cv2.dilate(thresh,kernel,iterations=1)
    thresh = cv2.erode(thresh,kernel,iterations = 2)
    thresh = cv2.erode(thresh,kernel2,iterations = 1)

    #show_images([thresh])

    mask=np.zeros((thresh.shape[0]+2, thresh.shape[1]+2),np.uint8)

    counter = 0
    for i in range(thresh.shape[0]):
        for j in range(thresh.shape[1]):
            if thresh[i][j]==255 and mask[i][j]==0:
                counter+=1
                cv2.floodFill(thresh, mask,(j,i), 150)

    return counter
