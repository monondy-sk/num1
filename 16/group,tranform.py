import pandas as pd
import numpy as np
data = {
    '部门': ['销售', '销售', '技术', '技术', '销售', '技术'],
    '员工': ['张三', '李四', '王五', '赵六', '钱七', '孙八'],
    '工资': [5000, 6000, 8000, 7500, 5500, 8200],
    '奖金': [1000, 1200, 1500, 1400, 1100, 1600]
}
df = pd.DataFrame(data)
print("原始数据:")
print(df)

# 聚合操作 vs 转换操作
grouped = df.groupby('部门')

# 1. 聚合操作 - 返回分组级别的统计
agg = grouped['工资'].mean()
print("\n聚合结果: 每个部门平均工资:")
print(agg)
df.loc[[1,2],'工资'] = np.nan   # 模拟缺失值
print(df)

# 可以看到以部门分组,工资为即分成每个部门的x1,x2,x3...的Series,这部分的Series就是进入transform函数的参数x,再fillna缺失值
df['工资'] = df.groupby('部门')['工资'].transform(lambda x : x.fillna(x.mean()))
print(df)
# 如果还有NaN（整个组都是NaN），用全局均值填充
if filled.isna().any():
    global_mean = df['工资'].mean()
    filled = filled.fillna(global_mean)


# 2. 转换操作 - 返回与原始数据相同形状
transform_result = grouped['工资'].transform('mean')
print("\n转换结果: 每个员工的部门平均工资:")
print(transform_result)

"""
    groupby即聚合,聚合完()就将该列转化为行索引了,而我们后面[]指的就是行索引聚合后产生的多个子Series,
    我们可以对这些子Series进行操作,可以直接.(Series常见方法（mean,max...）),这样每个子Series就会进行统计计算的操作了
    也可以使用transform函数,用x表示一个个进去的参数,在对x进行操作,方法很多了(fillna,mean),且不担心报错
    最后transform返回的是一个Series,与原始数据的形状相同,这样就可以直接修改原数组了
"""