import cv2
import numpy as np

img= cv2.imread("ucgen.png") 

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gri=np.float32(gri)
corner=cv2.goodFeaturesToTrack(gri,10,0.01,10)  
corner=np.int0(corner)

for c in corner:
    x,y=c.ravel() #düzleştirme işlemi
    cv2.circle(img,(x,y),3,(255,0,0),3)
   
dim=(400,400)
resize=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("u",resize)

cv2.waitKey(0)
cv2.destroyAllWindows()