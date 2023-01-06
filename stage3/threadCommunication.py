import threading
import time
from threading import  Lock
from queue import Queue
from multiprocessing import Process
# 一、the global variable can be share between threads
''''
num=0
def task1():
    global num
    num += 10
    print('task1 num', num)

def task2():
    global num
    num += 30
    print('task1 num', num)
if __name__ == '__main__':
    print('main thread start')
    t1=threading.Thread(target=task1)
    t2=threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('main thread',num)
'''

# 二、problem in thread communication
'''
num=0
def task1():
    global num
    for i in range(1000000):
        num+=1
    print(f'task1 {num}\n')
def task2():
    global num
    for i in range(1000000):
        num+=1
    print(f'task2 {num}\n')
if __name__ == '__main__':
    t1=threading.Thread(target=task1)
    t2=threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('main ',num)
'''

# 三、lock,thread synchronization
'''
num=0
lock=Lock()
def task1():
    global num
    # acquire:lock
    for i in range(1000000):
        lock.acquire()
        num+=1
        lock.release()
    # unlock
    print(f'task1 {num}\n')
def task2():
    global num
    for i in range(1000000):
        lock.acquire()
        num += 1
        lock.release()
    print(f'task2 {num}\n')
if __name__ == '__main__':
    t1=threading.Thread(target=task1)
    t2=threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('main ',num)
'''

# 四、thread synchronization and synergy ;application

'''
lock1=Lock()
lock2=Lock()
lock3=Lock()
lock2.acquire()
lock3.acquire()

class Task1(threading.Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('...task1...')
                time.sleep(1)
                lock2.release()

class Task2(threading.Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('...task2...')
                time.sleep(1)
                lock3.release()

class Task3(threading.Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('...task3...')
                time.sleep(1)
                lock1.release()
if __name__ == '__main__':
    t1=Task1()
    t2=Task2()
    t3=Task3()
    t1.start()
    t2.start()
    t3.start()
'''

# 五、Producer consumer model

class Producter(threading.Thread):
    def run(self):
        global queue
        count=0
        while True:
            if queue.qsize()<1000:
                for i in range(100):
                    count+=1
                    msg=f'{count}st product'
                    queue.put(msg)
                    print(msg)
                time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        count=0
        while True:
            if queue.qsize()>100:
                for i in range(10):
                    msg=f'{self.name} consume {queue.get()}'
                    print(msg)
                time.sleep(1)

if __name__ == '__main__':
    queue=Queue()
    p=Producter()
    c=Consumer()
    p.start()
    time.sleep(1)
    c.start()