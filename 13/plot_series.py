import matplotlib.pyplot as plt
import numpy as np

# TODO: 线图
# 绘制一个简单的折线图
# plt.plot([1,2,3,4,5],[1,4,9,16,25],'--')
# plt.show()

# # 绘制一个简单的折线图,绘制sin函数
# x=np.arange(0,3*np.pi,0.1)
# y=np.sin(x)
# plt.plot(x,y)              # plot()
# plt.show()

# # 绘制一个简单的折线图,绘制cos函数
# x=np.arange(0,5*np.pi,0.1)      # 从0到5π,步长为0.1     步长越小,曲线越平滑
# x2=np.arange(0,5*np.pi,0.8)     # 可以看到已经不平整了
# y=np.cos(x2)
# plt.plot(x2,y,
#          color='red',
#          linewidth=2,
#          linestyle='--',
#          alpha=0.5
#          )
# plt.show()

# 如果多个折线,可用legend()搭配labels参数表示多个线

# TODO:散点图
# x = np.arange(0,3*np.pi,0.1)
# y = np.sin(x)
# plt.scatter(x,y)            # scatter()  可以看到,散点图全是点,而不是连续的线
# plt.show()

# TODO:条形图
# labels = ['A','B','C','D']
# values = [1,2,3,4]
# plt.bar(labels,values)      # bar()
# plt.show()

# TODO:饼图
# labels = ['A','B','C','D']
# values = [1.5,2,3,4]
# colors = ['red','green','blue','yellow']
# plt.pie(values,               # pie()
#         labels=labels,
#         colors=colors,
#         )
# plt.show()

# TODO:其它常见函数  subplot()   tight_layout()
# x=np.arange(0,3*np.pi,0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.subplot(2,1,1)          # 2行1列,第三个参数表示第1个子图
# plt.title('sin(x)')         # 标题
# plt.xlabel('x')             # x轴标签
# plt.ylabel('sin(x)')        # y轴标签
# plt.plot(x,y1)

# plt.subplot(2,1,2)          # 第2个子图
# plt.title('cos(x)')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.plot(x,y2)

# plt.tight_layout()           # 调整子图间距
# plt.show()

# TODO: pandas之Series

# import pandas as pd
# import numpy as np

# # Series的创建
# a = 1                  # 标量创建Series
# ser = pd.Series(a)
# print(ser)

# list = [1,2,3,4,5]     # 列表创建Series
# indexs = ['a','b','c','d','e']     # 自定义索引(标签),不指定默认从0开始递增
# ser = pd.Series(list,index=indexs)
# print(ser)

# arr = np.arange(5)     # 数组创建Series
# ser = pd.Series(arr,copy=True)   # 默认索引为0,1,2,3,4  copy=True表示深拷贝,不引用了
# print(ser)

# dict = {'a':1,'b':2,'c':3}   # 字典创建Series
# ser = pd.Series(dict)        # 默认索引为字典的键
# print(ser)
# print(ser[2])

# 常见属性
# ser = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# print(ser.values)
# print(ser.index)
# print(ser.dtype)
# print(ser.empty)

# Series的索引与访问
# ser = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# # 位置索引
# print(ser[0])

# # 标签索引
# print(ser['a'])

# #切片
# print(ser['a':'c'])    # 切片时,包含起始索引和结束索引
# print(ser[1:3])        # 切片时,不包含结束索引

# TODO: DataFrame
import pandas as pd
import numpy as np



