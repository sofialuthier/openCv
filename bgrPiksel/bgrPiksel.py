import cv2
import numpy as np

opelResmi=cv2.imread("opel.jpg")

cv2.imshow("opel resmi",opelResmi)

print(opelResmi[(30,80)])

print("resmin boyutu:"+ str(opelResmi.size))
print("resmin özellikleri:"+str (opelResmi.shape))
print("resmin veri tipi:"+str(opelResmi.dtype))


cv2.waitKey(0)
cv2.destroyAllWindows(0)