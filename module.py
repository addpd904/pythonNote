# 一、import basic grammar
#1.import,import all function and class
# time.py
import time as ti
print('hi')
ti.sleep(1)
print('hello')
# 2.from
# just import the function sleep()
from time import sleep as sl
sl(1)
#3.*
from time import *

# 二、DIY module
from mymodule import sum
sum(2,4)

# 三、DIY package
# import ii2hq.com.mymodule as mym1
# mym1.fun1()
from ii2hq.com import mymodule as mym1
mym1.fun1()

# 四、install other package,tensorflow,pandas....
# pip install
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple



