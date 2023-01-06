import threading
# create a thread local object
# the threadlocal variable is a global var,but it just is belong to a thread
local=threading.local()

def process_student():
    student_name=local.name
    print(f'name {student_name}\n')

def process_thread(name):
    local.name=name
    process_student()
t1=threading.Thread(target=process_thread,args=('zs',))
t2=threading.Thread(target=process_thread,args=('ls',))
t1.start()
t2.start()