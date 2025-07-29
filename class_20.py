
class Department:
    def method(self,list_sequence):
        result=[]
        for i in list_sequence:
            if i % 2==0:
                result.append(i**2)
            else:
               result.append(i**3)
        return result
    def method2(self,strn):
        rev_strn=strn[::-1]
        return rev_strn

Dep_obj=Department()

x=Dep_obj.method([1,2,3,4,5,6])
print(x)

y= Dep_obj.method2("Talari Bharath")
print(y)

"""
class student:
    def greet(self,name):
        return f"Hello! Good Morning.{name}"

x=student()
y=x.greet("Bharath")
print(y)
"""
"""
class student:
    def __init__(self,name):
        self.name=name
    def show(self):
        return ("student name is:",self.name)

s1=student("Bharath")
x=s1.show()
print(x)
"""
"""
class student:
    def __init__(self,name):
       self.rev_str= name[::-1]
    def show(self):
        return "student name is:", self.rev_str
x=student("Bharath")
y=x.show()
print(y)
"""
"""
class car:
    def __init__(self,Brand,colour):
        self.Brand=Brand
        self.colour=colour
    def show_info(self):
        return (f"Brand:{self.Brand},colour:{self.colour}")
ob_je=car(input("Enter your car Brand:"),
          input("Enter your selecting colour:"))
sho_obj_in= ob_je.show_info()
print(sho_obj_in)
"""
"""

class maths:
    def square(self,*args):
        return [i**2 for i in args]

M=maths()
x=M.square(2,4,6,8,10)
print(x)
"""
"""
class maths:
    def square(self,list_seq):
        return [i**2 for i in list_seq if i%2==0]

M=maths()
Sq_val = M.square([1,2,3,4,5])
print(Sq_val)
"""
"""
class number_check :
    def check_even_odd(self,num):
        if num%2==0:
            return "Even"
        else:
            return "odd"

obj_num=number_check()
check_num=obj_num.check_even_odd(int(input("Enter a number:")))
print("The number is :",check_num)

"""


"""
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def inf(self):
        return (f"person name is: {self.name} and his age is:{self.age}")

name=person("Bharath",18)
info=name.inf()
print(info)

name=person(input("Enter your name : "),
            int(input("Enter your age:")))
info=name.inf()
print(info)
"""
"""
class person :
    def __init__(self,name,age,Gender,mail,mobile_no):
        self.name=name
        self.age=age
        self.Gender=Gender
        self.mail=mail
        self.mobile_no=mobile_no

    def inf(self):
        return f"name:{self.name}," \
               f"age:{self.age}," \
               f"Gender:{self.Gender}," \
               f"mail:{self.mail}," \
               f"MObile_no:{self.mobile_no}"


Bio_ob=person("Bharath",28,"Male","bharathkumartalari70@gmail.com",9010297520)
Bio_data=Bio_ob.inf()
print("person Bio data :",Bio_data)

"""
"""


class person :
    def __init__(self,name,age,Gender,mail,mobile_no):
        self.name=name
        self.age=age
        self.Gender=Gender
        self.mail=mail
        self.mobile_no=mobile_no

    def inf(self):
        return f" name:{self.name}," \
               f"age:{self.age}," \
               f"Gender:{self.Gender}," \
               f"mail:{self.mail}," \
               f"mobile_no:{self.mobile_no}"



Bio_ob=person(input("Enter your name : "),
              int(input("Enter your age : ")),
                  input("Enter your Gender : "),
                  input("Enter your mail id : "),
                  int(input("Enter your mobile no : ")))
Bio_data=Bio_ob.inf()
x={}
x[Bio_ob.name]=Bio_data
print(x)
"""