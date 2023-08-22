import cv2
import numpy as np


resim1=cv2.imread("friends.jpg")
resim2=cv2.imread("kemalSunal.jpg")

print(resim1[100,200])
print(resim2[100,200])


cv2.imshow("friends",resim1)
cv2.imshow("kemal sunal",resim2)
print(resim1[100,200]+resim2[100,200])

cv2.waitKey(0)
cv2.destroyAllWindows()