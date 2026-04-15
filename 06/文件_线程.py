# 队列以及栈
"""
    队列(排队) : 先进先出队列
    栈(手枪子弹上膛) : 后进先出队列
    queue.Queue()
        maxsize=0 : 队列容量,如果为0 无限内存

    Queue.get(item,timeout=None) 出列  数据空 如果timeout=None会一直等待入列一个元素
    Queue.get_nowait() 出列  数据空 直接报错

    Queue.put(item,timeout=None) 入列 数据满 如果timeout=None会一直等待出列一个元素
    Queue.put_nowait() 入列   数据满 直接报错
"""
# import queue

# q = queue.Queue(maxsize=2)  # 创建一个队列,容量为2,先进先出
# q.put(1)            # 入列1
# q.put(2)
# # q.put_nowait(3)   #  数据满 直接报错
# # q.put(3,timeout=None)       # 数据满 会一直等待出列一个元素
# print(q.get())                # 出列1
# print(q.get(timeout=None))    # 出列2,如果队列为空,会一直等待入列一个元素  
# print(q.qsize())              # 获取队列中元素的数量 

# z = queue.LifoQueue(maxsize=2)  # 创建一个栈,容量为3,后进先出
# z.put(1)        # 入列1
# z.put(2)
# print(z.get())  # 出列2，后进先出
# print(z.get())   


# TODO 线程的创建
# 1.使用Tread直接创建线程
# from threading import Thread
# import time
# def coding(name,age):
#     for i in range(3):
#         print(f"子进程is coding")
#         time.sleep(0.3)

# def music(cde):
#     for i in range(3):
#         print(f"子进程is music")
#         time.sleep(0.3)

# if __name__ == '__main__':
#     thread1 = Thread(target = coding,kwargs={"name":"shsw","age":18})
#     thread2 = Thread(target = music,args=("hello world",))
#     thread1.start()
#     thread2.start()

# # 2.使用继承Thread类的子类创建线程
# from threading import Thread
# import time
# class MyThread(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.task_name = name

#     def run(self):      # 重写run方法,子线程会执行run方法中的代码
#         print(f"{self.task_name}任务开始")
#         time.sleep(2)
#         print(f"{self.task_name}任务结束")

# if __name__ == '__main__':
#     p = MyThread("测试")
#     p.start()                     # 只有start才能启动一个新线程，run()方法不会
#     time.sleep(1)                 # 主线程等待准备结束
#     print("主线程在等待子线程1s后结束")
    
"""
    1个进程里面的两个线程     主线程和子线程结束顺序：默认情况下，主线程会等待所有子线程结束完之后才会结束
    主线程是默认创建的，无需显示创建    任何手动创建的线程都是子线程
"""
"""
    守护线程类似于守护进程,主线程退出后,守护线程也会直接销毁
"""
# from threading import Thread
# import time

# def work():
#     for i in range(10):
#         print("工作1...")
#         time.sleep(0.2)         # 子线程只能执行5次

# if __name__ == '__main__':
#     work_thread = Thread(target=work)
#     work_thread.daemon = True    # 设置守护线程,主线程退出后,子线程也会直接销毁,不会执行子线程中代码

#     work_thread.start()
#     time.sleep(1)                # 可以看到子线程调用5次后，主线程结束了，同时子线程也会直接销毁

#     print("主进程执行完毕,并强制结束子线程")

"""
    join方法 : 在线程可以阻塞主线程的执行，直接等待子线程全部完成之后才继续运行主线程后面的代码
"""

# TODO 文件读写

# 相对路径  从当前目录开始写    ./表示当前目录   ../表示上一级目录   例如 ./class_1.py
# 绝对路径  从根目录开始写      /表示根目录      ./表示当前目录     例如 C:/Users/Extraordinarily/Desktop/传/realzuoye/基础/集合函数/class1.py
# python中尽量使用正斜杠/,      因为正斜杠/容易被理解为转义字符,除非加r前缀表示原始字符串
"""
  open(file,mode,encoding=encoding)    打开文件
  file: 文件名
  mode: 打开模式
  r: 只读模式   r+ 可读可写     (两者文件不存在,会报错)
  w: 写入模式   w+ 可写可读     (两者文件不存在,会创建新文件,存在,会覆盖原文件)
  a: 追加模式   a+ 可追加可读   (两者文件不存在,会创建新文件,存在,会追加内容)
  b: 二进制模式                (读写二进制文件,例如图片,视频等)
"""

"""
    with语句打开文件,自动关闭文件,无需手动关闭 
    相当于
    finally:
        f.close()  # 必须手动关闭
"""
# 读取文件
# with open("C:/Users/Extraordinarily/Desktop/传/realzuoye/基础/集合函数/class_1.py","r") as f:
#     print(f.read())   

# with open(r"./test.txt","w")as f1:
#     f1.write(f"""shsw
#                 hello world
#                 hello world
#             """)
# with open(r"./test.txt","r",encoding="utf-8")as f2:
    # print(f2.read(2))     # 读取两个字符                              ("sh")
    # print(f2.readline())  # 从文件中读取单行数据 返回的是字符串类型      ("shsw\n")
    # print(f2.read())      # 读取所有字符                              ("shsw\nhello world\nhello world\n")
    # print(f2.readlines())   # 从文件中读取所有行  将每一行的数据存到列表中
    
    # while True:                 # 1，仅针对文本文件
    #     res =  f2.readline()    # 逐行读取
    #     if res == '':           # 读取到空行,说明文件读取完成
    #         break
    #     print(res,end="")       # end=""避免换行  

    # while True:                 # 2，通用方法（个人感觉最好用）
    #     res =  f2.read(1024)    # 读取1024个字符或字节
    #     if res == '':           
    #         break
    #     print(res)
"""
    encode()方法:将字符串转换为字节
    decode()方法:将字节转换为字符串
"""
# 写入文件
# with open(r"./test.txt","w")as f1:
#     f1.write(f"""shsw
#                 hello world
#                 hello world
#             """)
# with open(r"./test.txt","a")as f3:    # a表示追加模式
#     f3.write("hello world")
# with open(r"./test.txt","r")as f4:    
#     print(f4.read())

# with open(r"./test.txt","rb")as f5:    # rb表示二进制模式
#     # 二进制模式读取文件,返回的是字节类型
#     print(f5.read())
#     print(type(f5.read()))             # <class 'bytes'>  字节类型

#     # 字节转换为字符串
#     f5.seek(0)                         # 重置文件指针到文件开头
#     print(f5.read().decode('utf-8'))        # 字节转字符串(decode()方法)
#     print(type(f5.read().decode('utf-8')))  # <class 'str'>  字符串类型

# # 字符串转换为字节
# print("hello world".encode('utf-8'))        # 字符串转字节(encode()方法)
# print(type("hello world".encode('utf-8')))  # <class 'bytes'>  字节类型

# #关闭文件
# res =  open(r"./test.txt",'a')
# print(res)
# res.close()  # 关闭文件,释放资源

# 指针操作
"""
    seek(offset,where)方法:
        offset : 移动的偏移量，单位为字节，一中文字符=三字节
        where : 移动的位置（起点）
            0 : 文件开头
            1 : 当前位置
            2 : 文件末尾
    tell()方法:返回文件指针当前位置
"""
# with open("./test.txt","r+")as f:
    # f.seek(1,0)       # 走1字节   （0）表示文件开头
    # print(f.tell())   # 指针指向1字节
    # # f.write("world")    # 写入world,覆盖已有内容
    # # print(f.readlines())

    # f.seek(0,1)       # 走0字节   （1）表示当前位置
    # print(f.tell())   # 指针指向0字节

    # f.seek(0)         # 重置文件指针到文件开头
    # print(f.tell())   # 指针指向0字节 

# 获取文件属性
# import os
# import time

# print(os.path.getsize("./test.txt"))                # 获取文件大小,单位为字节

# mtime_time = os.path.getmtime("./test.txt")         # 获取文件最后修改时间,单位为秒
# local_time = time.localtime(mtime_time)             # 将秒转换为本地时间元组 
# print(time.strftime("%Y-%m-%d %H:%M:%S",local_time))        # 将本地时间元组转换为字符串

# 目录操作
"""
    创建目录 :
        os.mkdir(path)     创建单个目录  存在则报错
        os.makedirs(path)  创建多级目录  存在则报错
"""
# import os
# os.mkdir("./test1")
# os.makedirs("./test1/123")

"""
    检查路径是否为文件   os.path.isfile()  
    检查路径是否为目录   os.path.isdir()  
"""
# import os
# print(os.path.isfile("./test.txt"))  # True
# print(os.path.isdir("./test1"))      # False

"""
    获取文件的绝对路径  os.path.abspath()
    路径拼接：  拼接路径  
    os.path.join()
"""
# import os
# print(os.path.abspath("./test.txt"))
# print(os.path.join(r"C:\Users\Extraordinarily\Desktop\传\realzuoye\基础\集合函数","test.txt")) #加r表示原始字符串,避免转义字符的错误解释
