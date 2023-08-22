import cv2
import numpy as np

resim=cv2.imread("friends.jpg")
cv2.rectangle(resim,(300,200),(200,100),[0,0,255],3)

cv2.imshow("friends",resim)



cv2.waitKey(0)
cv2.destroyAllWindows()