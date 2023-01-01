# 一、write file
# open(name,mode,encoding)
f=open('E:/test.txt','w',encoding='UTF-8')
# f.flush(),let the data in internal storage into disk
f.write('hi \n hi \n how are you')
f.flush()
f.close()


# 二、read file
# open(name,mode,encoding)
f=open('E:/test.txt','r',encoding='UTF-8')
# 1.return a str,so we can use function like strip(),split()
str1=f.read()
print(str1)
# 2.
# f.readlines() read all,return a list
# f.readline() read a line
# 3.traversal
# for line in f:
#     print(line)
f.close()
# 4.auto close file
with open('E:/test.txt','r',encoding='UTF-8') as f1:
    for line in f1:
        print(line,end='')
# we can use strip() to remove "\n"


# 三、append date
# open(name,mode,encoding)
f=open('E:/test.txt','a',encoding='UTF-8')
# f.flush(),let the data in internal storage into disk
f.write('\nbye \n goodbye')
f.close()

