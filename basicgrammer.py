#cancle newline
print('hello \n hi',end='')
print('\tworld ')
# comments # and ''''''
# 一、sting format
#1.
name='zhangshan'
score=99.9
print(f'nama:{name},math score:{score}')
#2.
print('name:%s math score:%8.3f'%(name,score))

#二、input
"""
a=input('input a num')
b=input()
print(a+b)
"""

#三、bool
result=5>8
print(f'5 is larger than 8?{5>8}')

#四、if else
#Py judge that if the statement belong to 'if' via indentaton
a=18
b=18
if a>b:
    print(f'a {a} is larger than b {b}')
elif a==b:
    print(f'a {a} is equal to b {b}')
else:
    print(f'a {a} is less than  b {b}')

#五、 while
i =0
sum=0
while i<100:
    i+=1
    sum+=i;
print(sum)

#Haskell
i1=1
while i1<=9:
    j=1
    while j<=i1:
        print(f'{i1}*{j}={i1*j}\t',end='')
        j+=1
    print()
    i1+=1

#六、for 轮询机制，像待办事项,in后写序列类型
name ='zhangshan'
for x in name:
    print('%s\t'%x,end='')
for i2 in range(5):#range(1,6,2)
    print('%d\t'%i2,end='')
# 2.scope
print()
for i3 in range(1,4,2):
    print(i3)
print(i3)

# 七、function
def sum(a,b):
    return a+b
print(sum(2,5))
# return None,amount to false when you use it in 'if'
def sum1(a,b):
    i4=100
print(type(sum1(2,3)))
# local variable and global variable
# global variable
num1=100
def sum2(a,b):
    # local variable
    i4=100
    # Modify global variable in function
    global num1
    num1=2000
    return a+b