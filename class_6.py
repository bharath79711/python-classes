"""
slicing and indexing
"""
#-6 -5 -4 -3 -2 -1
#p   y  t  h  o  n

#p y t h o n
#0 1 2 3 4 5==> indexing
#str[start:stop:increment]
x="python"
print(x[0])#p
print(x[4])#o
print(x[2:5])#thon
#2:5:1
print(x[1:4:2])#yh
print(x[1:])#ython
print(x[1::1])#ython
print(x[:4:])#pytho
print(x[::])#python
print(x[-1])#n
print(x[-2:-5:-1])#ohty
print(x[-1::-1])#nohtyp
print(x[::-1])#0:5:-1
#54321

# Ranging
# range
# range(start:stop:increment)
x = range(10, 0, -1)
# print(list(x))
# basic functions
# print() to display the value
# len() to length find

# print(len("thiru.ala"))
# loops(for,while) break,continue
y = range(10)  # [0,1,2,3 4 ..9]
"""
for variable in squence:
   print(variable)

for i in y:#[0...9]
    print(i)

"""
for i in y:
    print("before cond:", i)  # 0123456
    if i == 6:
        break
    print("after cond:", i)  # 012345