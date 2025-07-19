# x=(1,2,3,2,4,2,5,6,2,7,2,8)
''''
print("2 count:",x.count(2))
import copy
y=copy.copy(x)
print(y)

z=copy.deepcopy(x)
print(z)
print(tuple(reversed(x)))

print(sorted(x))
print(sorted(x,reverse=True))

x=(1,2,3,2,4,(2,5,6,2),7,2,8)
flat=[]
for item in x:
    if isinstance(item,tuple):
        flat.extend(item)
    else:
        flat.append(item)
        print(flat)
        print(flat.count(2))
        print(sorted(flat))
        print(sorted(flat,reverse=True))

'''
'''
x=(1,2,3,2,4,2,5,6,2,7,2,8)
print(x[5])
import copy
y=copy.copy(x)
z=copy.deepcopy(x)
print("y:",y)
print("z:",z)
print(tuple(reversed(x)))
a=sorted(x)
b=sorted(x,reverse=True)
print(type(a),a)
print(type(b),b)
'''
'''
x=(1,2,3,2,4,(2,5,6,2,7),2,8)
flat=[]
for item in x:
    #print(isinstance(item,tuple))
    if type(item)==tuple:
        flat.extend(item)
        print(flat)
    else:
        flat.append(item)
        print(tuple(sorted(flat)))
'''
'''
x=(5,(2,4),7,(1,3,6),8)
y=[]
for item in x:
    if type(item)==tuple:
        y.extend(item)
        print(y)
    else:
        y.append(item)
        print(sorted(y))
'''
'''
marks=((40,30),20,10,(60,50),70)
y=[]

for item in marks:
    if type(item)==tuple:
        y.extend(item)
        print(y)
    else:
        y.append(item)
        print(sorted(y))


print(marks[3])

'''
data = (1, (5, 3), 2, (8,), 0)
y = []
for item in data:
    if type(item) == tuple:
        y.extend(item)
        print(y)
        '''
    else:
        y.append(y)
        print(y)
        '''






























