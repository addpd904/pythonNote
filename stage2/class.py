#一、 basic grammar
# design a blueprint
class Student:
    name=None
    gender=None
    age=None
    # self,just like this in java
    def sing(self,num):
        print(f'I am {self.name},i can sing {num} songs')
# generate a object,instantiation
stu1=Student()
stu2=Student()
stu1.age=18
stu1.gender='nan'
stu1.name='zs'
stu1.sing(3)

# 二、1.Construct Method.When you instantiate a class,it will be executed.2.Override
class Dog:
    name = None
    gender = None
    age = None
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
        print('the construct Method has executed')
    # 1.Override Magic methods(start with '__'and end with '__')
    # <(less than)
    def __lt__(self, other):
        return self.age<other.age
    # <=(less or equal)
    def __le__(self, other):
        return self.age<=other.age
    # ==
    def __eq__(self, other):
        return self.age == other.age
    # override __str__
    def __str__(self):
        return f'{self.name},{self.age},{self.gender}'
    # 2.self,just like this in java
    def sing(self,num):
        print(f'I am {self.name},i can sing {num} songs')
dog1=Dog('heidog','nan',20)
dog2=Dog("baidog",'nv',19)
# amount to : dog1.__lt__(dog2),so return False
print(dog1<dog2)
dog1.sing(8)

# 三、encapsulation,private member and method，just like private member in java. just can be use in inside
class Cat:
    name=None
    # private member and method start with '__'
    __gender=None
    age=None
    # self,just like this in java
    def sing(self,num):
        print(f'I am {self.name},i can sing {num} songs')
    # private member and method start with '__'
    def __eat(self,num):
        print(f'I am {self.name},i can eat {num} pieces of bread')
# generate a object,instantiation

# 四、extend
# 1.basic grammer
class Phone:
    producer=None
    IMEI=None
    ver = '9.0'
    def surfInternet(self):
        print('phone can surf Internet')
    def facialRecognition(self):
        print("phone have facial Recognition v1.0")
# 2.multiple extend
class NFC:
    ver='7.0'
    def read_card(self):
        print('i can read card')
# pass,just like placeholder.indicate that the statement empty
class XiaoMi(Phone,NFC):
    pass
mi1=XiaoMi()
print(mi1.ver)
# 3.Override member of superclass.call the member of superclass
class HuaWei(Phone,NFC):
    producer = 'huawei'
    ver = 11.0
    def facialRecognition(self):
        print("phone have facial Recognition v5.9")
    #     call the member of superclass
    def call_memberOfSuperclass(self):
        print(Phone.ver)
        print(super().ver)
        Phone.facialRecognition(self)
        super().facialRecognition()
hua1=HuaWei()
hua1.call_memberOfSuperclass()

# 五.polymorphism ˌpɒlɪˈmɔːfɪz(ə)m.same thing ,but behavior not same
# abstract class,just like a standard
class Animal:
    name=None
    # abstract method
    def __init__(self,name:str):
        self.name=name
    def eat(self):
        pass
class Tortoise(Animal):
    def eat(self):
        print(f'{self.name} eat apple')
class Rabbit(Animal):
    def eat(self):
        print(f'{self.name} eat strawberry')
def eatfruit(an:Animal):
    an.eat()
tor=Tortoise('tortoise')
rab=Rabbit('rabbit')
eatfruit(tor)
eatfruit(rab)




