import cv2

#rgb가 아니라 bgr순서대로 받아옴
img = cv2.imread('4.png',cv2.IMREAD_COLOR)

print(img.shape)
print(img[20,20])

cv2.imshow('창의제먹',img)
retvalue =cv2.waitKey(0) # 사용자의 키입력 기다리는중
print(retvalue)
if retvalue == 49:
    print("1을 입력했네요")

if retvalue == 50:
     print("2을 입력했네요")
cv2.imwrite('4_copy.png',img)


