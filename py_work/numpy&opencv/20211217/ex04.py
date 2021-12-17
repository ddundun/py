import cv2

hid_img = cv2.imread('hid.jpg',cv2.IMREAD_GRAYSCALE)

print(hid_img[0,0])
print(hid_img[0,1])
print(hid_img[0,2])
print(hid_img[0,3])
print(hid_img[0,4])
print(hid_img[0,5])
cv2.imshow('hid_img',hid_img)
cv2.waitKey(0)

# 임계점처리

ret, tresh_img = cv2.threshold(hid_img,75,255,cv2.THRESH_BINARY)
# 0은 검정 75이상은 다 0처리 ?#
# tresh_img[0:30,0:30] =255
# 0 1 값만 -> 흰색 검은색~
cv2.imshow('tresh_img',tresh_img)
cv2.waitKey(0)

ret, tresh_img = cv2.threshold(hid_img,75,255,cv2.THRESH_BINARY_INV)
# 인벌스 -> 위에거 반대
cv2.imshow('tresh_img',tresh_img)
cv2.waitKey(0)

ret, tresh_img = cv2.threshold(hid_img,75,255,cv2.THRESH_TRUNC)
# 75이상인부분 75처리
cv2.imshow('tresh_img',tresh_img)
cv2.waitKey(0)

ret, tresh_img = cv2.threshold(hid_img,75,255,cv2.THRESH_TOZERO)
# 바이너리 반대 75이상 0?
cv2.imshow('tresh_img',tresh_img)
cv2.waitKey(0)


ret, tresh_img = cv2.threshold(hid_img,75,255,cv2.THRESH_TOZERO_INV)
# 75이상 그대로놔두고 나머지 인벌스처리
cv2.imshow('tresh_img',tresh_img)
cv2.waitKey(0)