import cv2
import matplotlib.pyplot as plt
import numpy as np

lionimg = cv2.imread('lion.png')
rabbitimg = cv2.imread('rabbit.png')

# 250 222
#
sumimg = cv2.add(lionimg,rabbitimg)
plt.imshow(cv2.cvtColor(sumimg,cv2.COLOR_BGR2RGB))
plt.show()
# cv2.imshow('sumimg',sumimg)
# cv2.waitKey(0)

sumnpimg = np.add(lionimg,rabbitimg)
plt.imshow(cv2.cvtColor(sumnpimg,cv2.COLOR_BGR2RGB))
plt.show()
# cv2.imshow('sumnpimg',sumnpimg)
# cv2.waitKey(0)

