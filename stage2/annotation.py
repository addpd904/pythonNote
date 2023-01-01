# 一、make annotation for variable
a: int=10
b:str='hi'
class Stusent:
    pass
stu:Stusent=Stusent()

list1:list=[1,3,4]
list2:list[int]=[1,3,4]
dict1:dict[str,int]={'zs':88,'ls':89}
dict2={'zjl':78,'ls':89}             #type:dict[str,int]

# 二、make annotation for function
def func(data:list,num: int)->int:
    for ele in data:
        print(ele)
    return 100

# 三、Union
from typing import Union
list3:list[Union[int,str]]=[2,2,'hi']

def fun1(data:Union[int,str]):
    pass
