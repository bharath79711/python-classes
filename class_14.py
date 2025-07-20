
"""x = [1,2,3,4,5]
data =iter(x)
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))"""
'''
def func_name(x,y):#20, 40
    def inner(k,z):#20,40
        data2=k+z#60
        return data2

    data = inner(x,y)#60

    return data

# data = func_name(20,40)#60
# print(data)

def func_name2(x,y):#20, 40
    def inner1(k,z):#20,40
        data2=k+z#60
        return data2

    data3 = inner1(x,y)

    return data3


# decorators is function ,@, it is top of the fun
#with @
def func_deco(func):
    def inner(x,y):
        if y>=1:
            return func(x,y)
        else:
            return "y should be greater than 1"

    return inner


@func_deco
def divide(x,y):
    return x/y


data = divide(20,10)
print(data)
data = divide(10,0)
print(data)

'''

# without @
def func_deco2(func):
    def inner(x,y):
        if x>y:
            return func(x,y)
        else:
            return "x should be greater than y"

    return inner


def divide2(x,y):
    return x/y

data=func_deco2(divide2)
data2=data(2,5)
print(data2)