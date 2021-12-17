import cv2

img = cv2.imread('rabbit.png',cv2.IMREAD_GRAYSCALE) # 회색화

cv2.imshow('img',img) # 원래 이미지 보여주기
cv2.waitKey(0)

ret, tresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #treshold 이미지 보여주기
# 127이상 하얀색으로 반전시킨것
cv2.imshow('tresh',tresh)
cv2.waitKey(0)

adtresh = cv2.adaptiveThreshold(img,255,
                                cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY,21,3)
cv2.imshow('adtresh',adtresh)
cv2.waitKey(0)

adtresh = cv2.adaptiveThreshold(img,255,
                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY,21,3)
cv2.imshow('adtresh',adtresh)
cv2.waitKey(0)