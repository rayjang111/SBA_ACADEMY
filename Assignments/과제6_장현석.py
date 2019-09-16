#-*- coding:utf-8 -*-
import numpy as np
import cv2
src=cv2.imread('./data/Heart10.jpg')
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
ret,dst=cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV)
ret,labels=cv2.connectedComponents(dst)
dst   = np.zeros(src.shape, dtype=src.dtype)+255
for i in range(1, ret): # 분할영역 표시
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    dst[labels == i] = [b, g, r]
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
