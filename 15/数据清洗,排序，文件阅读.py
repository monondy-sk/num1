# df = pd.DataFrame({
#     'A': [1, 2, np.nan],
#     'B': [4, np.nan, 6],       # np.nan是一种特定的浮点数,表示缺失值
#     'C': [7, 8, 9]
# })

# # 1. 缺失值检测 isnull
# print(df.isnull())

# # 2. 删除缺失值 dropna
# df_d1 = df.dropna(axis=0,how='any')  # axis=0表示删除行,how='any'表示删除包含缺失值的行
# print(df_d1)
# df_d2 = df.dropna(axis=1,thresh=2)  # axis=1表示删除列,thresh=2表示至少包含2个非缺失值,才保留该列
# print(df_d2)

# # 3. 填充缺失值 fillna
# df_f1 = df.fillna(value=0)   # 标量填充
# print(df_f1)

# df_f2 = df.fillna(method='ffill')   # 前向填充,第一个没有就炸了
# print(df_f2)

# df_f3 = df.fillna(method='bfill')   # 后向填充,最后一个没有就炸了
# print(df_f3)

# df_f4 = df.fillna(value={'A':0,'B':1,'C':2})   # 指定列填充指定值
# print(df_f4)

# df_f5 = df.fillna(value=0,limit=1)   # 每行或列缺失值最多填充1个0
# print(df_f5)s

# # 4.删除重复行  drop_duplicates
# df = pd.DataFrame({
#     'A': [1, 1, 2, 2, 3, 3],
#     'B': [1, 1, 2, 2, 3, 3],
#     'C': [1, 1, 2, 2, 3, 3]
# })
# # 删除重复行,保留第一次出现的重复项,且不改变行索引标签
# df_dedup_first = df.drop_duplicates()
# print(df_dedup_first)
# # 根据指定列删除重复行
# df_dedup_column = df.drop_duplicates(subset=['A'])
# print(df_dedup_column)

# TODO: 数据转换
import pandas as pd
import numpy as np

# # 1.替换值 replace
# a = pd.DataFrame({'A':[1,2,3],'B':[4,5,'不神']})
# a.replace(to_replace=1,value=100,inplace=True)        # inplace=True表示原地替换
# print(a)
# a.replace([2,3],15,inplace=True)
# print(a)
# a.replace({4:22,5:33},inplace=True)
# print(a)
# a.replace(r'不神$','神了',inplace=True,reagex=True)
# print(a)

# # 2.转换数据类型 astype
# a = pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
# a = a.astype({'A':int,'B':float})      # 字典转换数据类型
# c = a['A'].astype(float)               # 选取A列,转换为浮点数
# print(c)

# # TODO: 数据排序
# df = pd.DataFrame({
#     'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
#     'col2': [2, 1, 9, 8, 7, 4],
#     'col3': [0, 1, 9, 4, 2, 3],
#     'col4': ['a', 'B', 'c', 'D', 'e', 'F']
# })
# # 按列升序排序 sort_values
# res1 = df.sort_values(by=['col1'],ascending=True)  # ascending=True表示升序
# print(res1)

# # 按索引标签升序排序 sort_index
# arrays = [np.array(['qux', 'qux', 'foo', 'foo']),     # 创建一个多级索引的DataFrame
#           np.array(['two', 'one', 'two', 'one'])]
# df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1]},index=arrays)  #两列（array）行索引
# print(df)

# # 按列索引升序排序 sort_index
# df = df.sort_index(axis=1,ascending=True)   # axis其实默认是0,表示按行索引排序
# print(df)

# # 按多级索引升序排序 sort_index
# df = df.sort_index(level=0,ascending=True)  # level=0表示按第一级索引升序排序(后面的也如此)
# print(df)

# 数据筛选 条件
# df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1]})
# print(df['A'] >= 2)        # 筛选出A列中大于等于2的行
# print(df[df['A'] >= 2])    # 把符合条件的行补全
# print(df[df >= 2])

# # 数据拼接 concat
# df1 = pd.DataFrame({'A': [1, 2, 3, 4],
#                     'B': [4, 3, 2, 1]},index = [1,2,3,4])
# df2 = pd.DataFrame({'A': [5, 6, 7, 8],
#                     'C': [6, 5, 4, 3]},index = [5,6,7,8])
# df3 = pd.concat([df1,df2],axis=0,join='outer')     # join='outer'表示外连接,保留所有索引标签(默认),并集
# df4 = pd.concat([df1,df2],axis=1,join='inner')     # axis=1表示按列拼接,在交集时要有公共行标签才有数据
# print(df3)
# print(df4)

# TODO: 分组与聚合
# df = pd.DataFrame({
#     '年龄':[18,18,18,20,20,20],
#     '姓名':['张三','李四','王五','赵六','钱七','孙八'],
#     '性别':['男','男','男','男','女','女']
# })
# print(df)
# grouped = df.groupby(['年龄'])
# print(list(grouped))

# # TODO: 常见统计计算
# max
# mean
# min
# std
# var
# count
# sum

# TODO: 数据读写
# # csv文件写入与读取   to_csv    read_csv
# df = pd.DataFrame({'姓名':['张三','李四','王五','赵六','钱七','孙八'],
#               '性别':['男','男','男','男','女','女'],
#               '年龄':[18,18,18,20,20,20]})
# df.to_csv('data.csv',index=False,encoding='utf-8-sig',sep='\t',mode='w')
# # with open('data.csv','r',encoding='utf-8-sig') as f:
# #     df1 = pd.read_csv(f,encoding='utf-8-sig',sep='\t')     # 读取csv文件
# #     print(df1)
# df1 = pd.read_csv('data.csv',encoding='utf-8-sig',sep='\t')
# print(df1)

# # excel文件写入与读取   to_excel    read_excel
# df = pd.DataFrame({'姓名':['张三','李四','王五','赵六','钱七','孙八'],
#                '性别':['男','男','男','男','女','女'],
#                '年龄':[18,18,18,20,20,20]})
# df.to_excel('data.xlsx',index=False,sheet_name='Sheet1',engine='openpyxl')

# df1 = pd.read_excel('data.xlsx',sheet_name='Sheet1')
# print(df1)