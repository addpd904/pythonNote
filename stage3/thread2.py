# consumer model
import threading
import time
# Multithreaded execution in parallel.(多线程并行执行).process
# 一、generate a thread via DIY a class that extend threading,overload run

def sing(msg):
    while True:
        print(f'{msg} singing')
        # we can use sleep to let the cpu release
        time.sleep(2)
def dance(msg):
    while True:
        print(f'{msg} dancing')
        time.sleep(3)
class MyThread(threading.Thread):
    def __init__(self,func,name,args):
        super().__init__(target=func,name=name,args=args)
    def run(self) -> None:
        # _target:the target func;_args:the argument that be passed
        self._target(*self._args)

if __name__ == '__main__':
    print('main thread start')
    t1=MyThread(sing,'thread-1',('zs',))
    t2=MyThread(dance,'thread2',('ls',))
    # when you call start ,the run will be call
    t1.start()
    t2.start()
    t1.join()
    t2.join()