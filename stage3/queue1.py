from multiprocessing import *
# 一、queue
# 1.creat a queue and set mount of ele
# 2.mount of element in queue
q1=Queue(3)
# 3.insert element
q1.put('message1')
q1.put('message2')
q1.put('message3')
# 4.block:true ,timeout:after queue is full and element4 wait for 3second ,a exception will be thrown
# q1.put('message4',block=True,timeout=3)
# 5.full:judge if queue is full
print(q1.full())
# 6.get ele in queue
print(q1.get())
print(q1.get())
print(q1.get())
# print(q1.get(block=True,timeout=3))
# 7.empty:judge if queue is empty
print(q1.empty())
# 8.get numbers of element in queue
print(q1.qsize())
