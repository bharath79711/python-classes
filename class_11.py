'''
student={"name":"Bharath",
         "age":28,
         "marks":85}
print(student)
print(student.get("name"))
print(student["age"])
student["course"]="python"
print(student)
student["gmail"]="bharathkumartalari70@gmail.com"
student["age"]=29
print(student)
del student["marks"]
print(student)
student.pop("name")
print(student)
student.popitem()
print(student)
'''
'''
x ={"name":"Bharath",
    "age":28,
    "village":"chintakunta"}
x["phone"]=9010297520
#print(x)
'''
'''
x["age"]=29
print(x)
#del x["village"]
#print(x)
x.pop("village")
print(x)
x.popitem()
print(x)
'''
'''
print(x.keys())
print(x.values())
print(x.items())
'''
'''
students={
    "Anu":80,
    "Madhu":65,
    "Bharath":90,
    "Tiru":55}
for name,marks in students.items():
    if marks>70:
        print(name)

'''
'''
student={"Ravi":80,
         "Bharath":60,
         "Anu":50,
         "Tiru":45,
         "Ashok":75}
for name ,marks in student.items():
    if marks<60:
        print(f"{name}:{marks}")
'''
'''
student={"name":"Bharath","age":28}
for key in student:
    print(f"{key}:{student[key]}")
'''
'''
student={"name":"Bharath","age":28,"course":"python"}
for key,value in student.items():
    print(f"{key}:{value}")
'''
'''
student={"name":"Bharath",
         "maths":90,
         "science":85,
         "English":88}
total=0
for value in student.values():
    if type(value)==int:
      total=total+value
print("Bharath total marks:",total)
'''
'''
students={
    "Bharath":{"maths":80,"science":70},
    "Tiru":{"maths":85,"science":90},
    "Anu":{"maths":60,"science":75},
    }
for name,subjects in students.items():
    total=0
    count=0
    for subject, marks in subjects.items():
        total=total+marks
        count=count+1
    average=total/count
    print(f"{name}:average={average}")
'''
'''
student={
    "name":"Bharath",
    "marks":{"maths":85,"science":90}
    }
#print(student["name"])
print(student["name"],student["marks"]["science"])
'''
students = {
    "Anu": {"math": 60, "sciene": 75},
    "bharath": {"math": 80, "sciene": 70}
}
for name, subjects in students.items():
    print(f"{name} math:{subjects['math']}")




































































