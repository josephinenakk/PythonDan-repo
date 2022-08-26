#1. for loop :A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). 
#2. while loop

########### 1.a Looping Through a String: 
s= "cat"
print("s= ",s)
for x in s:
    print(x)
"""
ANSWER:
s=  cat
c
a
t"""
########## 1.b getting element by index
print("\nline 16- for loop ,getting element by index : \n")
s="forloop"
print("s= ",s)
for x in s[0:3]:
    print(x)
"""
ANSWER:
line 16- for loop ,getting element by index :
s = forloop
f
o
r
"""
############ 1.c for loop ,string , break
print("\nline 30- for loop ,string , break : ")
s="forloop"
print("s= ",s)
for x in s:
    if x == "o":
        break
    print(x)
"""
ANSWER:
line 30- for loop ,string , break :
s=  forloop
f
"""
############ 1.d for loop ,string , continue
print("\nline 44- for loop ,string , continue : ")
s="forloop"
print("s= ",s)
for x in s:
    if x == "o":
        continue
    print(x)
"""
ANSWER:
line 44- for loop ,string , continue :
s=  forloop
f
r
l
p
"""
############# 1.e for loop ,string , pass
print("\nline 61- for loop ,string , pass : ")
s="forloop"
print("s= ",s)
for x in s:
    pass
print(None)
"""
ANSWER:
line 61- for loop ,string , pass :
s=  forloop
None
"""
############# 1.f Else in For Loop
print("\nline 74- using continue string")
for letter in 'Python':
    pass   
else:
    print ('Current Letter :', letter)
"""
ANSWER:
line 74- using continue string
Current Letter : n
"""
############# 1.f if,Else,break in For Loop
print("\nline 85- using else and break ")
for x in 'Python':
    if x =="t": break
    print(x)
else:
  print("Finally finished!")
    
"""
ANSWER:
line 85- using else and break
P
y
"""
############## 2.a for loop on list
list1 = ["car","color","model","brand"]
print("\nline 100- for loop on list = ")
for x in list1:
    print(x)
"""
ANSWER:
line 100- for loop on list :
car
color
model
brand
"""
############# 2.b getting list element by index
print('\nline 112- getting list element by index at 0 : ')
list1 = ["car","color","model","brand"]
for x in list1[0:3]:
    print(x)
"""
ANSWER:
line 112- getting list element by index at 0 :
car
color
model
"""
############# 2.c getting list element by index
print('\nline 124- getting list element by index at 0 : ')
list1 = ["car","color","model","brand"]
for x in list1[0]:
    print(x)
"""
ANSWER:
line 124- getting list element by and iterating:
c
a
r
"""
############# 2.d List Using break
print('\n line 136- List Using break')   
list1 = ["car","color","model","brand"]
for x in list1:
    print(x)
    if x == "color":
        break
"""
ANSWER:
line 136- List Using break
car
color
"""
############# 2.e List Using continue
print("\nline 149- List using continue")
list1 = ["car","color","model","brand"]
for x in list1:
    if x == "color":
        continue
    print(x)
"""
ANSWER:
line 149- List using continue
car
model
brand
"""
"""
ANSWER:
"""
#2.f Nested Loops :A nested loop is a loop inside a loop.
print("\nline 166-Nested Loops :")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
"""
ANSWER:
line 166-Nested Loops :
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""
#3.a.range ( only end point, default staing point is 0)
print("\nline 186- range example without starting point and step :")
for x in range(5):
    print(x)
#range(5) is not the values of 0 to 5, but the values 0 to 4.
"""
ANSWER:
line 186- range example without starting point and step :
0
1
2
3
4
"""
#3.b.range with stating point and end point
print("\nline 200- range example with starting point and no step :")
for x in range(5,10):
    print(x)
"""
ANSWER:
line 200- range example with starting point and no step :
5
6
7
8
9
"""
#3.c range with stating point and end point and step
print("\nline 213- range example with starting point and step :")
for x in range(5,10,3):
    print(x)
"""
ANSWER:
line 213- range example with starting point and step :
5
8
"""
#3.d printing in list form
print("\nline 223- ", list(range(2,8)))
"""
ANSWER:
line 223-  [2, 3, 4, 5, 6, 7]
"""

#3.fother examples 
print("\nline 230- ")
for i in range(3):
    print("welcom")
"""
ANSWER:
line 230-
welcom
welcom
welcom
"""
#3.h other examples 
print("\nline 230- ")  
for _ in range(3):
    print("welcom")
"""
ANSWER:
line 230-
welcom
welcom
welcom
"""
# 4. dictionary:
#4.a 
print("line 253- dict for:")
a={"Joe","fine","G","C","A"}
for i in a:
    print(i) # cant give in order
"""
ANSWER:
line 253- dict for:
G
A
fine
Joe
C
"""
#4.b getting keys
print("\nline 267:\n********************")
a1={"Joe":1,"fine":2,"G":3,"C":4,"A":4}
for i in a1:
    print(i)
    #print(a1.keys())
    #print(a1[i])
    # print(a1.get(i))#gives you keys
"""
ANSWER:
line 267:
********************
Joe
fine
G
C
A
"""
#4.c getting keys in list form
print("\nline 285:\n********************")
a1={"Joe":1,"fine":2,"G":3,"C":4,"A":4}
for i in a1:
    print(a1.keys())
"""
ANSWER:
line 285:
********************
dict_keys(['Joe', 'fine', 'G', 'C', 'A'])
dict_keys(['Joe', 'fine', 'G', 'C', 'A'])
dict_keys(['Joe', 'fine', 'G', 'C', 'A'])
dict_keys(['Joe', 'fine', 'G', 'C', 'A'])
dict_keys(['Joe', 'fine', 'G', 'C', 'A'])
"""
#4.d getting values
print("\nline 300 :\n********************")
a1={"Joe":1,"fine":2,"G":3,"C":4,"A":4}
for i in a1:
    print(a1[i])
"""
ANSWER:
line 300:
********************
1
2
3
4
4
"""
##4.d getting values using get method
print("\nline 315 :\n********************")
a1={"Joe":1,"fine":2,"G":3,"C":4,"A":4}
for i in a1:
    print(a1.get(i))
"""
ANSWER:
line 315 :
********************
1
2
3
4
4
"""
#4.c toget keys and values
print("\nline 330:\n********************")
a1={"Joe":1,"fine":2,"G":3,"C":4,"A":4}
for keys1,values1 in a1.items():
    print(keys1,"----",values1)
"""
ANSWER:
line 330:
********************
Joe ---- 1
fine ---- 2
G ---- 3
C ---- 4
A ---- 4
"""
#4.d 
print("\nline 345:\n********************")
a1={"Joe":1,"fine":2,"G":3,"C":4,"A":4}
for dict_item in a1.items():
    print(dict_item)
"""
ANSWER:
line 345:
********************
('Joe', 1)
('fine', 2)
('G', 3)
('C', 4)
('A', 4)
"""