import cv2

img_basic = cv2.imread('4.png',cv2.IMREAD_COLOR)
cv2.imshow('basic',img_basic)
cv2.waitKey(0)
cv2.imwrite('4_c1.png',img_basic)

img_gray = cv2.cvtColor(img_basic,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',img_gray)
cv2.waitKey(0)
cv2.imwrite('4_gray.png',img_gray)