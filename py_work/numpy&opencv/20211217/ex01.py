import cv2

lionimg = cv2.imread("lion.png")

center_x = lionimg.shape[1]/2
center_y = lionimg.shape[0]/2

cv2.imshow('lionimg', lionimg)
cv2.waitKey(0)



for angle in range(0,181,10):
    M= cv2.getRotationMatrix2D((center_x,center_y),angle,0.5) #10도 0.5배수
    print(M)
    warplion = cv2.warpAffine(lionimg,M,(lionimg.shape[0],lionimg.shape[1]))

    cv2.imshow('warplion',warplion)
    cv2.waitKey(0)
