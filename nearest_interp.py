"""
    图像采样：
        算法：最邻近插值
        图像：lenna.png 图像大小是 512*512   图像放大 800*800
        手工实现步骤：1、获取原图像 宽、高、通道
                2、获取图像缩放倍数
                3、新建缩放后尺寸目标空图像
                4、找原图像缩放操作像素点的最邻近插值点,设置该点像素值与原图该最邻近点的像素值相同
                5、使用opencv 回显缩放后的目标图像
"""

import cv2
import numpy as np

def function(image,aim_height,aim_weight):
    height,weight,channel = image.shape
    sh = aim_height/height
    sw = aim_weight/weight
    zero_image = np.zeros([aim_height,aim_weight,channel],np.uint8)

    for i in range(aim_height):
        for j in range(aim_weight):
            x = int(i/sh + 0.5)
            y = int(j/sw + 0.5)
            zero_image[i,j] = image[x,y]
            # print(i,j,x,y)

    return zero_image

img = cv2.imread("lenna.png")
aim_image = function(img,800,800)
print(aim_image)
print(aim_image.shape)
cv2.imshow("源图",img)
cv2.imshow("目标图",aim_image)
cv2.waitKey(0)
