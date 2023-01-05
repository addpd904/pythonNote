# data_container:list tuple str set dict
# 一、list
# 1.conception
li =['zhangshan',99,88]
for i in li:
    print('%s '%i,end='')
print(li)
li1=[['zs',2],[3,'ls']]
print(li1)
print(li1[-1][-2])
# 2.method
# search for element and return its index
index=li.index(99)
# insert element
li.insert(1,'li')
print(li)
# append element at the end of list
li.append('ls')
# append a list at the end of list
li.extend(li1)
print(li)

# new list
myli=[1,2,2,'ls']
# delete element
element=myli.pop(2)
# remove the element that firstly is found
myli.remove(2)
# count
count=myli.count(2)
# get length of list
len1=len(myli)
# clear list
myli.clear()

# 3.iteration
index1=0
myli1=[1,2,3,'8']
# len1=len(myli1)
while index1 < len(myli1):
    print(f'{myli1[index1]}')
    index1+=1
for i in myli1:
    print(i)
# 4.judge if element is in list
print(1 in myli1)


# 二、tuple only read ,don't allow to modify
tup=(1,'hi',[33,22])
print(tup)
# tup=('hi'),this is a str.When you add a comma,it will become a tupletup=('hi',)
len22=len(tup)
# the list that is in tuple can be modified
tup[2][0]=88


# 三、str,only read ,don't allow to amend
str1='hello world'
print(str1[-2])
# find element
str1.index('h')
# replace,return a new str
str2=str1.replace('h','hihi')
# split,return a list
list4=str1.split(' ')
print(type(list4))
# strip ,remove the specified character
str4=str1.strip('he')
count5=str1.count('l')

