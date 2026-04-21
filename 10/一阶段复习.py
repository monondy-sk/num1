# 考试前最后一舞

# TODO:基础概念
"""
    标识符:  数字,字母,下划线,不能以数字开头
    注释:    #开头,直到换行符 ,  '''开头,直到'''结束
    进制:    10进制,2进制,8进制,16进制
    进制转换
"""
# TODO:运算符
"""
    算数运算符: +,-,*,/,%,//,**
    赋值运算符: =,+=,-=,*=,/=,%=,//=,%=,<<=,>>=,&=,|=,^=
    关系运算符: >,>=,<,<=,==,!=
    逻辑运算符: and,or,not
    成员运算符: in,not in
    位运算符: &,&&,|,||,^,^,<<,>>,~
"""
# TODO:输入输出
"""
    输入: input()
    输出: print() 常用f-string输出格式
"""
# TODO:条件语句
"""
    if elif else
"""
# TODO:循环语句
"""
    for 常与range()函数结合使用,生成一个数组
    while 循环,直到条件为False,才会退出循环
"""
# TODO:数字型数据
"""
    整数: int
    浮点数: float
    字符串: str
    布尔值: bool  属于整数的子类,只有0和1两种取值
    空值: None
"""
# TODO:字符串
"""
    字符串创建: s = "hello"
    字符串访问: 下标访问
    字符串增加: 不可变,只能拼接 s1+s2
    字符串删除: 不可变,不能删除字符串中的字符
    字符串修改: 不可变,不能修改字符串中的字符
    字符串的查找:  'l' in s       返回bool
                  s.find('l')    返回字符l的下标,如果不存在则返回-1,更安全
                  s.index('l')   返回字符l的下标,如果不存在则报错
                  s.count('l')   返回字符l出现的次数
    字符串的常用方法: 置换  s.replace('old','new')  替换所有old为new
                    去空格  s.strip()        去掉字符串首尾的空格
                    切片  s[start:end:step]  start为开始下标,end为结束下标,step为步长,注意包左不包右
                    分割  s.split('l')       l为分割符,默认为空格
                    合并  s.join(['a','b','c'])  用a,b,c连接字符串s
"""
# s = "hello"
# print(s.find('l'))
# print(s.index('o'))                
# TODO:列表
"""
    列表创建: l = [1,2,3,4,5]
    列表访问: 下标访问 l[0]
    列表增加: l.append(6)  在列表末尾增加元素6      insert(1,6)  在下标1的位置增加元素6     l1+l2
    列表删除: del l[0]  删除列表中的第一个元素       remove(6)  删除列表中第一个出现的6      pop(0)  删除下标为0的元素
    列表修改: l[0] = 100  修改列表中的第一个元素为100
    列表查找: 6 in l  返回bool
             l.index(6)  返回元素6的下标,如果不存在则报错
             
    列表常用方法:     len(l)  返回列表的长度
                    sort()  对列表进行排序
                    reverse()  对列表进行反转
                    max(l)  返回列表中的最大值
"""
# l = [1,2,3,4,5]
# print(l[0])
# l.pop(0)
# print(l)
#TODO:元组
"""
    元组的创建: t = (1,2,3,4,5)
    元组的访问: 下标访问 t[0]
    元组的增加,删除,修改: 不可变,不能增加,删除,修改元组中的元素      t1+t2
    元组的查询: 6 in t  返回bool 
              t.index(4)  返回元素4的下标,如果不存在则报错
              t.count(4)  返回元素4出现的次数
"""
# t1 = (1,2,3,4,5)
# t2 = (6,7,8,9,10)
# print(t[0])
# print(t.index(4))
# print(t+t2)
# TODO:集合
"""
    集合的创建: s = {1,2,3,4,5}
    集合的访问: 不能通过下标访问集合中的元素,只能通过遍历集合来访问
    集合的增加: s.add(6)     在集合s中增加元素6        s.update([7,8,9])  向集合s中增加多个元素
    集合的删除: s.remove(6)  从集合s中删除元素6,报错    s.pop()  任意删除一个元素并返回,大概率是第一个元素
    集合的查询: 6 in s       返回bool
    集合的并集,交集,差集  s|s2,    s&s2,    s-s2          
"""
# s = {1,2,3,4,5}
# # print(s[0])    非序列,下标统统消失,只能操控元素  
# s.update([6,7,8,9,5,4,3,2,1])  # 去重了部分
# print( 1 in s)
# s2 = {222,111}
# print(s2&s)  
# print(s2-s)
# TODO:字典
"""
    字典的创建: d={'a':1,'b':2,'c':3}
    字典的访问: d['a']        d.get('a')
    字典的增加,修改: d['d']=4      d['b']=100     
    字典的删除: del d['a']    d.pop('a')
    字典的查询: 6 in d       返回bool
    字典的常用方法: len(d)  返回字典的长度
                    keys()  返回字典的所有键       (['a', 'b', 'c'])
                    values()  返回字典的所有值     ([1, 2, 3])
                    items()  返回字典的所有键值对
"""
d={'a':1,'b':2,'c':3}
# print(d['a'])
# # l=[1,2,3]
# # d[l]=4        #字典的键必须是不可变类型,字符串,整数,元组
# print(d.pop('a'))
# print(d.get('a'))

#TODO:函数
"""
    函数的定义: def 函数名(参数1,参数2,参数3):
        函数体
        return 返回值
    传参方式: 位置参数,关键字参数(参数名=参数值),
             位置不定长参数(*args)只能放在最后面,不然最后的参数就只能用关键词传参,    
             关键字不定长参数(**kwargs)只能放在最后面             结果参下例
    局部变量: 函数体定义的变量,global声明后可以在函数体外部使用
    全局变量: 函数体外部定义的变量,哪都可以使用 
    lambda:  匿名函数,  lambda  参数表达式 : 返回值     lambda a,b : a+b
"""
# def add(*num,b):
#     print(num)
#     print(b)
# add(1,b=100)
# def sub(**num,b):
#     print(num)
#     print(b)
# sub(a=1,b=100)

# TODO:类和对象
"""
    类的定义: class 类名:
        类体
    属性：实例属性,类属性
    方法：实例方法,类方法,静态方法
    构造方法：初始化实例对象     析构方法：释放实例对象占用的内存
    面向对象编程：封装: 将属性和方法封装在类中,只能通过类的实例来访问,不能直接访问类的属性和方法
                 继承：子类可以继承父类的属性和方法,super().__init__()可以调用父类的构造方法
                 多态：一个对象可以有多种表现,多态性 
"""
# class Animal:
#     color = 'white'
#     def __init__(self,name):
#         self.name = name
# class Cat(Animal):
#     __category = 'cat'              # 私有属性,只能在类的内部访问
#     def __init__(self,name,age):
#         super().__init__(name)      # 调用父类的构造方法,初始化实例属性name
#         self.age = age
#         self.color = Animal.color   # 子类可以继承父类的属性,方法
#         self.category = Cat.__category
# c1 = Cat('小白',1)                   # 无需传递color参数,因为子类可以继承父类的属性
# print(c1.name)
# print(c1.age)
# print(c1.color)

# TODO:文件操作
"""
    文件操作: open(filepath,mode,encoding='utf-8')函数   中文文件操作必须指定编码,否则会报错,默认是gbk
    filepath: 文件路径,可以是绝对路径,也可以是相对路径
    mode: 文件打开模式,默认是r,只读模式
    r:只读,    w,只写     a,追加写     b:二进制模式,只能用于读写    r+,w+:读写模式
    文件的读:  f.read()  读取文件所有内容 ,  f.readline() 读取文件的一行内容
    文件的写:  f.write()
    文件的关闭:  f.close()
"""
# with open('./test.txt','r',encoding='utf-8') as f:       #with语句可以自动关闭文件
#     content = f.read() 
#     print(content)
# 文件属性及目录操作
"""
    os.path.getsize(filepath)  返回文件的大小,单位是字节
    os.getmtime(filepath)  返回文件的修改时间,单位是秒

    os.mkdir(filepath)  创建目录
    os.listdir(filepath)  返回目录下的所有文件和子目录
    os.path.join(filepath,subpath)  拼接路径
    os.path.isfile(filepath)  判断是否是文件
    os.path.isdir(filepath)  判断是否是目录
    os.path.abspath(filepath)  返回文件的绝对路径
    os.path.exists(filepath)  判断文件是否存在,返回bool
"""
# import os
# print(os.path.isfile('./test.txt'))
# print(os.path.exists('./test.txt'))
# TODO:多进程
"""
    进程是资源分配的最小单位
    进程的创建: import multiprocessing
    进程的启动: p.start()
    进程的等待: p.join()
    进程的终止: p.terminate()
    进程的通信：管道,队列,信号量,事件,  一般用队列
"""
# import multiprocessing
# def add(a,b):
#     print(a+b)
# if __name__ == '__main__':
#     p = multiprocessing.Process(target=add,args=(1,2))
#     p.start()       #启动子进程
#     p.join()        #等待子进程结束
# TODO:多线程
"""
    线程是cpu调度的最小单位
    线程的创建 import threading
    获取当前线程: threading.current_thread()
    线程启动:t.start()
    线程等待:t.join()
    线程终止:t.terminate()
    线程是共内存的,可以共享进程的资源
"""
# import threading 
# def add(a,b):
#     print(threading.current_thread())  # 打印当前线程对象
#     print(a+b)
#     lock.release()
    
# if __name__ == '__main__':
#     lock = threading.Lock()      #互斥锁,只能有一个线程获取锁,其他线程必须等待锁被释放
#     for i in range(5):
#         t = threading.Thread(target=add,args=(1,2))
#         lock.acquire()
#         t.start()
#     for i in range(5):
#         t.join()

# TODO:进程池以及线程池
"""
    进程池: multiprocessing.Pool(processes=5)
    线程池: threading.ThreadPool(max_workers=5)
"""