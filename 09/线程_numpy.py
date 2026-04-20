# 1. 使用 threading 模块实现一个多线程下载器模拟程序：
# 要求：
# （1）创建 5 个线程模拟下载任务
# （2）每个线程下载一个文件，打印"正在下载文件 X..."（X 为线程编号）
# （3）每个下载任务耗时 2 秒（使用 time.sleep 模拟）
# （4）所有下载完成后，打印"所有文件下载完成！"
# （5）使用 join() 确保主线程等待所有下载线程完成
# import threading
# import time
# class Downloader:
#     def __init__(self, file_name):
#         self.file_name = file_name
#     def download(self):
#         print(f"正在下载文件 {self.file_name}...")
#         time.sleep(2)
#         print(f"文件 {self.file_name} 下载完成！")
# if __name__ == "__main__":
#     for i in range(5):
#         downloader = Downloader(f"文件{i}")
#         thread = threading.Thread(target=downloader.download)
#         thread.start()
#     for i in range(5):
#         thread.join()
#     print("所有文件下载完成！")

# 2. 使用 ThreadPoolExecutor 实现一个线程池应用：
# 要求：
# （1）创建一个包含 3 个线程的线程池
# （2）提交 10 个任务到线程池，每个任务打印"任务 X 正在执行"（X 为任务编号）
# （3）每个任务耗时 1 秒（使用 time.sleep 模拟）
# （4）使用 submit() 方法提交任务
# （5）使用 shutdown() 方法等待所有任务完成并关闭线程池
# （6）观察线程池如何复用线程执行任务

# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor


# def task(i):
#     print(f"任务{i}正在执行")
#     time.sleep(1)
# if __name__ == "__main__":
#     executor = ThreadPoolExecutor(max_workers=3)
    
#     for i in range(10):
#         executor.submit(task, i)
    
#     executor.shutdown()
#     print("所有任务完成！")


# TODO：向量,矩阵,张量
"""
    向量,有方向的量,(1,2)表示一个2维向量
      向量相加,相乘(点积比较重要)

    矩阵,长方阵列数据集合, [ 1  2 ]
                         [ 3  4 ]表示一个2*2的矩阵
    矩阵加法(对应元素相加),矩阵x矩阵(第一个的列数必须等于第二个的行数,每一行元素对应每一列元素相乘再相加)

    张量,多维数组,如标量为0维张量,向量为1维张量,矩阵为2维张量

"""

#numpy数组
# import numpy as np
# a = np.array((1,2))     # 进去之后整体就是numpy数组类型，单个元素有许多基类,如int32,float32等,根据需要选择
# b = np.array((3,4))     
# print(a)                # [1 2]
# print(type(a))          # <class 'numpy.ndarray'>这是numpy数组类型,可以进行向量加法,矩阵加法等操作

# a=a+b                   # 相加与列表(追加)不同, 此处是对应元素相加 [4(1+3) 6(2+4)]

# print(a)                # [4 6]
# print(type(a[0]))       # <class 'numpy.int32'>