# 多继承用super
# class fruit:
#     def __init__(self,name="水果",color="未知"):  # 只能有一个初始化函数,不能有两个初始化函数,否则会报错
#         self.name=name
#         self.color=color
#     # def __init__(self,*args):     #不知长短,可以是任意多个参数，字典格式用**kwargs
#     #    self.name,self.color =args
# class banana(fruit):
#     def __init__(self,a,b):
#         super().__init__(a,b)    #可见fruit必须要两个初始化函数，此处也必须有两个实参，但可默认值
# b=banana("香蕉","黄色")
# print(b.__dict__)

# 继承的多态 相当于子类重写父类方法A
# class A:
#     def A(self):
#         print("父类方法A")
# class B(A):
#     def A(self):
#         print("子类重写了父类方法A")
# b=B()
# b.A()

# 鸭子方法实现多态，不关注是哪个类，拿来用就行
# def query(any_instance):
#     any_instance.speak()
# class dog:
#     def speak(self):
#         print("汪汪汪")
# class cat:
#     def speak(self):
#         print("喵喵喵")
# # 调用query方法
# query(dog())  #狗实例传入即可调用方法

# query(cat())  #猫实例传入即可调用方法

# TODO 模块与包

# 模块就是一个.py文件，模块中可以有多个类，变量，方法

# 包就是一个包含多个模块和一个__init__文件(包含版本号，模块列表，初始化代码)的目录

# 导入模块的方式：
# import 模块名  
# from 模块名 import 类名,变量名,方法名       例如：from math import pi
# from 模块名 import as 别名  

# python有多种模块类型：
# 模块类型: 自定义模块,内置模块,第三方模块
# 自定义模块即自己写的模块,例如class_1.py，需要在当前目录下运行                 导入方式:import 模块名
# 内置模块即python自带的模块,例如math,random等，不需要import                  导入方式:import 模块名
# 第三方模块即从第三方网站下载的模块,例如requests ,需要先安装                   导入方式:import 模块名

# import fun
# import os
# import requests

# TODO 进程的创建
# import os
# from multiprocessing import Process
# import time

# def coding():
#     print(f"此进程为{os.getpid()}")
#     print(f"此进程的父进程为{os.getppid()}")
#     for i in range(3):
#         print(f"子进程is coding")
#         time.sleep(0.3)

# def music():
#     print(f"此进程为{os.getpid()}")
#     print(f"此进程的父进程为{os.getppid()}")
#     for i in range(3):
#         print(f"子进程is music")
#         time.sleep(0.3)

# if __name__ == '__main__':
#     process1=Process(target=coding)
#     process2=Process(target=music)

#     process1.start()    # 启动子进程1
#     process2.start()    # 启动子进程2,结果打印        子进程is music
#                         # 可以看到是交替执行          子进程is coding
#                         #                           子进程is music

# 默认情况下主进程会等待所有子进程结束后再结束
# from multiprocessing import Process
# import time

# def work():
#     for i in range(10):
#         print(f"主进程is work")
#         time.sleep(0.3)

# if __name__ == '__main__':         # 这是主线程
#     process1=Process(target=work)
    
    # 由于主进程会等待所有子进程结束后再结束,所以子进程1执行结束后,主线程才会结束
    # 因此我们有两个方法使子进程在主进程之前结束

    ## 1，使用守护进程          # 绑定主进程
    # process1.daemon=True          # 设置为守护进程,主进程退出后子进程直接销毁
    # process1.start()              # 启动子进程1
    # time.sleep(1)                 # 主进程等待1秒,然后主线程就准备结束了，子进程1也会直接销毁
    # print("主线进程结束,子进程1也会直接销毁")
    
    ## 2，使用terminate()方法   # 手动打断子线程
    # process1.start()              # 启动子进程1
    # time.sleep(1)                 # 主进程等待1秒,然后主线程就准备结束了
    # process1.terminate()          # 在主线程结束前销毁所有子进程
    # print("子进程1被终止")
    # print("主线进程结束")

    # # 3，使用join()方法       # 此方法即在子线程未完成时阻塞主线程的结束，直到子线程完成
    # process1.start()              # 启动子进程1
    # time.sleep(1)                 # 主进程等待1秒,然后主线程就准备结束了
    # process1.join()               # join()表示主线程在等待子进程1结束
    # # 如此便可看到子线程确实完整执行了10次
    # print("主线进程结束") 

# 僵尸进程   # 子进程已经死亡，但还有残留资源未被回收
# 孤儿进程   # 父进程意外死亡，子进程未被回收
