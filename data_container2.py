# slice up sequence,for instance:list,tuple,str
#get a new sequence
tup1=(1,2,3,5)
# start:end:step,don't include end
tup2=tup1[0:2:1]
print(tup2)
tup3=tup1[:]
tup4=tup1[3:0:-1]
# Reverse
tup5=tup1[::-1]



# 一、set,don't allow to repeat,no order
# 1.conception
set1={'hi','hello'}
# empty set
set2=set()
set3={'hi'}
# 2.method
# add
set1.add('bye')
set1.remove('hi')
# get a element randomly
ele1=set1.pop()
# get a difference set between two sets
set4=set1.difference(set3)
# eliminate differences
set1.difference_update(set3)
# union,merge
set5=set1.union(set3)
# 3.traverse
for el in set1:
    print(el)


# 一、dict,don't allow to repeat,no order
# 1.conception
dict1={'zs':11,'ls':88,'ww':99}
print(dict1)
dict2=dict()
print(dict1['zs'])
# 2.operation
dict1['zs']=100
# add,delete
dict1['ll']=77
dict1.pop('zs')
# get all keys and values
keys=dict1.keys()
for key in keys:
    print(dict1[key])
for key in dict1:
    print(dict1[key])
# 3.method
# get max element
max(dict1)
# 4.get a value via key.If the key is not in the dict,return None
zsscore=dict1.get('zs')
# 5.judge if key is in list
print('zs' in dict1)

# 二、General operation
# type conversion
# list(tuple),str,set,dict;tuple(list),str,set,dict;str();set()
# sorted,sorted() return a list
mylist1=[['zs',88],['ls',100],['zjl',77]]
def mysort(element):
    return element[1]
mylist1.sort(key=mysort)
print(mylist1)
# 三、comparison in string