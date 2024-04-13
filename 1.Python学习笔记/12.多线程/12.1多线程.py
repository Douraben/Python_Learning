"""
线程是程序的一种轻量级执行单元，它可以在单台机器上的多CPU核心上同时运行多个程序，充分利用资源。

threading 是 Python 中的一个模块，它提供了低级别的线程支持。在 Python 3.3 及更高版本中，
线程被实现为 _thread 模块的一个替代。threading 模块提供了更高级别的线程管理功能，例如创建线程、
保护线程之间的共享资源、设置线程优先级等。
导入threading模块后，可以使用其提供的功能来创建、管理、同步和通信线程

使用 threading 模块的步骤如下：

导入 threading 模块。
创建一个继承自 threading.Thread 的自定义线程类。
在自定义线程类的 __init__ 方法中重写 threading.Thread 的 __init__ 方法，设置线程名称、目标函数等。
实现目标函数，该函数将在线程启动时执行。
使用 start() 方法启动线程。
使用 join() 方法等待线程完成。

Thread 类的主要方法包括：

__init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)：初始化线程对象。

self：指向线程对象的引用，通常在类的方法中使用。

group：线程组，用于将多个线程组合在一起。如果未指定或为None，则线程属于默认线程组。

target：线程要执行的函数或方法。如果未指定或为None，则线程在start()方法中启动时将执行run()方法。

name：线程的名称。如果未指定或为None，则线程将生成一个默认名称。

args：元组，用于传递给目标函数的参数。

kwargs：字典，用于传递给目标函数的关键字参数。



start(self)：启动线程。
run(self)：定义线程要执行的任务。
join(self, timeout=None)：等待线程结束。
getName(self)：获取线程的名称。
is_alive(self)：检查线程是否仍在运行。
setName(self, name)：设置线程的名称。
setDaemon(self, daemonic)：设置线程为守护线程（daemon thread）。

"""
import threading


# 定义一个名为name的函数
def name(name_i):
    n = 0
    # 无限循环
    while n <= 100:
        n += 1
        # 打印你好 世界
        print(name_i)


# 定义一个名为age的函数
def age(age_i):
    a = 0
    # 无限循环
    while a <= 100:
        a += 1
        print(age_i)


# 如果当前运行的文件是主文件
if __name__ == "__main__":
    # 定义一个名为name_info的线程
   # 定义一个名为name_info的线程
    name_info = threading.Thread(target=name, args=("你好世界！",))  # 元组方式传参
    # 定义一个名为age_info的线程
    age_info = threading.Thread(target=age, kwargs={"age_i": "浩瀚宇宙"})   # 字典方式传参

    # 启动name_info线程
    name_info.start()

    # 启动age_info线程
    age_info.start()
