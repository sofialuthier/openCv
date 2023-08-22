import cv2

cap=cv2.VideoCapture(0)
while True:
  
  ret,frame=cap.read()
  frame=cv2.flip(frame,1)# ters çevirme işelmi için
  kenar=cv2.Canny(frame,50,50)

  cv2.imshow("a",frame)
  cv2.imshow("c",kenar)

  if cv2.waitKey(20) & 0xFF==ord("q"):
    break
cap.release()
cv2.destroyAllWindows()