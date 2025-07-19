'''
List:
------
-[]
-list
-homogeneous and heterogeneous
ex:
x=[1,1,2,3,4,5]
y=[1.1,2.2,...]
zz=[str,str,str]
z=[1,1.1,"tiru",True]
-mutable or editable or changeable
- increase length or decrease length of elements
-supports indexing

functions
--------
len(x)
max(x)
min(x)
sum(x)

methods
-------
list.count(value)
list.find(value)
list.insert(index,value)
list.append(value)
list.extend(list)
list.remove(value)
list.pop()
list.reverse()
x=[1,2,3,4,1,1,5]
print("length:",len(x))
print("max:",max(x))
print("min:",min(x))
print("sum:",sum(x))

print("count:",x.count(1))
x.append(7)
print("append:",x)
y=[8,9,10]
x.extend(y)
print("extend:",x)
print("find the index:",x.index(1))
x.remove(1)
print(x)
x.pop()
print(x)
xx

'''
x=[1,2,22,3,35,43,1,4]

"""
for i in x:
    if i==4:
        x.append(10)
print(x)

for i  in x:#[1,2,3,4,2,4]
    if i==3:
        break
    x.append(i*2)
print(x)

x.clear()
print(x)

x.sort(reverse=True)
print(x)
print(sorted(x))

del(x)
print(x)

y=x.copy()
print("y value",y)
x.append(33)
print("append x:",x)
print(y)
"""
#shallow copy
import copy
y=copy.copy(x)
print("y value is:",y)
x.append(33)
print("x value is:",x)
print("y value is:",y)


#deep copy
xx=[1,2,3,[4,5,6]]#nested list
yy=copy.copy(xx)
print("yy is:",yy)

import copy
x=[1,2,3,4,[4,5,6,7],10]
#  0,1,2,3,   4,      5
"""
print(x[2])#3
print(x[3])#
print(x[4])#[4,5,6,7]
print(x[5])#10
print(x[4][1])#5
y=copy.copy(x)
print("value y:",y)
print("value x:",x)
x[4][1]=44
print("value x:",x)
print("value y:",y)
x[1]=55
print("value x:",x)
print("value y:",y)"""
y=copy.deepcopy(x)
print("value x:",x)
print("value y:",y)
x[4][1]=44
print("value x:",x)
print("value y:",y)
x[1]=55
print("value x:",x)
print("value y:",y)