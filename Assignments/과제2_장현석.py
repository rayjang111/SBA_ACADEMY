import numpy as np
import cv2
fourcc=cv2.VideoWriter_fourcc(*'XVID')
frame_size=512,512
out=cv2.VideoWriter('../videos/count.avi',fourcc,1,frame_size,isColor=True)
for text in list(range(1,6))[::-1]:
    img=np.zeros(shape=(512,512,3),dtype=np.uint8)+255
    text=str(text)
    org=(int(img.shape[0]/2-100),int(img.shape[1]/2)+100)
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,text,org,font,10,(255,0,0),2)
    out.write(img)
    cv2.imshow('img',img)
    cv2.waitKey(500)
cv2.destroyAllWindows()
out.release()