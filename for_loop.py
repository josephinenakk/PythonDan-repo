#for loop on string
from multiprocessing.sharedctypes import Value
from turtle import color


s="forloop"
for x in s:
    print(x)

#1. getting element by index
print("\nline 7- by index\n")
for x in s[0:3]:
    print(x)


#2. for loop on list
list1 = ["car","color","model","brand"]
print("\nline 14- list1 = ")
for x in list1:
    print(x)

print('\nline 18- list1 at 0')
for x in list1[0]:
    print(x)

print('\n line 22- Using break')   
for x in list1:
    print(x)
    if x == "color":
        break

print("\nline 28- using continue")
for x in list1:
    print(x)
    if x == "color":
        continue

print("\nline 34- using continue string")
for letter in 'Python':     
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

print("\nline 40- using continue and !=")
for letter in 'Python':     
   if letter != 'm':
      continue
   print ('Current Letter :', letter)

print("\nrange example :")
for x in range(5):
    print(x)

print("\nline 53- range with starting point,ending point and step")
for x in range(100,150,10):
    print(x)

print("\nline 50- ", list(range(2,8)))

print("\nFor and else example :")
colors1=[ "blue","green","red","cyan","magenta"]
for c in colors1:
    print(c)
else:
    print("\ngood")

print("\nline 59- Nested for")
colors1=[ "blue","green","red","cyan","magenta"]
list1 = ["car","color","model","brand"]
for x in list1:
    for y in colors1:
        print(x,y)

print("\nline 65- Access Index in for Loop")
colors1=[ "blue","green","red","cyan","magenta"]
for index,value in enumerate(colors1):
    print(index,value)

print ("\n list again: ")
colors1=[ "blue","green","red","cyan","magenta"]
for x in colors1:
    y=colors1.append(x)
print(y)


