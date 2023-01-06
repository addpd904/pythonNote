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
        # we can use sleep to let the cpu release
        time.sleep(2)
def dance(msg):
    while True:
        print(f'{msg}dancing')
        time.sleep(3)
if __name__ == '__main__':
    dance_thread=threading.Thread(target=dance,args=('ls ',))
    sing_thread=threading.Thread(target=sing,kwargs={'msg':'zs '})
    # 1.start thread
    sing_thread.start()
    dance_thread.start()
    # 2.join ,main thread wait for subthread
    sing_thread.join()
    dance_thread.join()
    # 3.judge if subthread is alive
    print(sing_thread.is_alive())