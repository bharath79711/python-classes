"""
operation  ==>mode
read        ==> r
write       ==> w
append      ==> a
read and write  ==>r+
write and read ==>w+
append and read  ==>a+

write     x
w       -> already won't create new file error ,file create
"""
# def function_read(file):
#     try:
#         data_obj = open(file,"r")
#         # print(data.name)#file name
#         # print(data.mode)# mode
#         data = data_obj.read()
#         return data
#
#     except Exception as error:
#         print("error is:",error)
#
#     finally:
#         data_obj.close()
#
# f_data = function_read("file.txt")
# print(f_data)
# without with
"""
# file_obj = open("file.txt","r")
# read operation
# print(file_obj.read())
# print(file_obj.readlines())# list
# print(file_obj.readline())#fist line
"""
# with
# read with
"""
with open("file.txt","r") as file_obj:
    print(file_obj.read())
    # read operation
    # print(file_obj.read())
    # print(file_obj.readlines())# list
    # print(file_obj.readline())#fist line
"""
# write
"""
with open("govindha.txt","w") as fileop:
    # fileop.write("hey hei i am fine \n how are you")
    fileop.writelines("hello what up \n dsf hgg hkdsgf ")
    print("i have created file")
"""
# append
"""
with open("govindha.txt","a") as fileop:
    # fileop.write("hey hei i am fine \n how are you")
    fileop.writelines("\n hello i am fine \n what are you doing ")
    print("i have created file")
"""
# read plus write
"""
with open("govindha.txt","r+") as fileop:
    fileop.write("\n hei anu \n  how are you")
    data = fileop.read()
    print(data)
    print("i have read file")
"""
#seek
"""
with open("govindha.txt","r") as fp:
    fp.seek(5)# it will go sp index
    print(fp.read())
"""

#map ,filter
#map(function,sequence)
"""data = map((lambda x:x**2),(1,2,3,4,5))
print(data)
print(list(data))"""

#filter
# filter(func,sequence)
data = filter((lambda x:x%2==0),(1,2,3,4,5))
print(data)
print(tuple(data))
