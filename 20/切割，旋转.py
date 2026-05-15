# TODO: 形态切割
# img = cv2.imread('./th.jpg')
# #获取高和宽
# h,w,a = img.shape
# print(f"{h},{w}")
# # 定义范围,此处的x为x轴方向
# x_min,x_max = 40,100
# y_min,y_max = 80,120

# try :
#     if not ((x_min>0 and x_max<w) and (y_min>0 and y_max<h)):
#         raise OverflowError("超边界")   #手动抛出异常同样需要捕获
#     rctg = cv2.rectangle(img,(x_min,y_min),(x_max,y_max),(0,0,255),2) # 画框

#     # 切割即切片
#     rec_img = img[y_min:y_max,x_min:x_max]
#     print(f"{rec_img.shape[0]},{rec_img.shape[1]}")

#     cv2.imshow('retg',rctg) #某些版本=img
#     cv2.imshow('img',img)

#     cv2.imshow('rec_img',rec_img)
#     cv2.waitKey(0)
# except Exception as e:
#     print(e)

# TODO:图像旋转

"""
    1.真正的旋转矩阵,getRotationMatrix2D 生成含平移的仿射矩阵
    2.插值填充,     cv2.INTER_LINEAR(双线性,默认)
    3.边界填充,     镜像反射(cv2.BORDER_REFLECT),复制,固定值
"""

# img = cv2.imread('./th.jpg')

# h,w = img.shape[0:2]

# # 先生成旋转矩阵
# center = (w//2,h//2)
# angel = 45
# scale = 1
# M = cv2.getRotationMatrix2D(center,angel,scale)

# # 对图片进行插值处理的方式,图片放大时特别有用
# mode = cv2.INTER_LINEAR


# # 执行仿射变换(旋转)
# rotation_img = cv2.warpAffine(img,M,      # 旋转矩阵
#                               (w,h),      # 输出的img大小
#                               flags=mode, # 插值方式
#                               borderMode=cv2.BORDER_REFLECT) # 边界填充方式
# cv2.imshow('img',img)
# cv2.imshow('rotation',rotation_img)
# cv2.waitKey(0)

# 图像翻转 flip

# img = cv2.imread('./th.jpg')

# h,w = img.shape[0:2]

# index_img = cv2.flip(img,1)  # 1 水平翻转(列变换)

# lie_img = cv2.flip(img,0)    # 0 依旧行变换，竖直翻转

# all_img = cv2.flip(img,-1)   # -1 都变

# i_img = cv2.flip(img)

# cv2.imshow('水平',index_img)
# cv2.imshow('竖直',lie_img)
# cv2.imshow('镜像',all_img)

# cv2.waitKey(0)
