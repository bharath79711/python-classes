# String Manipulations
"""
name = "bangalore karnataka"
upper ==> lower string to upper ==> str.upper()
lower ==>capital to small ==>str.lower()
title ==> Starting letters capital ==>str.title()
isupper ==> str.isupper()
islower ==>str.islower()
split() ==>str.split()
join() ==>join_str.join(Squence)
replace() ==>str.replace(old_str,new_str)
capitalize() ==>str.capitalize()# starting letter converted to caps
startswith() ==>str.startswith(str_check)==>
endswith()==>str.endswith(str_check)
strip() ==>str.strip()==both left and right spaces will be removed
lstrip()==>str.lstrip()==>left space will removed
rstrip()==>str.rstrip()==>right space removed

"""

name = input("Enter the name:")  # REddy ==>str

if name.isupper():
    print("all are capital", name)
elif name.islower():
    print("all are small case:", name)
else:
    print("all are mixed case", name)
    print("COnverting to lower:", name.lower())  # reddy
    print("COnverting to upper:", name.upper())  # REDDY

