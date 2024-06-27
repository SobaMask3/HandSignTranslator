import cv2

img = cv2.imread("/home/wtc1/Desktop/HStranslator/src_imgs/dog.jpeg",cv2.IMREAD_ANYCOLOR)
cv2.imshow("Dog",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
