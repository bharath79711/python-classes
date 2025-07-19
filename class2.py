"""
# Type Casting
x = 100
y ="300"
z = 16.6
#str to int
name = str(x)#"100"
print("x int to str:",name,type(name))
#str to float
yy = float(y)
print("str to float:",yy,type(yy))

#int to str
xx = str(x)
print(f"int to str{x} type is {type(xx)}")
#int to float
xxy = float(x)
print("in to float:",x,type(xxy))


#float to str
zz = str(z)#str
print("float to str:",z,type(zz))
#float to int
zzz = int(z)#16
print("float to int:",z,type(zzz))
"""
# operators
# arthimatic op
x = 10
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print("floor divi",x//y)

#comparitive
print("x is euql to y:",x==y)
print("x not equal to y:",x!=y)

#relation opo
print("x >y:",x>y)
print("x<y:",x<y)
print("x>=y:",x>=y)
print("x<=y:",x<=y)

# logical op
yy= x>y   #10>3 #True
zz = x<y #10<3#False
z = 30
kk = x<z #10<30#True
print("and logical T and T =T:",yy and zz)#False
print("and logical T and T =T:",yy and kk)#True

print("or logical T or T =T:",yy or zz)#True
print("or logical T or F =T:",yy or kk)#True

print("not:",not yy)#False

# membership
name = "bangalore"
print("membetship op:","b" in name)# True
print("membetship op:","k" in name)# False
print("membetship op:","c" not in name)# True














