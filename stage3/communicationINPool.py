import time
from multiprocessing import Process,Queue,Pool,Manager


def write(q):
    a=['a','b','c','d']
    for i in a:
        print('put the value :%s' % i)
        q.put(i)
        time.sleep(1)
def read(q):
    for i in range(q.qsize()):
        print('get the value :%s'%q.get())
        time.sleep(1)
if __name__ == '__main__':
    # we need to use Manager.Queue rather than Queue,otherwise ,a exception will be thrown
    q1=Manager().Queue(4)
    pool=Pool(3)
    # apply,blocking
    pool.apply(write,(q1,))
    # after the subprocess pw end,the subprocess just start
    pool.apply(read,(q1,))
    pool.close()
    pool.join()
