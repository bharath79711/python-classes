"""
Exceptional Handling or Error Handling(Solve)
- Whenever error raises the interpretor abnormally terminates script
    for handling the error we are going to execeptional handling

-------
M1:
---
try:
    - error possible area

except:
    - error handle area

M2
---
-->if you want to know what error you should go this
try:
    ---
except Exception as error:
    print("error found:",error)

M3:
---
- if you know exact error
try:
    ---
except TypeError:
    print("error got")

M4:
----
try:
    ----
except Exception:
    ----
finally:
    ----if error raise or error won't raise it will execute

M5:
----
try:
    ---
except:
    ---
else:
    - if error won't raise in try block it will execute otherwise it won't
M6:
---
    raise: we can explicitly error
    raise Exception("error description")
    raise SPError("error description")
"""

def func_div(x, y):
    try:
        data = x / y
        return data
    except ZeroDivisionError:
        print("hey check the divider value should greater than 0")


# data_div = func_div(10, 2)
# print(data_div)
# data_div_2 = func_div(10,0)
# print(data_div_2)
#=============================================
def func_div1(x, y):
    try:
        data = x / y
        return data
    except Exception as error:
        print("error is:", error)


# data_div = func_div(10, 2)
# print(data_div)
#
# data_div_2 = func_div(10, 0)
# print(data_div_2)
#============================================
def func_div3(x, y):
    try:
        data = x / y
        return data
    except:
        print("error i got in function please check values")


# data_div = func_div(10, 2)
# print(data_div)
#
# data_div_2 = func_div(10, 0)
# print(data_div_2)

#==============================================
def func_div4(x, y):
    try:
        data = x / y
        # return data
    except:
        print("error i got in function please check values")
    else:
        print("else block will execute error wont raise")
        return data

# data_div = func_div(10, 2)
# print(data_div)
#
# data_div_2 = func_div(10, 0)
# print(data_div_2)

#==========================================
def func_div5(x, y):
    try:
        data = x / y
        # return data
    except:
        print("error i got in function please check values")
    finally:
        print("i will execute your code any time")

# data_div = func_div(10, 2)
# print(data_div)
#
# data_div_2 = func_div(10, 0)
# print(data_div_2)

#=================================
def func_div6(x, y):
    try:
        data = x / y
        raise Exception ("Error found")
    except:
        print("error i got in function please check values")
    finally:
        print("i will execute your code any time")

# data_div = func_div(10, 2)
# print(data_div)

# data_div_2 = func_div(10,0)
# print(data_div_2)
#====================================
