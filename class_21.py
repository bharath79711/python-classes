# inheritance
#single level and multi level inheritance
"""
class Grandfather:
    def my_char1(self):
        return "Head of the family "
    def my_char2(self):
        return "Ruler of his village  "
class father(Grandfather):
    def my_char3(self):
        return "Drinker"
class son(father):
    def my_char4(self):
        return "traveller"

so_obj = son()
print(so_obj.my_char1())
print(so_obj.my_char2())
print(so_obj.my_char3())
print(so_obj.my_char4())

"""

#Multiple inheritance
"""
class father:
    def my_char1(self):
        return "strong in low situation "

class mother:
    def my_char2(self):
        return "more sensitive nature"

class son(father,mother):
    def my_char3(self):
        return "Too lazy to work"

obj=son()
print(obj.my_char1())
print(obj.my_char2())
print(obj.my_char3())
"""
#hierarchical
"""
class Library:
    def mech(self):
        return "mech Books"
    def eee(self):
        return "eee Books"
    def ece(self):
        return "ecee Books"
class Mech(Library):
    def mech_in(self):
        return "Mech Books only"
class Eee(Library):
    def eee_in(self):
        return "Eee Books only"

class Ece(Library):
    def ece_in(self):
        return "Ece Books only"


x=Ece()
print(x.ece_in())
print(x.ece())
print(x.eee())
print(x.mech())
"""
"""
class Department:
    def public(self):
        return "iam in public method"
    def _protected(self):
        return "iam in protected method"
    def __private(self):
        return "iam in private method"


Dep=Department()
print(Dep.public())
print(Dep._protected())
print(Dep._Department__private())
#print(Dep.__private())  directly used in this way error found

"""
#_____Methods_____
#self Method

class employee:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def display(self):
        return self.x*self.y


#static method

    @staticmethod
    def even_sq(*args):
        even_numbers = []
        for x in args:
            if x % 2 == 0:
                even_numbers.append(x ** 2)
        return even_numbers

    @classmethod
    def odd_sq(cls,*args):
        odd_numbers = []
        for x in args:
            if x % 2 != 0:
                odd_numbers.append(x ** 2)
        return odd_numbers

ob=employee(10,20)
print("x*y:",ob.display())
print(ob.odd_sq(1,2,3,4,5,6,7,8,9))
print(ob.even_sq(1,2,3,4,5,6,7,8,9))
#del ob
#print(ob)
# gc :- garbage collection
"""Whenever an object has not used or not alloctaed garbage collection program
it will kill memory.
==> garbage collection is automatic in python no need manullay"""
x=10
y=20
print(y)
import gc
print(gc.isenabled())
gc.enable()#disable state to  enable state
gc.disable()#enable state to disable state