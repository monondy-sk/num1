# # TODO  锁
# # 互斥锁的使用
# from threading import Lock,Thread
# import time
# import threading

# ticket_num = 10  # 定义100张票
# def buy_ticket(lock):
#     lock.acquire()       # 请求锁
#     global ticket_num
#     if ticket_num > 0 :
#         ticket_num -= 1
#         print(f'当前还剩{ticket_num}张票')
#         time.sleep(0.2)
#         print(threading.current_thread().name)  # 打印当前线程名称，在任务中只能这样打印线程名称
#     else:
#         print('票已售罄')
#     lock.release()       # 释放锁

# if __name__ == '__main__':
#     task_list = []       # 定义线程列表
#     lock = Lock()        # 创建互斥锁
#     for i in range(8):
#         t1 = Thread(target=buy_ticket,args=(lock,))
#         # time.sleep(1)          # 不打开就一次性创建完所有线程
#         # print(t1.name)         # 打印线程名称，主线程可以这么打印
#         t1.start()  # 启动子线程
#         task_list.append(t1)

#     for i in task_list:
#         # print(i.name)    # 打印线程名称
#         i.join()           # 相当于上保险，保证主线程在子线程执行完毕才能结束
#     print(task_list)       # 打印线程列表最终状态
#     print("主线程结束,剩余票数为：",ticket_num)

"""
    由于GIL(全局解释器锁)的存在,导致python不能实现并行执行字节码,只能实现并发执行字节码
    即只能实现一个线程在执行字节码,其他线程只能等待,直到当前线程的时间片用完
    这个顺序是不确定的,因为线程的执行顺序由操作系统决定
"""
"""
    互斥锁的使用可以解决线程安全问题
    同时互斥锁内维护了一个类似FIFO的队列,用于存储等待锁的线程
    因此,创建的线程抢锁时是由操作系统和互斥锁队列近似FIFO的规则共同决定的
    不一定是先创建的线程先抢到锁     
    顺序：  操作系统  —>  GIL  ->  线程  ->  互斥锁队列  ->  互斥锁
"""
"""
    因此,多线程真正能使用的就是IO密集的任务(GIL只是执行字节码只能单线程)
    如果是CPU密集的任务,则必须用多进程来实现(多进程会创建多个GIL)
"""

# # 死锁
# import time
# from threading import Thread,Lock,current_thread

# mutex1 = Lock()
# mutex2 = Lock()
# # 死锁现象（了解 平常不要出现死锁现象）
# def task():
#     mutex1.acquire()
#     print(f'{current_thread().name}抢到锁1')    # 1，线程A执行完，   5，线程B来了，成功获取锁1
#     mutex2.acquire()
#     print(f'{current_thread().name}抢到锁2')    # 2，线程A执行完，   6，线程B获取锁2时(持有锁1)，发现锁2被A占用喽
#     time.sleep(1)
#     mutex1.acquire()
#     print(f'{current_thread().name}抢到锁1')
#     mutex2.release()
#     mutex1.release()

#     mutex2.acquire()
#     print(f'{current_thread().name}抢到锁2')    # 3，线程A执行完，
#     time.sleep(1)                               # 4，等待1秒，换到线程B从头开始
#     mutex1.acquire()
#     print(f'{current_thread().name}抢到锁1')     # 7,线程A回来了(持有锁2)，发现锁1被B占用喽，最终和B形成死锁状态
#     mutex2.release()
#     mutex1.release()

# if __name__ == '__main__':
#     for i in range(8):
#         t = Thread(target=task)
#         t.start()


# # 计时器
# import time
# import threading

# def get_time():
#     current_time = time.time()
#     format_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(current_time))

# if __name__ == '__main__':
#     times = threading.Timer(5,get_time)
#     times.start()         # 启动计时器,由于是Thread的子类,所以相当于启动了一个子线程
#     times.cancel()        # 取消计时器
    
# # 事件
# import threading

# event = threading.Event()

# def waiter():
#     event.wait()        # 等待事件被设置
#     print("已通知开放")  # set事件发生后执行

# def setter():
#     # 执行某些操作TODO
#     event.set()  # 设置事件，通知所有等待的线程
