import time
from multiprocessing import Process,Queue


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
    q1=Queue(4)
    pw=Process(target=write,args=(q1,))
    pr=Process(target=read,args=(q1,))
    pw.start()
    pw.join()
    # after the subprocess pw end,the subprocess just start
    pr.start()
    pr.join()