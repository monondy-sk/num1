# TODO: DataFrame
# import pandas as pd
# import numpy as np

# # 列表创建DataFrame
# list = [[1,2,3],[4,5,6],[6,7,8]]
# columns=('a','b','c')          # 注意这里要是列表或元组
# df = pd.DataFrame(list,columns=columns)
# print(df)

# 字典创建DataFrame
# dict ={'姓名':['张三','李四','王五'],'年龄':[18,19,20]}
# df = pd.DataFrame(dict)         # 字典的键就默认变成了列名
# print(df)

# ndarray创建DataFrame
# arr = np.array([[1,2,3],[4,5,6],[6,7,8]])
# df = pd.DataFrame(arr)
# print(df)

# # Series创建DataFrame
# # 1. 单列df
# ser = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# df = pd.DataFrame(ser)
# print(df)
# 2. 多列df
# s1 = pd.Series(['张三','李四','王五'],name='姓名')
# s2 = pd.Series([18,19,20],name='年龄')
# df = pd.DataFrame({s1.name:s1,s2.name:s2})      # 可以看到{}包装,这不就是伪装字典吗
# print(df)

# # TODO: DataFrame的常见属性
# dict ={'姓名':['张三','李四','王五'],'年龄':[18,19,20]}
# df = pd.DataFrame(dict,index=['a','b','c'])         # 字典的键就默认变成了列名
# print(df)
# print(df.values)       # 变二维数组了
# print(df.index)
# print(df.columns)      # 列名,字典键名
# print(df.empty)
# print(df.dtypes)       # 一定要加s
# res = df.T             # 转置,行和列互换 [1,2]->[2,1]
# print(res)

# TODO: DataFrame的索引与访问
# data = {
#     '姓名': ['小明', '小红', '小刚'],
#     '年龄': [20, 18, 22],
#     '成绩': [85, 90, 88]
# }
# df = pd.DataFrame(data)

# # 列名索引访问,返回的是一个Series对象
# print(df['姓名'])
# print(df[['姓名', '年龄']])

# # loc和iloc访问单个或多个数据,切片时才会保留索引标签
# print(df.loc[0,'姓名'])
# print(df.loc[0:2,'年龄'])      # 切片时,包含起始索引和结束索引,此效果只有loc才支持
# print(df.iloc[0, 0])
# print(df.iloc[0:1, 0:1])     # 切片时,不包含结束索引，和Series切片一样

# # 获取行数据  head()和tail()
# print(df.head(2))     # 获取前2行数据
# print(df.tail(1))     # 获取后1行数据

# TODO: 数据清洗
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({
#     'A': [1, 2, np.nan],
#     'B': [4, np.nan, 6],       # np.nan是一种特定的浮点数,表示缺失值
#     'C': [7, 8, 9]
# })