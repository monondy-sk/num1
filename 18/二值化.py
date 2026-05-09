import cv2
import numpy as np
# TODO:二值化
"""
    阈值法二值化:固定阈值
    自适应二值化:通过算法算出阈值,如otsu 是全局型,平均值和高斯是局部型自适应算法
"""
# 1.阈值法二值化
"""
    将灰度图变成两种颜色的二值化图(截断可多种) otsu算法可算出合适的阈值(最大类间方差最适合分割前景后景)
    1.阈值法(最大,反)   阈值thresh  最大值maxval
    2.截断法    阈值thresh

"""

# image = cv2.imread('./th.jpg')     # 获取图像

# gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  # 转灰度图

# thresh = 127   # 阈值
# maxval = 255   # 最大值

# # otsu算法是通过组合加入  threshold生成二值图像数组
# ret , image_binary = cv2.threshold(gray_image,thresh,maxval,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# print(ret)
# print(image_binary)
# cv2.imshow('img',image_binary)  # 前面全部都是np数组，imshow显示图像
# cv2.imshow('img_gray',gray_image)
# cv2.waitKey(0)

# cv2.imwrite('th1.jpg',image_binary)

# 2.自适应二值化
"""
    通过核对每个像素点进行局部计算阈值(otsu是全局)
    1.mean         平均值
    2.GAUSSIAN     高斯
"""
img = cv2.imread('./th.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

block_size = 9

binary_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, 5)

cv2.imshow('gray', gray_img)
cv2.imshow('binary', binary_img)
cv2.waitKey(0)