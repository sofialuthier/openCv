import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True :
    ret,goruntu=kamera.read()




    
    cv2.rectangle(goruntu,(200,200),(300,200),(0,0,255),4)
    cv2.line(goruntu,(0,0),(200,200),(0,0,255),4)
    cv2.circle(goruntu,(300,300),25,(0,0,255),4)
    cv2.imshow("senel",goruntu)

    if cv2.waitKey(25)& 0xFF ==('q'):
        break
kamera.release()
cv2.destroyAllWindows()