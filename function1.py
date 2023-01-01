# 一、return more than one value
def fun1():
    return 1,'hi'
x, y = fun1()
# 二、pass parameters
# 1.pass via key value
def fun2(name,score,age):
    return 0
fun2(age=12,name='zs',score=99)
#2.default parameter,must put it at the end
def fun3(score,age,name='ls'):
    return 0
fun3(88,19)
# 3.Indefinited length parameters
# args is a tuple
def fun4(*args):
    return 0
fun4(1,2,3,4)
# kwargs is a dict
def fun5(**kwargs):
    return 0
fun5(zs=7,ls=99)

# 三、function as a parameter
def fun6(compute):
    res=compute(1,8)
    return res
def sum(a,b):
    return a+b
def mul(a,b):
    return a*b
print(fun6(sum))
fun6(mul)
# 四、 anonymous function,lambda,just a line
def fun7(compute):
    res=compute(1,8)
    return res
fun7(lambda a,b:a+b)
