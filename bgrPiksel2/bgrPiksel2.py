import cv2
import numpy as np

resim= cv2.imread("joker.jpg")

resim[20,30]=[0,0,0]
for i in range(100):
    resim[70,i]=[255,255,255]
cv2.imshow("joker",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()