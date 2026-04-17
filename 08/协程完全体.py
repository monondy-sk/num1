#  协程
"""
    async 相当于把一个普通函数变成一个可以暂停执行的异步函数,返回一个协程对象
    await 用于暂停执行,通常搭配async.time()函数使用,可以使当前协程暂停,转而执行其他协程
"""
# import asyncio
# async def task():
#     print("任务1开始")
#     await asyncio.sleep(1)
#     print("任务1结束")
#
# async def task2():
#     print("任务2开始")
#     await asyncio.sleep(2)
#     print("任务2结束")
#
# async def main():
#     await task()
#     await task2()
#     print("所有任务结束")
#
# asyncio.run(main())

"""
    Task是事件循环调度的基本单位，用于封装协程。创建Task对象会将协程加入事件循环的调度队列
    语法:  asyncio.create_task(task())
"""
# #Task建立事件循环
# import asyncio
# async def task():
#     print("任务1开始")                # 2, 进来了
#     await asyncio.sleep(1)          # 3, 等待是不可能的,直接在循环列表找下家协程
#     print("任务1结束")                # 6, 到这就完结t1的使命了,
#
# async def task2():
#     print("任务2开始")                # 4, 到这了
#     await asyncio.sleep(2)          # 5, 我也不等,又回task了,同时保存进度哦，下次调用t2从这开始
#     print("任务2结束")                # 7, 最后一步
# async def main():
#     t1= asyncio.create_task(task())  #加入事件循环队列
#     t2= asyncio.create_task(task2())
#
#     result1 = await t1               # 1, await当前协程,直接就开始t1(task)
#     result2 = await t2               # 7, 继承5的进度,开始
#
#     print(result1)
#     print(result2)
#
# asyncio.run(main())


"""
    协程之间可以通过队列进行通信,实现生产者-消费者模式
"""
# # 非常好的消费者生产者例子
# import asyncio
# import random
# import time
#
# async def producer(queue, name, count):
#     """生产者协程：向队列中添加数据"""
#     for i in range(count):
#         item = f"产品-{name}-{i}"
#         await asyncio.sleep(random.uniform(0.1, 0.5))  # 这里就进入循环队列
#         await queue.put(item)  # 将产品放入队列
#         print(f"[{time.strftime('%X')}] 生产者 {name} 生产了: {item}")
#     # 放入结束标志
#     await queue.put(None)
#     print(f"生产者 {name} 完成")
#
# async def consumer(queue, name):
#     """消费者协程：从队列中取出数据"""
#     while True:
#         item = await queue.get()  # 这里获取很重要，如果产品队列为空，那消费者就在等待生产，让出协程，直到有产品进来(就像吃席等上菜一样)，就唤醒此处的协程。
#         if item is None:
#             # 结束标志，重新放回以便其他消费者也能结束
#             await queue.put(None)
#             break
#         print(f"[{time.strftime('%X')}] 消费者 {name} 消费了: {item}")
#         await asyncio.sleep(random.uniform(0.2, 0.8))  # 模拟消费时间
#         queue.task_done()  # 标记任务完成
#     print(f"消费者 {name} 完成")
#
# async def queue_example():
#     """
#     使用asyncio.Queue进行协程间通信
#     """
#     # 创建队列，最大容量为5
#     queue = asyncio.Queue(maxsize=5)
#
#     # 创建生产者和消费者
#     producers = [
#         producer(queue, "A", 3),
#         producer(queue, "B", 2)
#     ]
#
#     consumers = [
#         consumer(queue, "X"),
#         consumer(queue, "Y")
#     ]
#
#     print("开始生产-消费...")
#     start_time = time.time()
#
#     # 并发运行所有任务
#     producer_tasks = [asyncio.create_task(p) for p in producers]
#     consumer_tasks = [asyncio.create_task(c) for c in consumers]
#
#     # 等待所有生产者完成
#     await asyncio.gather(*producer_tasks)
#
#     # 等待队列中的所有项目被处理
#     await queue.join()
#
#     # 取消消费者任务
#     for task in consumer_tasks:
#         task.cancel()
#
#     # 等待消费者任务被取消
#     await asyncio.gather(*consumer_tasks, return_exceptions=True)
#
#     elapsed_time = time.time() - start_time
#     print(f"生产-消费完成，总耗时: {elapsed_time:.2f}秒")
#
# #运行
# asyncio.run(queue_example())