#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import cv2
import os
os.chdir('C:/Users/edu/Desktop/HyunSuk/files')
src=cv2.imread('./data/lena.jpg')
while True:
    r=cv2.selectROIs('src',src)
    if len(r)==2:
        r1,r2=r
        break
    print("두개 영역만을 추출하세요. %s 개의 영역을 추출하셨습니다"%len(r))
print('r1=',r1)
print('r2=',r2)
img1=src[r1[1]:r1[1]+r1[3],r1[0]:r1[0]+r1[2]]
img2=src[r2[1]:r2[1]+r2[3],r2[0]:r2[0]+r2[2]]
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img1=cv2.merge([img1,img1,img1])
_ ,img1 = cv2.threshold(img1, 150, 255, cv2.THRESH_BINARY)
img2=cv2.bitwise_not(img2)
src[r1[1]:r1[1]+r1[3],r1[0]:r1[0]+r1[2]]=img1
src[r2[1]:r2[1]+r2[3],r2[0]:r2[0]+r2[2]]=img2
cv2.imshow('result',src)
cv2.waitKey(0)
cv2.destroyAllWindows()
