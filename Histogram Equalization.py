



import cv2
import numpy as np
import matplotlib.pyplot as plt

# 获取原图
img = cv2.imread("lenna.png")

# 图像灰度处理
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 灰度图进行直方图均衡化处理
dst = cv2.equalizeHist(gray)

# 计算直方图
# hist = cv2.calcHist([dst],[0],None,[256],[0,256])

# 显示灰度图直方图 和 直方图均衡化处理后的直方图
plt.figure()
plt.hist(gray.ravel(),256)
plt.figure()
plt.hist(dst.ravel(),256)
plt.show()

# 展示灰度图和直方图均衡化处理后的灰度图
cv2.imshow("灰度图 + 灰度图均衡化后效果图",np.hstack([gray,dst]))
cv2.waitKey()

