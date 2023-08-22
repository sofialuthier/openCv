import cv2
import numpy as np 

resim=np.zeros((300,300,3),dtype="uint8")

cv2.line(resim,(0,0),(100,100),(0,0,255),)
cv2.circle(resim,(150,150),25,(0,255,0),2)
cv2.putText(resim,"senel",(200,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
cv2.imshow("deneme line ",resim)



cv2.waitKey(0)
cv2.destroyAllWindows()
