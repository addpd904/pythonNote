import threading
import time
# Multithreaded execution in parallel.(多线程并行执行).process
# 一、
# 1.basic grammer
# singal thread
# def sing():
#     while True:
#         print('singing')
#         time.sleep(1)
# def dance():
#     while True:
#         print('dancing')
#         time.sleep(1)
# if __name__ == '__main__':
#     sing()
#     dance()
# Multithreaded execution
def sing(msg):
    while True:
        print(f'{msg}singing')
        time.sleep(3)
def dance(msg):
    while True:
        print(f'{msg}dancing')
        time.sleep(3)
if __name__ == '__main__':
    dance_thread=threading.Thread(target=dance,args=('ls ',))
    sing_thread=threading.Thread(target=sing,kwargs={'msg':'zs '})
    sing_thread.start()
    dance_thread.start()
