import cv2
import numpy as  np


resim=cv2.imread("joker.jpg")
resimGri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY) #resmi griye çevirmek iöin convert etmek gerekir.

yukseklik,genislik=resimGri.shape 
#atama sağdan sola yapılarak yüksekliği,genişliği ve kanal sayısı alınır (kanal sayısı en fazla üç olabilir bunlar mavi,yeşil ve kırmızı rgb renkleridir.) 

yukseklik,genislik,kanalsayisi=resim.shape
print("gri resim",yukseklik,genislik)
print("orjinal resim",yukseklik,genislik,kanalsayisi)


cv2.imshow("orjinal",resim)
cv2.imshow("grilestirilmis resim",resimGri)


cv2.waitKey(0)
cv2.destroyAllWindows()