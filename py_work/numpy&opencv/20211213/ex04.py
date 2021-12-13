import time
import cv2

img = cv2.imread('4.png',cv2.IMREAD_COLOR)

start_time = time.time()
# for i in range(10):
#     for j in range(10):
        # img[i,j] = [255,255,255]
        # img[i,j] = [255,0,0]
img[0:10,0:10] = [255,0,0]
end_time = time.time()
print('걸린시간',end_time-start_time)

cv2.imshow('title',img)
cv2.waitKey(0)
cv2.imwrite('4blue.png',img)