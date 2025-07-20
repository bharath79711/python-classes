
#advance
#lambda functions ==> (lambda arg:expression)(value)
#generators
#decorators
#iterators
"""
def func_name(x,y):
    z = x+y
    return z

dd = func_name(10,20)

dd = (lambda x,y:x+y)(10,20)
# print(dd)
x = [1,2,3]
# data = (lambda x:(i for i in x if i % 2 == 0))((1,2,3,4,5,6))
# print(list(data))

data = (lambda x:(i*i for i in x))
print(data(x))
"""
#Generator
def func_name(x):
    for i in x:#[1,2,3,4,5]
        yield i


data = func_name([1,2,3,4,5])#1,2,3,4,5
print((list(data)))