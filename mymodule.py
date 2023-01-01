def sum(a,b):
    print(a+b)
    return a+b
def mul(a,b):
    print(a*b)
#value: just the sum() can be use
__all__ = ['sum']
# if __name__ == '__main__',value:prevent run when you import the module
if __name__ == '__main__':
    sum(4,7)
