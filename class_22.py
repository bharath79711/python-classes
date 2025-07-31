#polymorphism:-
''' method override and overloading
x=10
print("x is :",x)
x=20
print("x is :",x)'''
import multiprocessing

'''
class Employee:
    def display(self):
       return ("Hello world")
class college(Employee):
    def display(self):
        return ("Hello world! Good morning")

cc=college()
print(cc.display())
'''
#global variables or scope and local variables or scope #name spaces
Ex:1

'''
x=10
def fun(y):
    return x*y

data=fun(10)
print(data)
'''
Ex:2
'''
x=10
def fun(y):
    x=20
    return x*y

data=fun(10)
print(data)
'''
Ex:3
'''
x=10
def fun(y):
    global x
    x=20
    return x*y

data=fun(10)
print(data)
print(x+10)
'''
#Multi Threading and Multi processing :-
#    Multiple functions we can execute parllel
'''

import threading
import time
import multiprocessing


def func_sum(x,y):
 time.sleep(3)

 print(f"sum is :{x+y}")
def func_sub(x,y):
     time.sleep(3)
     print(f"sub is: {y-x}")

def func_div(x,y):
    time.sleep(3)
    print(f"div is: {y/x}")

    
t1=threading.Thread(target=func_sum,args=(10,20))
t2=threading.Thread(target=func_sub,args=(10,20))
t3=threading.Thread(target=func_div,args=(10,20))
t1.start()
t1.join()

t2.start()
t2.join()

t3.start()
t3.join()

# syntax of multi processing same as multi threading 
t1=multiprocessing.Process(target=func_sum,args=(10,20))
t2=multiprocessing.Process(target=func_sub,args=(10,20))
t3=multiprocessing.Process(target=func_div,args=(10,20))
t1.start()
t2.start()
t3.start()
t3.join()
t1.join()
t2.join()

'''
#datetime
import datetime as dt
import calendar as c

print(dt.datetime.today())
c_no=dt.datetime.today().weekday()
print(c.day_name[c_no])
print(dt.datetime.now().date())
print(dt.datetime.now().time())
print(dt.datetime.now().year)
print(dt.datetime.now().month)
print(dt.datetime.now().day)
print(dt.datetime.now().hour)
print(dt.datetime.now().minute)
print(dt.datetime.now().second)
print(dt.datetime.now().strftime("%H:%M:%S"))
print(dt.datetime.now().strftime("%I:%M:%S"))

print(dt.datetime.now().strftime("%Y-%m-%d"))
print(dt.datetime.now().strftime("%A"))
print(dt.datetime.now().strftime("%a"))
print(dt.datetime.now().strftime("%B"))
print(dt.datetime.now().strftime("%b"))
print(dt.datetime.now().strftime("%C"))
print(dt.datetime.now().strftime("%Y"))