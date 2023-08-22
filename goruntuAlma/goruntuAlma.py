import cv2 as cv 
import numpy as np 

kamera=cv.VideoCapture(0) # kendi bilgisayarımla ytanımla olan kamerayı alır.
# 1,usb # 2 videodan görüntü

while True:
    ret,goruntu=kamera.read()
    cv.imshow("senel",goruntu)

    if cv.waitKey(30)& 0xff ==('q'):
        break
    
kamera.release()


cv.destroyAllWindows()