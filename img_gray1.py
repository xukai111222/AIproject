import cv2
# from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from PIL import Image

"""图片手工灰度处理"""
img = cv2.imread("lenna.png")

h , w = img.shape[:2]
img_gray = np.zeros([h,w],img.dtype)
img_binary = np.zeros([h,w],img.dtype)

for i in range(h):
    for j in range(w):
        m = img[i,j]
        img_gray = (m[0]*0.11 + m[1]*0.59 + m[2]*0.3)
        if (img_gray[i,j] <= 0.5):
            img_binary[i,j] = 0
        else:
            img_binary[i,j] = 1

print(img_gray)
print(img_binary)

plt.subplot(221)
plt.imshow(img)

plt.subplot(222)
plt.imshow(img_gray,cmap='gray')

plt.subplot(223)
plt.imshow(img_binary,cmap='gray')

# 显示图片
plt.show()


