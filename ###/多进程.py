from multiprocessing import Process

""" 直接运行函数 """
def func(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=func, args=('bob',))
    p.start()
    p.join()  # 等待子进程结束后再继续往下运行，通常用于进程间的同步

""" 继承Process类 """
class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        """ 重写run方法，start后直接运行 """
        print('hello', self.name)

if __name__ == '__main__':
    p = MyProcess('bob')
    p.start()
    p.join()

""" 进程池 """
from multiprocessing import Pool
if __name__ == '__main__':
    pool = Pool(12)  # 最多同时运行12个进程,如果不填写，进程数=cpu核数
    for i in range(10):
        pool.apply_async(func, args=(i,))  # 异步执行，不等待子进程结束
    pool.close()
    pool.join()  # 等待子进程结束后再继续往下运行，通常用于进程间的同步