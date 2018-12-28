import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
import os

def show_images(imgs):
    i=0
    for img in imgs:
        i = i+1
        img=cv2.pyrDown(img)
        img=cv2.pyrDown(img)
        cv2.imshow('slika' + str(i),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#CHANGE path
img = cv2.imread("Pictures/Challenge_1/5.jpg",1)

noisy = img.copy()

#Salt and Peper noise
slt = 0.15 # CHANGE: verovatnoca da se javi salt
pep = 0.15 # CHANGE: verovatnoca da se javi pepper
for i in range(noisy.shape[0]):
    for j in range(noisy.shape[1]):
        random=np.random.rand(1)
        if random<=pep:
            noisy[i][j][0]=0
            noisy[i][j][1]=0
            noisy[i][j][2]=0
        elif random >= 1-slt:
            noisy[i][j][0]=255
            noisy[i][j][1]=255
            noisy[i][j][2]=255


#Gaussian noise
'''
noise=np.zeros(img.shape,np.uint8)
m=np.asarray([0,0,0]) # CHANGE: mean = centriranost vrednosti za svaki kanal (B,G,R)
s=np.asarray([50,50,50]) # CHANGE: standard deviation = 'sirina' dobijenih vrednosti za svaki kanal
noise=cv2.randn(noise,(50,50,50),(255,255,255))
noisy=cv2.subtract(img,noise)
'''

show_images([img,noisy])
#CHANGE path
cv2.imwrite("Pictures/salt_and_pepper_strong.jpg",noisy)
