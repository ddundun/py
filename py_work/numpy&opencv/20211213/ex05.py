import cv2

img = cv2.imread('4.png',cv2.IMREAD_COLOR)

# h 30 w 20
# roi = img[10:40,20:40]
# cv2.imshow('roi',roi)
# cv2.waitKey(0)
#
# img[0:30,0:20] = roi
# cv2.imshow('img',img)
# cv2.waitKey(0)

cv2.imshow('img',img[:,:,0]) #한개 부분 보여주면 gray 흑백처리
cv2.waitKey(0)

img[:,:,0] = 0 # 파란색 부분 제거
cv2.imshow('img',img)
cv2.waitKey(0)