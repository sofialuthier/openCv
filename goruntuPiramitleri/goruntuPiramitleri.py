import cv2 
import numpy as np

resim= cv2.imread("kemalSunal.jpg")
ikiKat=cv2.pyrUp(resim)
ikiKatKucuk=cv2.pyrDown(resim)



print("iki  kat kucuk resim",ikiKatKucuk.shape)
print("orjinal resim",resim.shape)
print("iki kat buyuk resim",ikiKat.shape)
cv2.imshow("orjinal resim",resim)
cv2.imshow("iki kat buyuk resim ",ikiKat)
cv2.imshow("iki kat kucuk resim ",ikiKatKucuk)

cv2.waitKey(0)
cv2.destroyAllWindows()