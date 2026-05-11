# TODO: 形态学变化
"""
    形态学变化:对图像进行形态学操作,如开运算,闭运算,膨胀,腐蚀等
    腐蚀操作,去除孤立小白点(噪声)                 erode
    膨胀操作,填充小孔(填充小黑点),连接碎块         dilate
"""
# # 直接灰度化图像
# gray_img = cv2.imread('./th.jpg',cv2.IMREAD_GRAYSCALE)
# # 二值化图像
# ret,binary_img = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
# # 腐蚀操作
# kernal = np.zeros((3,3),dtype=np.uint8)
# erode_img = cv2.erode(binary_img,kernal,iterations=1)

# cv2.imshow('erode',erode_img)
# cv2.waitKey(0)

# # 结构化核
# kernal3 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))     # 矩形
# kernal4 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))    # 十字
# kernal5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))  # 圆形

# # 直接灰度化图像
# gray_img2 = cv2.imread('./th.jpg',cv2.IMREAD_GRAYSCALE)
# # 二值化图像
# ret2,binary_img = cv2.threshold(gray_img2,127,255,cv2.THRESH_BINARY)

# # 膨胀操作
# kernal2 = np.ones((5,5),np.uint8)
# dilate_img = cv2.dilate(binary_img,kernal2)

# cv2.imshow('dilate',dilate_img)
# cv2.waitKey(0)

"""
    开运算是先腐蚀后膨胀: 腐蚀削边界,去白点噪声,   膨胀再填充孔洞,连接碎块
    闭运算是先膨胀后腐蚀: 膨胀填充空洞,连接碎块,   腐蚀削边界,去白点噪声
    同时核越大效果越好
"""


# TODO:HSV 图片颜色识别
"""
    HSV与RBG不同,在颜色上更符合人的视觉体验
    色调:     范围为 0-360                  
    饱和度:   颜色的浓和淡,越高越鲜艳(0-255)   0时无色(由于H减小可能变灰)
    亮度:     颜色亮度,明亮或黑暗   (0,255)   0为黑色 (亮度),255为白色(亮度)
"""

"""
    图片颜色识别即对色调(饱和度、亮度)设置阈值.
    使用cv2.inrange生成二值掩膜(白黑),再来个位与运算bitwise_and就可以了
"""
# img = cv2.imread('./th.jpg')
# # 转hsv图像数组
# hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# # 掩膜阈值范围设置
# lower = np.array([26,43,46])
# upper = np.array([34,255,255])

# # 生成掩膜
# mask = cv2.inRange(hsv_img,lower,upper)

# # 位与运算
# yellow_img = cv2.bitwise_and(img,img,mask=mask)

# cv2.imshow('img',img)
# cv2.imshow('yellow_img',yellow_img)
# cv2.waitKey(0)

# TODO: 图片颜色替换
# img = cv2.imread('./th.jpg')

# hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# # 选择区域
# lower = np.array([26,43,46])
# upper = np.array([34,255,255])
# mask = cv2.inRange(hsv_img,lower,upper)

# # 开运算(将连接的断开先腐蚀后膨胀)
# kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

# # erode_img = cv2.erode(mask,kernal)
# # open_img = cv2.dilate(erode_img,kernal)
# open_img = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)    #二合一：开运算

# # 选择替换
# # for i in range(open_img.shapopene[0]):
# #     for j in range(open_img.shape[1]):
# #         if open_img[i][j] == 255:
# #             hsv_img[i][j] = (0,0,0)
# hsv_img[open_img == 255] = (0,0,0)
# # 注意得到的hsv是不能直接imshow,因为格式不是BGR,   除非改原图 img[open_img == 255] = (0,0,0)
# img1 = cv2.cvtColor(hsv_img,cv2.COLOR_HSV2BGR)

# cv2.imshow('hsv_img',hsv_img)
# cv2.imshow('img1',img1)
# cv2.waitKey(0)