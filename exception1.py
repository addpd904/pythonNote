# 一、grammar
# 1.catch exception,basic grammar
try:
    f1 = open('1.txt', 'r', encoding='utf-8')
except:
    print('there is a bug')
else:
    print('well done! no bug')
finally:
    print('the program has end')
# 2.catch the specified
try:
    print(name)
except NameError as e:
    print("the variable is not definded")

# 3.catch multiple exception
try:
    1/0
except (NameError,ZeroDivisionError) as e:
    print("the variable is not definded or ZeroDivisionError")

# 4.catch all exception
try:
    3/0
except Exception as e:
    print(e)
else:
    print('well done! no bug')

# 二、exception pass
def fun1():
    return 1/0
def fun2():
    fun1()
def main():
    try:
        fun2()
    except Exception as e:
        print(f'the wrong message:{e}')
main()
