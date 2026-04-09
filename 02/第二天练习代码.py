# a = float(input("请输入系数 a (a ≠ 0): "))
# b = float(input("请输入系数 b: "))
# c = float(input("请输入系数 c: "))

# if a == 0:
#     print("错误：a 不能为 0")
# else:
#     delta = b**2 - 4*a*c
    
#     print(f"\n方程为: {a}x² + {b}x + {c} = 0")
#     print(f"判别式 Δ = {delta}")
    
#     # 根据判别式的值计算根
#     if delta > 0:
#         # 两个不相等的实数根
#         x1 = (-b + delta**0.5) / (2*a)
#         x2 = (-b - delta**0.5) / (2*a)
#         print(f"方程有两个不相等的实数根:")
#         print(f"x₁ = {x1:.6f}")
#         print(f"x₂ = {x2:.6f}")
#     elif delta == 0:
#         # 两个相等的实数根
#         x = -b / (2*a)
#         print(f"方程有两个相等的实数根:")
#         print(f"x₁ = x₂ = {x:.6f}")
#     else:
#         # 没有实数根
#         print("方程没有实数根")


# s=input("字符串:").lower()
# w=input("目标:").lower()
# k=0
# for i in s:
# 	if i==w:
# 		k+=1
# print(k)


# s=input("字符串:")
# i=0
# t=True
# for i in range(len(s)//2):
#     if s[i]!=s[(len(s)-i-1)] :
#         t=False
#         break
#     else :
#         t=True

# char=""
# for i in s:
#     if i.isalpha():
#         char+=i.lower()
# if t == True:
# 	print("是回文字符串")
# else :
#   	print("不是")

# lst=[3,1,2,4,5]
# lst=[i for i in lst if i%2==0]
# print(lst)


# str="zmjjkk"
# print(str.find("x"))
# print(str.index("x"))

# numbers=[15,8,23,4,42,16]
# max=0
# min=numbers[0]
# for i in numbers:
# 	if i>max:
# 		max=i
# 	if i<min:    
# 		min=i
# print(min)
# print(max)


# items =[('apple',2.5),('banana',1.8),('orange',3.0),('grape',2.8)]
# items.sort(key=lambda a : a[1])	
# print(items)


# data=[1,2,3,4,5,6,7,8,9]
# group_size = 3
# data_s=[]
# length = len(data)//group_size
# for i in range(length):
#     data_p=data[i*group_size:(i+1)*group_size]
#     data_s += [tuple(data_p)]
# print(data_s)


# s="sadad"
# # s={1,2,3,4,5,6,7,8,9}
# print(len(s))

# list1=[1,2,3,4,5,5]
# list2=[4,5,6,7,8,5]
# list3= list(set(list1) & set(list2))
# print(list3)

# group_a =['apple','banana','orange','grape']
# group_b=['banana','grape','watermelon']
# group_c =['orange','peach']

# group_d = set(group_a ) - set(group_b) - set(group_c)
# print(group_d)

# group_e = (set(group_a) & set(group_b)) - set(group_c)
# print(group_e)

# group_f = set(group_a) - set(group_b) - set(group_c)
# group_g = set(group_b) - set(group_a) - set(group_c)
# group_h = set(group_c) - set(group_a) - set(group_b)
# print(group_f,group_g,group_h)


# s = "Hello world! Hello Python."
# s=s.strip()
# s=s.lower()
# # s=s.replace("!","")
# # s=s.replace(".","")
# for i in s:
#     if not i.isalpha():
#         s=s.replace(i," ")

# words = s.split()
# print(words)
# freq_dict = {}
# for word in words:
#      if word in freq_dict:
#             freq_dict[word] += 1
#      else:
#             freq_dict[word] = 1
				
# print(freq_dict)


# original_dict={'a':1,'b':2,'c':1,'e':2}
# new_dict={}
# for key,value in original_dict.items():
#     if value in new_dict:
#         new_dict[value].append(key)
#     else:
#         new_dict[value] = [key]
# print(new_dict)