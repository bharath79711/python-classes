#list comprehension
x=[1,2,3,4,5]
#first syntax
#[expression loop condition]
#ex1
y=[i**2 for i in x]#exp loop
print(y)
#ex2 even square
z=[i**2 for i in x if i%2!=0]
#exp loop cond
print(z)
yu=[i**2 if i%2==0 else 1 for i in x]
print(yu)

'''
x=[1,2,3,4,5]
y=[i**2 for i in x]
print(y)
z=[i**2 for i in x if i%2==0]
print(z)
yy=[i**2 if i%2==0 else i+1 for i in x ]
print(yy)

x=[1,2,3,4,5]
y=[i*10 for i in x]
print(y)

words=["python","jAVa","c"]
upper_words = [word.upper() if word.islower()else 0 for word in words ]
print(upper_words)
'''

'''
words =["apple","banana","kiwi"]
lengths=[len(word)for word in words]
print(lengths)
'''
'''
word = "pythonai"
vowels=[ch for ch in word if ch in "aeiou"]
print(vowels)
'''
'''
x=[1,2,3,4,5]
y=[i**2 for i in x if i%2!=0]
print(y)
'''
'''
x= [1,2,3,4,5,15,30,45]
result = [i for i in x if i%3==0 and i%5==0]
print(result)
'''
'''
words = ["python","java","telugu"]
revered_words = [word[::-1]for word in words]
print(revered_words)
'''
'''
nested=[[1,2],[3,4],[5]]
flat =[items for sublist in nested for items in sublist]
print(flat)
'''
'''
x =[1,2,3,4,5,6]
y=["even"if i%2==0 else "odd" for i in x]
print(y)

'''
'''
char =['a','b','c','A','B','C']
ASCII_value =[ord(ch)for ch in char]
print(ASCII_value)
'''
'''
x= [65,66,67,68,97,98,99,100]
y=[chr(i)for i in x]
print(y)
'''
'''
number =[int(f"{i}{j}")for i in range(1,4) for j in range (1,4)]
print(number)
'''

'''
sentence = "hello world"
no_vowels =''.join( [ ch for ch in sentence if ch not in "aeiou"])
print(no_vowels)
'''
'''
x=[5,11,13,4,10,15]
y=[i**2 for i in x if i%2!=0 and i>10]
print(y)
'''
'''
x= [1,2,3,4,5]
y=[]
for i in x:
    y.append(i**2)
    print(y)
 '''
'''
x= [1,2,3,4,5,6]
y=[]
for i in x:
    if i%2!=0 and i>1:
        y.append(i)
        print(y)
'''
'''
x=[1,3,2,4,2,3,56,87,9,2,1,1,5,2,1,7,2]
count =0
for i in x:
    if i==2:
        count=count+1
        print("2 appeared:",count, "times")
'''

























