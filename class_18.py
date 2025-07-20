import re

# match:-
# search
# findall
# sub
x = "bharath hgf dshgf sdhf sfhsjfj.;lsak dsadsfd bharath lsd d;bharath sdkfjdsh kdgh kgh ds"
# match ==>re.match(pattern,str) ==
"""
# starting of the string
data = re.match("bharath",x)
print(data)
print(data.group())
"""

# search ==>re.search(pattern,str)
# when the pattern match in the entire string it will return one
"""
data = re.search("bharath",x)
print(data)
print(data.group())
"""

# findall ==>re.findall(pattern,str)
# matches the pattern it will return all
"""
data = re.findall("bharath",x)
print(data)
# print(data.group())
"""
"""
#sub whenever pattern matches it will replace substring
#re.sub(pattern,repl,str)
data = re.sub("bharath","anu",x)
print(data)
"""

"""
\d ==>it will match numbers
[a-zA-Z] ==>it will uses to match small and capital cases
/w ==> it will match both numbers and letters
/s ==> it will match the psaces
. ==> it will return single 
^ ==>starting oth string 
$ ==>string last lo pattern
{} ==> {1,}
* ==>0 or more than 1
+ ==> more than 1 match
"""
"""
y = "reddy vari palli cvapb4576m 133a1a0326 12345 10f65a0306 19w55a0406 thi122rumala@gmail.com anu@outlook.com bha@gmail.com madanapalli 517351 560036 517325 838535965466 940244665036 dbzpm3688h"

data = re.findall("[a-zA-Z]{5}\d{4}[a-zA-Z]",y)
data_mails = re.findall("\w{1,}@[a-zA-Z]{1,}.com",y)
print(data)
print(data_mails)
data_rolls = re.findall("\d{1,4}[a-zA-Z]\d{1,2}[a-zA-Z]\d{4}",y)
print(data_rolls)
"""
def func_read(file):
    with open(file, "r") as fp:
        y = fp.read()
        data = re.findall("[a-zA-Z]{5}\d{4}[a-zA-Z]",y)
        data_mails = re.findall("\w{1,}@[a-zA-Z]{1,}.com",y)
        data_rolls = re.findall("\d{1,4}[a-zA-Z]\d{1,2}[a-zA-Z]\d{4}",y)
        return data,data_rolls,data_mails

data,data_rolls,data_mails = func_read("file.txt")

print(data,data_rolls,data_mails)

import re

x="""
  chintakunta village cvapb4576m 133a1a0326 12345 10f65a0306 19w55a0406
   thiru122mala@gmail.com anu@outlook.com bharath70@gmail.com kadapa
   516172 516175 517351  838535965466 940244665036

"""
data_mails=re.findall("\w{1,}@[a-zA-z]{1,}.com",x)

print(data_mails)


data_rolls = re.findall("\d{1,}[a-zA-Z]\d{1,}[a-zA-Z]\d{4}",x)
print(data_rolls)

data_adhar_no = re.findall("\d{12}",x)
print(data_adhar_no)


import re
"""
x="India is my Country . Bharath lives in Banglore with Tiru and Anu"

data=re.findall("[A-Z][a-zA-Z]{1,}",x)
print(data)
"""
"""
x="Today's date is 13-07-2025. My DOB is 02-11-1996 in valid:1-1-1999"

data= re.findall("\d{2}-\d{2}-\d{4}",x)
print(data)
"""
"""
x="I am learning python and enjoying building and debbuing programs"

data = re.findall("[a-zA-Z]{1,}ing",x)
print(data)
data1= re.findall("\w{1,}ing",x)
print(data1)
"""
"""

x="python is easy. pycharm is IDE.I like pygame and pyinstaller."

data=re.findall("py\w{1,}",x)
print(data)

x= "cvapb4576m  133a1a0326  10f65a0306 abcd xyz abc123"

data=re.findall("\w{1,}\d{1,}\w",x)


print(data)
"""
"""
x = "Bharath and Anu went to Delhi with Ravi and Tiru."
y= re.sub("[A-Z]{1}[a-z]{1,}","NAME",x)
print(y)

res =re.findall("[A-Z][a-z]{1,}", x)
print(res)

"""
"""
x= "This is is  is good good good exaple.But not  not not not always"
data=re.findall(r"(\w{1,})\s{1,}\w{1,}\s{1,}\1",x)
print(data)
"""
"""
x= "products:₹250,₹199.99,$5.50,$100 and ₹50"
data=re.findall("[₹|$]\d[.\d]*",x)
print(data)
"""
"""
x= "valid: 01-01-2025, 31-12-1999.  In valid: 32-01-2023 00-13-2000"
data=re.findall("\d{01,31}-\d{01,12}-\d{4}",x)
print(data)
"""

x= "passwords: Bharath123, Bharathkumar ,Kumar@,Talari@326.Anu4565,Tiru#123,Madhu!222,Anu!1212"
data=re.findall(r"\b(?=.*A-Z)(?=.*a-z){1,}[@#!$](?=.*\d){1,}[A-Za-z@#$!\d]{6,}\b",x)
print(data)