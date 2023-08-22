import cv2
import numpy as np

resim=cv2.imread("friends.jpg")
kesit=resim[50:150,200:300]
resim[0:100,0:100]=kesit
resim[400:450,300:350]=(100,150,60)
cv2.imshow("kesit alani",kesit)
cv2.imshow("friends",resim)

resim [ :, :,0]=255 #mavinin en üst tonunu kullanır
resim [ :, :,1]=100 # yeşil için parametre
resim [ :, :,2]=80 #kırmızı için parametre


cv2.waitKey(0)
cv2.destroyAllWindows()
