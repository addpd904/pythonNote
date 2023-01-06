import multiprocessing
import time
from multiprocessing import  Process
def run_test(name,age,**kw):
    print('subprocess is runing')
    print(f'dict{kw}')
def worker(interval):
    print('work start')
    time.sleep(interval)
    print('work end')
# 一、
#   1.basic grammer
if __name__ == '__main__':

    print('main progress is executing')
    # create a subprocess pass argument
    p=Process(target=run_test,args=('zjl',19),kwargs={'zs':100,'ls':99})
    # launch subprocess
    p.start()
    # 2.join
    p2=Process(target=worker,args=(1,))
    p2.start()
# let the main process be executed after subprocess end.main process will wait for subprocess

    p2.join()
    # main process just waif for no more than 3 seconds
    # p2.join(3)
    # 3.property : pid,process's id
    print(p2.pid)
    # 4.is_alive : judge if process is alive
    print(p2.is_alive())
    print('main process end')

