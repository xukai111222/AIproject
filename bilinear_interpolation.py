"""
    图像采样：
        算法：双线性插值
        图像：lenna.png 图像大小是 512*512   图像放大 700*700
        手工实现步骤：1、获取原图像 宽、高、通道
                2、定义目标图像宽、高
                3、判断给定的目标图像宽高与源图像宽高是否相等，如相等则返回源图像的复制图像
                4、新建空白图像，计算目标图像相对源图像的缩放倍数
                5、进入循环遍历目标图像的通道、像素点
                6、循环内：
                    6.1、对目标图像坐标系与源图像坐标系进行几何中心对称
                    6.2、找到目标图像像素点相对源图像所在的插入虚拟像素点周围的四个点坐标（得到虚拟店像素值被周围点影响的权重）
                    6.3、套用双线性插值公式计算 f(R1) 、f(R2) ,最后得出 f(x,y) ,即得到目标图像像素点的像素值
                7、遍历完成，返回目标图像
                8、调用函数，展示目标图像
"""
import cv2
import numpy as np

def bilinear_interpolation(img,aim_h,aim_w):
    src_h , src_w ,channel = img.shape

    if aim_h == src_h and aim_w == src_w:
        return img.copy()

    aim_img = np.zeros((aim_h,aim_w,channel),dtype=np.uint8)
    scale_x ,scale_y = float(src_w/aim_w) , float(src_h/aim_h)

    for i in range(channel):
        for aim_y in range(aim_h):
            for aim_x in range(aim_w):
                # 几何中心对称
                src_x = (aim_x + 0.5)*scale_x - 0.5
                src_y = (aim_y + 0.5)*scale_y - 0.5

                # 找到插值周围坐标点，同时防止坐标值越界，即超过图像高度或宽度(src_w - 1)
                src_x0 = int(np.floor(src_x))
                src_x1 = min(src_x0 + 1,src_w - 1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1,src_h - 1)

                # 在x 方向做插值 (x1 - x0 = 1)计算时不写,img[src_x0,src_y0,1] ---> (x0,y0)对应的像素值
                insert_x0 = (src_x1 - src_x)*img[src_y0,src_x0,i] + (src_x - src_x0)*img[src_y0,src_x1,i]
                insert_x1 = (src_x1 - src_x)*img[src_y1,src_x0,i] + (src_x - src_x0)*img[src_y1,src_x1,i]

                # 在y方向做插值，确定虚拟像素点像素值并赋值给缩放后实际像素点
                aim_img[aim_y,aim_x,i] = int((src_y1 - src_y)*insert_x0 + (src_y - src_y0)*insert_x1)

    return aim_img

img = cv2.imread("lenna.png")
dst_img = bilinear_interpolation(img,700,700)
cv2.imshow("source image",img)
cv2.imshow("destination iamge",dst_img)
cv2.waitKey()







