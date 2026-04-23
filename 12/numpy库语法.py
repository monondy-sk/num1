# 创建随机数数组
import numpy as np

# TODO: 创建随机数数组
# np.random.seed(10)      # 固定随机种子,每次运行结果都相同

# a1 = np.random.rand(2,3)        # 形状为(2,3)的随机数数组,默认在[0,1)区间中采样float类型
# print(a1)

# a2 = np.random.random((2,3))    # 形状为(2,3)的随机数数组,默认在[0,1)区间中采样float类型
# print(a2)

# a3 = np.random.randn(5,2)    # 从标准正态分布中采样,默认均值为0,标准差为1
# print(a3)

# a4 = np.random.randint(0,10,size=(2,3))  # 从[0,10)区间中采样,默认包含0,不包含10
# a5 = np.random.randint(10,size=(2,3))    # 从[0,10)区间中采样一个整数,默认包含0,不包含10
# print(a4)
# print(a5)

# a6 = np.random.uniform(0,10,size=(2,3))    # 从[0,10)区间中采样,默认包含0,不包含10
# a7 = np.random.uniform(10,size=(2,3))    # 从[0,10)区间中采样,默认包含0,不包含10
# print(a6)
# print(a7)

# a8 = np.ones(8)
# np.random.shuffle(a8)    # 随机打乱数组的元素,改变原数组,只能操作一维数组
# print(a8)


# TODO: ndarray数组的运算

# a = np.array([11,12,13])
# b = np.array([1,2,3])       # 一维多维皆可进行运算

# # 加
# print(a+b)
# print(np.add(a,b))         #效果与a+b相同
# # 减
# print(a-b)
# print(np.subtract(a,b))    #效果与a-b相同,注意顺序不能改变
# # 乘
# print(a*b)
# print(np.multiply(a,b))    #效果与a*b相同
# # 除
# print(a/b)
# print(np.divide(a,b))      #效果与a/b相同,有小数类型转换为float类型
# # 指数
# print(a**b)
# print(np.power(a,b))      #效果与a**b相同,注意顺序不能改变

# # 点积
# print(np.dot(a,b))    # 点积为11*1+12*2+13*3=74
# # 二维数组的点积
# a = np.array([[1,2,3],
#               [4,5,6]])
# b = np.array([[1,2],
#               [3,4],
#               [5,6]])
# print(np.dot(a,b))        # [[22 28]    #相当于矩阵的点积
#                           #  [49 64]]

# 广播机制相当于给低维的数组添加维度(高维为1),使它们的维度相同,然后进行运算

# # squeeze()函数,删除数组中所有为1的维度
# a = np.array([[1,2,3]])
# print(a)
# print(a.shape)
# b=np.squeeze(a)         # 删除所有为1的维度,返回一个一维数组
# print(b)
# print(b.shape)          # (3,)

# # expand_dims()函数,在数组的指定轴上添加一个维度(高维为1)
# a = np.array([1,2,3])
# print(a)
# print(a.shape)
# b=np.expand_dims(a,axis=(0,1))  # 在第0轴上添加两个维度,返回一个2维数组
# print(b)                    # [[[1 2 3]]]
# print(b.shape)              # (1,1,3)

# TODO:numpy连接删除函数
# # concatenate()函数,连接数组       #规则： 除了被连接的轴,其他轴的维度必须相同
# a = np.array([[1,2],
#               [3,4],
#               [5,6]])
# b = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
# c = np.concatenate((a,b),axis=1)  # 在第1轴上连接,返回一个3维数组,不指定轴默认在第0轴上连接
# print(c)
# print(c.shape)                    # (3,5) ,5=2列+3列

# # stack()函数,将数组按指定轴上连接,返回一个新数组
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# c = np.stack((a,b),axis=1)        # 在第1轴上连接,返回一个2维数组,不指定轴默认在第0轴上连接
# print(c)                          # 会自动添加一个维度
# print(c.shape)                    # (3,2) ,3行2列

# # hstack()函数,将数组按水平方向堆叠,不改变数组的维度,axis=1
# a = np.array([[1,2,3],
#               [4,5,6]])
# b = np.array([[7,8,9],
#               [10,11,12]])
# c = np.hstack((a,b))        # 在第1轴上堆叠,返回一个2维数组
# print(c)
# print(c.shape)              # (2,6) ,2行6列

# # vstack()函数,将数组按垂直方向连接,返回一个新数组,即axis=0
# a = np.array([[1,2,3],
#               [4,5,6]])
# b = np.array([[7,8,9],
#               [10,11,12]])
# c = np.vstack((a,b))        # 在第0轴上堆叠,返回一个2维数组
# print(c)
# print(c.shape)              # (4,3) ,4行3列

# # split()函数,将数组按指定轴上分割,返回一个列表
# a = np.array([[1,2,3],
#               [4,5,6]])
# b = np.split(a,2,axis=0)      # 将a按第0轴(默认轴)上分割,2表示将a分为2份,每个元素为一个数组
# c = np.split(a,[1],axis=0)    # 将a按第0轴(默认轴)上分割,[1]即在1的索引上分割,每个元素为一个数组
# print(b)
# print(c)

# # hsplit()函数,将数组按水平方向分割,返回一个列表
# a = np.array([[1,2,3],
#               [4,5,6]])
# b = np.hsplit(a,3)      # 将a按第1轴(默认轴)上分割,3表示将a分为3份,每个元素为一个数组
# print(b)

# # vsplit()函数,将数组按垂直方向分割,返回一个列表
# a = np.array([[1,2,3],
#               [4,5,6]])
# b = np.vsplit(a,[1])      # 将a按第0轴(默认轴)上分割,[1]即在1的索引上分割,每个元素为一个数组
# print(b)

"""
    总结:concatenate()连接数组,hstack()1位连接,vstack()0位连接,而stack加新维度
         split()函数分割数组,hsplit()1位分割,vsplit()0位分割
"""
# # append()函数,在数组的指定轴上添加一个元素,返回一个新数组
# a = np.array([[1,2,3],
#               [4,5,6]])
# b = np.array([[7,8],
#               [9,10]])
# c = np.append(a,b,axis=1)    # b类似于concatenate()函数
# print(c)
# d = np.array([[7,8],
#               [9,10]])
# e = np.append(a,d)           # 现在没有axis参数,那么就会被展平再追加
# print(e)

# # insert()函数,在数组的指定轴上插入一个元素,返回一个新数组
# a=np.array([[1,2,3],
#             [4,5,6]])
# b=np.array([[7,8,9]])
# c=np.insert(a,2,b,axis=0)          # 2即索引 a[2]后插入b数组
# print(c)

# # delete()函数,删除数组的指定轴上的元素,返回一个新数组
# a=np.array([[1,2,3],
#             [4,5,6]])
# print(a[1])
# b=np.delete(a,1,axis=0)          # 1即索引 a[1]被删除
# print(b)

# TODO:numpy统计计算
"""
    注意:anxi
    这里的统计计算于之前使用axis参数不同
    之前的是按axis轴进行追加,删除,分割等  
    下面的例子展示了按axis轴进行统计计算的区别

    ！！！！！！！！！！！！！真言:axis选择哪一维,就会去掉那一维(即计算那一维)非常重要！！！！！！！！！！

"""
# a=np.array([[1,2,3],
#             [4,5,6]])
# b=np.array([[7,8,9]])
# c=np.array([[7,8],
#             [9,10]])
# d2=np.concatenate((a,b),axis=0)   # 可以看到是在0轴上连接了, 操作了行
# d1=np.concatenate((a,c),axis=1)   # 可以看到是在1轴进行拼接, 操作了列
# print(d1)
# print(d2)
# e=np.mean(a,axis=0)        # 按0轴进行均值计算,这里是对轴进行计算了，(不是操作)
# print(e)                   # 0为行,即对每行第一个元素进行均值计算, 计算了列

# # mean()函数,计算数组的均值
# a=np.array([[1,2,3],
#             [4,5,6]])
# print(a.mean())            # 计算数组a的均值
# print(a.mean(axis=0))      # 按0轴(默认轴)上计算,返回一个1维数组,每个元素为第0轴上的均值

# #sum()函数,计算数组的元素和
# a=np.array([[1,2,3],
#             [4,5,6]])
# print(a.sum())            # 计算数组a的所有元素的和
# print(a.sum(axis=0))      # 按0轴(默认轴)上计算,返回一个1维数组,每个元素为第0轴上的和
# # sum()函数多维计算
# b=np.array([                 #此处为两个2行3列的数组(2,2,3)
#             [
#              [1,2,3],
#              [4,5,6]
#             ],
#             [
#              [7,8,9],
#              [10,11,12]
#             ]
#            ])
# print(b.sum(axis=0))         # 那么统计0轴时,结果必须是(2,3)的数组
# print(b.sum(axis=1))         # 那么统计1轴时,结果必须是(2,3)的数组
# print(b.sum(axis=2))         # 那么统计2轴时,结果必须是(2,2)的数组

# # max()函数,计算数组的最大值
# a=np.array([[1,2,3],
#             [4,5,6]])
# print(a.max())            # 计算数组a的最大值
# print(a.max(axis=0))      # 按0轴上计算,返回一个1维数组,每个元素为第0轴上的最大值
# print(a.max(axis=1))      # 按1轴上计算,返回一个1维数组,每个元素为第1轴上的最大值

# # min()函数,计算数组的最小值
# a=np.array([[1,2,3],
#             [4,5,6]])
# print(a.min())            # 计算数组a的最小值
# print(a.min(axis=0))      # 按0轴上计算,返回一个1维数组,每个元素为第0轴上的最小值
# print(a.min(axis=1))      # 按1轴上计算,返回一个1维数组,每个元素为第1轴上的最小值

# # var()函数,计算数组的方差
# a=np.array([[1,2,3],
#             [4,5,6]])
# print(a.var())            # 计算数组a的方差
# print(a.var(axis=0))      # 按0轴上计算,返回一个1维数组,每个元素为第0轴上的方差
# print(a.var(axis=1))      # 按1轴上计算,返回一个1维数组,每个元素为第1轴上的方差

# # argmax()函数,计算数组的最大值的索引
# a=np.array([[1,2,3],
#             [4,5,6]])
# print(a.argmax())            # 计算数组a的最大值的索引
# print(a.argmax(axis=0))      # 按0轴上计算,返回一个1维数组,每个元素为第0轴上的最大值的索引
# print(a.argmax(axis=1))      # 按1轴上计算,返回一个1维数组,每个元素为第1轴上的最大值的索引

