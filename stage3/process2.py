# 一、generate a subprocess via creating a class that extend class Process;overload function run
import multiprocessing
import time
from multiprocessing import Process


class workerProcess(Process):
    def __init__(self,interval):
        Process.__init__(self)
        self.interval=interval
    # after you1 call statr(),the run() will be executed
    def run(self):
        print('work start')
        time.sleep(self.interval)
        print('work end')
if __name__ == '__main__':
    p3=workerProcess(1)
    p3.start()

