import numpy as np
import cv2
import matplotlib.pyplot as plt

counter = 1

def change_threshold(pos):
    global counter
    T1 = cv2.getTrackbarPos('T1','img')
    T2 = cv2.getTrackbarPos('T2','img2')
    #cv2.imshow('img',img)
    print('T1 = ',T1,', T2 = ' ,T2)
    
    ret,dst = cv2.threshold(img , T1, 255 ,cv2.THRESH_BINARY)
    ret,dst2 = cv2.threshold(img , T2 , 255 ,cv2.THRESH_BINARY)
    
    #print('ret = ',ret)
    cv2.imshow('img',dst)
    cv2.imshow('img2',dst2)
    if counter > 1 :
        draw_hist(T1, T2)
    counter +=1
    
def draw_hist(T1,T2):
    #cv2.normalize(hist,hist,1,0,cv2.NORM_L1)
    
    plt.cla()
    plt.title('histogram')
    plt.bar(binX , hist , width = 1)
    plt.vlines(T1, 0, 2800, colors = 'orange', linestyles = '-', label = 'T1')
    plt.text(T1-4,2800,'T1')
    plt.vlines(T2, 0, 2800, colors = 'blue', linestyles = '-', label = 'T2')
    plt.text(T2-4,2800,'T2')
    plt.show()
    
def calc_hist(img):
    hist = cv2.calcHist(images = [img] , channels = [0] , mask = None ,
                         histSize = [256] , ranges = [0,256])
    
    hist = hist.flatten()
    binX = np.arange(256)
    
    return hist,binX
    
    
file = 'data/baboon.jpg'
img = cv2.imread(file,cv2.IMREAD_GRAYSCALE)
img2 = img.copy()
img3 = img.copy()

hist , binX = calc_hist(img)

cv2.imshow('img',img2)
cv2.imshow('img2',img3)


cv2.createTrackbar('T1','img',0,255,change_threshold)
cv2.createTrackbar('T2','img2',0,255,change_threshold)

cv2.setTrackbarPos('T2','img2',150)
cv2.setTrackbarPos('T1','img',80) 

cv2.waitKey()
cv2.destroyAllWindows()

