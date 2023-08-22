import cv2
import numpy as np 

kemalSunal=cv2.imread("kemalSunal.jpg")
kemalSunal[40:70,90:160,0]=255
kemalSunal[40:70,90:160,1]=200

#rgb değerlerini değiştirmek için yapılan kod
#kemalSunal[:,:,0]=250 #mavi
#kemalSunal[:,:,1]=80 #sarı
#kemalSunal[:,:,2]=20 #kırmızı

cv2.imshow("kemal sunal fotografi",kemalSunal)

cv2.waitKey(0)
cv2.destroyAllWindows()