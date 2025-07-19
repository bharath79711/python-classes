# Ex:1
'''
x=[1,2,3,3,4,4,5,6,7,8,8,9,10,10]
print(set(x))
#out put:{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
'''
# Ex:2
''''
x={1,2,3,4}
x.add(5)
print(x)
#output:{1, 2, 3, 4, 5}
x.remove(3)
print(x)
#output:{1, 2, 4, 5}
num=4
if num in x:
    print(f"{num}:in x")
else:
    print(f"{num}:not in x")

print(len(x))
'''
# converting list to set
'''
x=[1,2,2,3,4,4,5]
print(set(x))
'''
# converting tuple to set
'''
x=(10,20,30)
print(set(x))
'''
# x={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
'''
x.clear()
print(x)
'''
'''
y=x.copy()
print(y)
'''
'''
x={"Bharath",12,"tiru",1223,"apple",21.2}
print(type(x),x)
'''
'''
x={1,1,2,2,3,4,5,6,6,7}
y={1,2,6,8,8,9,10,11,12}
print("union:",x.union(y))
print("intersection:",x.intersection(y))
print("difference b/w x and y:",x.difference(y))
print("symmetric difference:",x.symmetric_difference(y))
'''
'''
x={1,2,3,4,5,6}
y={1,2,3}
sub_set=x.issubset(y)
print("sub set:",sub_set)
super_set=x.issuperset(y)
print("super set:",super_set)
x.discard(7)
print(x)
x.remove(4)
print(x)
'''
x = [1, 2, 3, 4, 5, 6, 7]
y = [4, 5, 6, 8, 9, 10, 11]

xx = set(x)
yy = set(y)
print("common elements:", xx.intersection(yy))
print("symmetric difference:", xx.symmetric_difference(yy899






























