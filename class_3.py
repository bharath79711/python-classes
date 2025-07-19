# if concept
"""
if x>y:
    print("x is greter than y")
"""
# if else
"""
if x>y:#10>10
    print("x is greter than y")
else:
    print("x is less than y")


"""
# if elif else
"""
Ex:2
if x>y:#10>20
    print("x is greter than y")
elif x==y:#10==20
    print("x is equal to y")
else:
    print("x is less than y")
x = 2
y = 6
z = 9
Ex:3
if x>y and y>z:#2>6 and 6>9 #false #false ==false
    print("x is greter than y and z")

elif x<y and y<z:#2<6 and 6<9 #true #true  == true
    print(" x is smaller than y and z")

elif x<y or y<z:#
    print(" x is less than y or y is less than z")

else:
    print(" i am in else block")
"""
# Ex4
"""
x = 10
y = 20
z = 30
if x>y and y>z:
    print("x is greter than y and z:",x+y+z)

elif x<y and y<z:
    print(" x is smaller than y and z:",x*y*z)

elif x<y or y<z:
    print(" x is less than y or y is less than z:",x-y-z)

else:
    print(" i am in else block:",x,y,z)


#Ex:4
name = "anu and bharath learning python"

if "anuu" in name:#False
    print("anu is there in name")
elif "bharathu" in name:#False
    print("bharath is there in name")
else:
    print("anuu and bharathu not there in name")
# ex:5
x = 10
y = 3

if x>y and x%y==1:# 10>3 and 10%3==1 #T and T =T
    print("x is :",x)
else:
    print("y value:",y)
#ex:
x = 10
y = 10

if x==y:#10==20
    print("x is equal to y")
elif x!=y:#10 not equal to 20
    print("x is not equal to y")

Ex:
x = input("enter x value:")
print("x value is:",x,type(x))
if type(x)==str:
    z = int(x)
    print("convert to int:",z,type(z),z+30)
"""

name = input("Enter Your Name:")
age = input("Enter your age:")
course = input("Enter Your Course:")
if name and int(age) >= 20 and course == "BTech":  # T and T and T =T
    print(name, age, course)
else:
    print("please check age is greter than 20 and Course should be BTech")




























