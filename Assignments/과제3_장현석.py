import numpy as np
import cv2
import pandas as pd
path='./data/'
lena=cv2.imread(path+'lena.jpg')
apple=cv2.imread(path+'apple.jpg')
banana=cv2.imread(path+'banana.jpg')
baboon=cv2.imread(path+'baboon.jpg')
rows, cols, channels = lena.shape
fourcc=cv2.VideoWriter_fourcc(*'XVID')
frame_size=512,512
out=cv2.VideoWriter('../videos/screenTransition.avi',fourcc,30,frame_size,isColor=True)
for i in np.array(list(range(360))[::-1]):
    M1 = cv2.getRotationMatrix2D( (rows/2, cols/2),  i, 1 )
    dst1 = cv2.warpAffine( lena, M1, (rows, cols))
    cv2.imshow('video',  dst1)
    out.write(dst1)
    cv2.waitKey(10)
for i in np.arange(0,1,0.01):
    alpha=1-i
    beta=i
    weighted=cv2.addWeighted(apple,alpha,banana,beta,0)
    cv2.imshow('video',weighted)
    out.write(weighted)
    cv2.waitKey(30)
for i in np.arange(1,0.5,-0.01):
    M1 = cv2.getRotationMatrix2D( (rows/2, cols/2),  0, i )
    dst1 = cv2.warpAffine( banana, M1, (rows, cols))
    cv2.imshow('video',  dst1)
    cv2.waitKey(30)
    out.write(dst1)
for i in np.arange(0.5,1,0.01):
    M1 = cv2.getRotationMatrix2D( (rows/2, cols/2),  0, i )
    dst1 = cv2.warpAffine( banana, M1, (rows, cols))
    cv2.imshow('video',  dst1)
    cv2.waitKey(10)
    out.write(dst1)
for i in range(20):
    cv2.imshow('video',baboon)
    cv2.waitKey(100)
    out.write(baboon)
cv2.destroyAllWindows()
out.release()
