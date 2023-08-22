import cv2

img=cv2.imread("ucgen.png")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ai,tresh=cv2.threshold(gri,100,200,cv2.THRESH_BINARY)

n=cv2.moments(tresh)
#print(n)
x=int(n["n10"]/n["n00"])
y=int(n["n01"]/n["n00"])

cv2.circle(img,(x,y),10,(255,0,0),-1)
#sondaki -1 daiirenin içimim dolu olduüunu gösterir.
dim=(500,500)

resize=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("s",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()