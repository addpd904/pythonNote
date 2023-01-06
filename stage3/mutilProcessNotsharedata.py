from multiprocessing import Process
# the global variable don't be share between every process
num=0
def task1():
    global num
    num += 5
    print('task1 num', num)

def task2():
    global num
    num += 30
    print('task1 num', num)
if __name__ == '__main__':
    print('mainprocess start')
    p1=Process(target=task1)
    p2=Process(target=task2)
    p1.start()
    p2.start()
    # main process wait for subprocess
    p1.join()
    p2.join()
    print('main process num:',num)

