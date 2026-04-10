# TODO
#列表的增删改查语法
lst=[1,2,3,4,5]

# 增加
# lst.append(6)    # 在列表末尾添加元素
# lst.insert(2,4)  # 在索引为2的位置插入元素4
# print(lst)

# 删除
# lst.remove(3)  # 删除第一个出现的3
# print(lst)
# del lst[2]     # 删除索引为2的元素
# print(lst)
# lst.pop()      # 删除最后一个元素
# lst.pop(2)     # 删除索引为2的元素
# print(lst)

#修改
# lst[2]=100       # 修改索引为2的元素为100,有则修改,无则添加
# print(lst)

# 查询
# print(lst[2])      # 输出索引为2的元素
# print(lst.index(4)) # 输出元素4的索引
# print(lst.count(4)) # 输出元素4的出现次数
# print(lst[2:4])    # 输出索引为2到索引为4的元素(不包含索引为4)
# print(lst[2:4:1])  # 输出索引为2到索引为4的元素(不包含索引为4),每1个元素取一个
# print(lst[-1:-4:-1]) # 输出索引为-1到索引为-4的元素(不包含索引为-4),每1个元素取一个,从后往前取

#排序与反转
# lst.sort(key=lambda a : a)
# print(lst)
# lst.reverse()
# print(lst)



#元组的增删改查语法
tup = (1, 2, 3, 4, 5)
tup2 = (6, 7, 8, 9, 10)
#增删改皆不行
#查询
# print(tup)
# print(tup[2])
# print(tup[2:4])      #切片
# print(tup[2:4:1])
# print(tup[-1:-4:-1])

# print(tup.count(3))  # 输出元素3的出现次数
# print(tup.index(3))  # 输出元素3的索引

# 其它操作
# print(tup + tup2)    # 拼接元组
# print(tup * 2)       # 重复元组
# print(2 in tup)      # 检查元素2是否在元组tup中
# print(len(tup))      # 输出元组tup的长度
# print(max(tup))      # 输出元组tup的最大元素
# print(min(tup))      # 输出元组tup的最小元素
# print(sum(tup))      # 输出元组tup的元素总和

# 元组的排序
# print(sorted(tup,reverse=True))  # 可行，因为生成的是一个新的元组，不会改变原元组
# print(tup2.reverse())            # 不可行，因为reverse()方法会改变原元组，而不是返回一个新的元组  print(tup2[::-1])  # 可转元组tup2



# 集合的增删改查语法
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}

# 增加
# set1.add(6)
# print(set1)

# 删除
# set1.remove(3)     # 删除第一个出现的3
# print(set1)
# set1.discard(3)   # 不报错,无元素3时,不报错
# print(set1)
# set2.pop()        # 随机删除一个元素
# print(set2)

# 修改
# set1.update("单个字符")  # 将字符串"单个字符"转换为集合,并将其元素添加到set1中,会把字符串分割为单个字符加入set1中
# print(set1)
# set2.update(set1)   # 合并集合set2,将set1中的元素添加到set2中
# print(set2)

# 查询
# print(3 in set1)

# 集合的交集、并集、差集
# print(set1 & set2)  # 交集,或用intersection()方法表示
# print(set1 | set2)  # 并集,或用union()方法表示
# print(set1 - set2)  # 差集,或用difference()方法表示




#字典的增删改查语法
# dict1 = {'a':1,'b':2,'c':3}
# dict2 = {'d':4,'e':5,'f':6}
# # 增加
# dict1['d']=4        #有则修改,无则添加
# print(dict1)

# # 删除
# del dict1['b']      # 删除键为b的元素
# dict1.pop('c')      # 删除键为c的元素
# print(dict1)

# # 修改
# dict1['a']=100      # 修改键为a的值为100,有则修改,无则添加
# print(dict1)

# # 查询
# print(dict1['a'])               # 输出键为a的值
# print(dict1.get('a',11))        # 输出键为a的值,无则返回11(默认值)
# print('a' in dict1)             # 检查键a是否在字典dict1中
# print(100 in dict1.values())    # 检查值100是否在字典dict1的值中
# print('a' in dict1.keys())      # 检查键a是否在字典dict1的键中
# print('a' in dict1.items())     # 检查键值对(a,1)是否在字典dict1中


# TODO
# x = [1, 2,3]
# x[:2]= [4]
# # [[4],3]
# print(x)

# (1,2)+(1,2,6)
# print((1,2)+(1,2,6))

# print((2,) + (3,))
# print((2) + (3))

# x=1,3
# print(x,type(x))

# x,y='a','b'
# print(x,type(x))

# x,y=divmod(-10,3)
# print(x,y)
# print(pow(x,y))


# numbers=input("请输入6个不一样的数，用逗号隔开：")
# numbers=[int(i) for i in numbers.split(",")]
# print(max(numbers))


# A=input("6个：")
# A=[i for i in A if  i!=',']
# print(max(A))

    # print(dict())
    # print(set())

# x = {'a':'b', 'c':'d'}
# print('a' in x)
# print('b' in x)
# print('b'  in x.values())

# x = {1:2, 2:3, 3:4}
# print(x.get(3, 4))
# print(sum(x.values()))

# d ={'大海':'蓝色', '天空':'灰色', '大地':'黑色'}
# print(d['大地'], d.get('大地', '黄色'))

# ds={"av":2,"vr":4,"path":6}
# print(ds.popitem( ),len(ds))

# d={'name':'lisi','age':10,'sex':'男'}
# d['height']=1.8
# print(d)

# d1 = {'Name': 'lisi', 'Age': 17}
# d2 = {'Age': 8 }
# d1.update(d2)
# print(d1)
# print(d2)
