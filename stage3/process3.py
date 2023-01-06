# 一、process pool,for creating a large number of process
import multiprocessing
import time
def worker2(msg):
    print(f'work start{msg}')
    time.sleep(2)
    print(f'work end {msg}')
# numprocess: the max number of subprocess;when the pool is full ,the new subprocess need to wait
if __name__ == '__main__':
    pool=multiprocessing.Pool(3)
    # 1.non - blocking
    for i in range(5):
        msg='task%d'%i
        # async:execute the subprocess at the same time;connect async ajax
        # non-blocking
        pool.apply_async(worker2,(msg,))
    # before call join(),we need to close pool
    pool.close()
    pool.join()
'''
    # 2.blocking
    for i in range(5):
        msg='task%d'%i
        # apply:just like single process.just after task 1 end,task2 run
        # non-blocking
        pool.apply(worker2,(msg,))
    pool.close()
    pool.join()
'''