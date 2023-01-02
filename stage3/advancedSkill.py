# 一、closure
# 1.model
# shortcoming:variable occupy memory for a long time
def outer(logo:str):
    def inner(msg):
        print(f'{logo}  msg  {logo}')
    return inner
fn1=outer('mylogo')
fn1('hello')
fn1('hoe are you')

fn2=outer('testlogo')
fn2('bye')
# 2.app atm
# advantage:prevent variable from modify
def atm(init_money):
    def account(mon,deposit=True):
        nonlocal init_money
        if deposit==True:
            init_money+=mon
        else:
            init_money-=mon
        print(f'the balance is {init_money}')
    return account
account1=atm(0)
account1(1000)
account1(300,False)

# 二、decorator: add new features for function
# 1.basic grammer
# decorator
def deco(func):
    def inner():
        print('go to sleep')
        func()
        print('wake up')
    return inner
# way1 to use decorator
def sleep():
    print('sleeping')
fun1=deco(sleep)
fun1()
# way2 to use decorator
@deco
def sleep2():
    print('sleeping2')
sleep2()

# 三、singleton pattern.just provide a instantiation
from singletonPatternClass import str_tool
s1=str_tool
s2=str_tool
print(id(s1))
print(id(s2))

# 四、factory pattern
from factoryPatClass import Factory
factory=Factory()
work1=factory.get_person('w')
