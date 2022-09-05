#The while Loop
#while loop we can execute a set of statements as long as a condition is true.

#1. while loop
print("\nline 5- list1 : ")
i=0
list1 = ["car","color","model","brand"]
while i<4:
    print("\t",i+1,list1[i])
    i+= 1

#2. while loop with if and break.
print("\nline 13- list2 : ")
e=0
x=[]
list2= ["car","color","model","brand","car","color","model","brand"]
while e<7:
    if e == 3:
        break
    x.append(list2[e])
    e+=1
print("\t",x)

#3.while loop iterating and adding each value to empty string.
print("\nline 23-")
i=0
y=""
st1="focus"
while i<5:
    x=st1[i]
    #print(x)
    y=y+x
    i+= 1
print("\t",y)

"""
Answer:

line 5- list1 :
         1 car
         2 color
         3 model
         4 brand

line 13- list2 :
         ['car', 'color', 'model']

line 23-
         focus
"""   