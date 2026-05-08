import cv2
import numpy as np
import matplotlib.pyplot as plt
# # TODO: RGB彩图了解
# # 创建一个700*700的3通道图像，通道数为3，数据类型为uint8,每个通道1字节（8位）
# img = np.zeros((700,700,3),dtype=np.uint8)

# block_size = 100
# for i in range(0,700,block_size):
#     for j in range(0,700,block_size):
#         if (i/100)%2 == 0:
#             img[i:i+block_size,j:j+block_size,0] = 255
#             img[i:i+block_size,j:j+block_size,1] = 255
#             img[i:i+block_size,j:j+block_size,2] = 255
#         else:
#             img[i:i+block_size,j:j+block_size,0] = 0

# # cv2原始显示是bgr，plt显示是rgb，所以需要cv2.cvtColor转换一下
# image_rbg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# # 加入plt.imshow()函数，将img显示在plt窗口中
# plt.imshow(image_rbg)
# plt.show()

# # cv2.imshow('img',img)
# # cv2.waitKey(0)

# # 修改图像像素值
# img[:,:,2] = 255
# img[1:34,:,:] = (255,0,0)
# # 获取原图像素值
# # 1.切片获取像素值
# b = img[100,100,0]
# g = img[100,100,1]
# r = img[100,100,2]
# # 2.使用cv2 的split
# b,g,r = cv2.split(img)

# # rectangle
# # |-----x
# # |
# # y
# left_top = (j,i)    # j 表示x轴方向（列），i 表示y轴方向（行）
# right_bottom = (j+block_size,i+block_size)
# # 对角线绘制矩形    # 三通道    # 2px宽（-1表示实心填充）
# cv2.rectangle(img,left_top,right_bottom,(0,255,0),2)

# TODO: 灰度图了解
"""
    灰度图:只包含一个通道,每个像素值为0-255之间的整数,用于表示图像的灰度等级
    灰度图的通道数为1,数据类型为uint8,每个通道1字节(8位)
"""
"""
    彩色图转灰度图
    1.cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  加权平均值公式:gray = 0.299 * R + 0.587 * G + 0.114 * B
    2.直接取平均值:gray = (R + G + B) / 3    
    3.最大值:gray = max(R,G,B)             # 适合颜色偏黑白的图像

"""
# # 读取完是一个np数组
# img = cv2.imread('th.jpg',cv2.IMREAD_COLOR)
# # 获取图像的高、宽、通道数
# img_shape = img.shape

# # 灰度图模板   # 高即为行数，宽即为列数
# image_gray = np.zeros((img_shape[0],img_shape[1]),dtype=np.uint8)


# b,g,r = cv2.split(img)
# print(b.shape)


# # 加权平均法  # 0.299 * R + 0.587 * G + 0.114 * B
# red = 0.299
# green = 0.587
# blue = 0.114

# image_gray = (b*blue + g*green + r*red).astype(np.uint8)


# # # 填充像素
# # for i in range(img_shape[0]):
# #     for j in range(img_shape[1]):
# #         image_gray[i,j] = round(img[i,j,0]*blue + img[i,j,1]* green + img[i,j,2]*red)

# # print(image_gray[:,:])

# # cv2.imshow('image',img)

# cv2.imshow('image_gray',image_gray)

# cv2.waitKey(0)