import cv2
import numpy as np

resim=cv2.imread("kemalSunal.jpg")


sarilanResim=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,value=(40,50,60))
tekrarlananResim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
uzatilanResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
aynalananResim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)
cv2.imshow("aynalanan kemal sunal",aynalananResim)
cv2.imshow("uzatılan kemal sunal",uzatilanResim)
cv2.imshow("tekrarlanan kemal sunal",tekrarlananResim)
cv2.imshow("sarilan kemal sunal",sarilanResim)

cv2.waitKey(0)
cv2.destroyAllWindows()