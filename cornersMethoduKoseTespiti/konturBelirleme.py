import cv2
import numpy as np

img=cv2.imread("binary.png")
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



ret,tresh=cv2.threshold(imgray,100,100,cv2.THRESH_BINARY)#0 ve 1 leri ayırt et 
cont,a=cv2.findContours(tresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(cont)

#100 ve 200 esık değerdir

"""for k in cont:
    (x,y,w,h)= cv2.boundingRect(k)
    if cv2.contourArea(k)>100:
        cv2.rectangle(tresh,(x,y),(w+x),h+y),((0,0,255),2)

"""
cv2.drawContours(img,cont,1,(0,0,255),3)
cv2.imshow("a",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

