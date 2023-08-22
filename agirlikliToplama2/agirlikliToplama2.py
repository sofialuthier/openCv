import cv2
import numpy as np


resim1=cv2.imread("opel.jpg")
resim2=cv2.imread("sedan.jpg")

#iki resiminde pikselleri ve boyutları aynı olamalıdır.



cv2.imshow("opel",resim1)
cv2.imshow("sedan",resim2)
toplam=cv2.add(resim1,resim2)
agirlikliToplam=cv2.addWeighted(resim1,0.7,resim2,0.3)

cv2.imshow("toplanmıs resimler",toplam)
cv2.imshow("agirlirlitoplama ",agirlikliToplam)
#iki resmin aynı pikselde olmaması hata verir.

cv2.waitKey(0)
cv2.destroyAllWindows()