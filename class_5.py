"""
for i in range(x):
    print(i*y)

def func_name(x,y):
    for i in range(x):
        print(i*y)

x = int(input("enter the value x:"))
y = int(input("enter the value y:"))

data = func_name(x,y)
print(data)
print("==========")
x = int(input("enter the value x:"))
y = int(input("enter the value y:"))
data2= func_name(x,y)
print(data2)
"""

"""
def func_sum(x, y):
    value = x + y
    return value  # 30


data_sum = func_sum(10, 20)  # 30
print(data_sum)
print(data_sum * 20)


"""
'''
for i in range(10):
    if i==5:
        break
    print(i)

x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))

while x>y:
    print("the value is x greater than y:",x*y)
    y=y+2
'''
x = [1, 6, 1, 6, 8, 1, 9, 3, 1, 4]
y = [2, 5, 7, 11, 0, 9]
print("len(x):", len(x))
print("len(y):", len(y))
print("max(x):", max(x))
print("min(x):", min(x))
print("max(y):", max(y))
print("min(y):", min(y))
print("sum(x):", sum(x))
print("sum(y):", sum(y))

x.insert(1, 2)
print(x)

print(x.count(1))
print(y.index(0))
print(x.index(3))

x.append(5)
print(x)

# x.extend(y)
# print(x)

x.remove(9)
print(x)

x.pop()
print(x)

x.pop(0)
print(x)

x.reverse()
print(x)

for i in reversed(x):
    print(i)

x.sort()
print(x)

x.sort(reverse=True)
print(x)

x.copy()
print(x)

x.clear()
print(x)





























































