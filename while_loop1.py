#1.  for loop adding each element to an empty string
print("1. for loop adding each element to an empty String")
s= "hello"
y=""
for i in s:
    y=y+i
    print("line 6- ",y)
print("line 7- out of for_loop : ",y)
print("\n")

#2. for loop adding each element to an empty list
print("2. for loop adding each element to an empty list")
list_example = [ "New York", "Los Angles", "Boston", "Denver","Alabama","colorado" ,"New York"]
y=[]
for l in list_example:
    y.append(l)
    print("line 16- inside of for_loop : ",y)
print("line 17- out of for_loop : ",y)
print("\n")

#3.while loop
# Iterate until x becomes 0
print("3.while loop Iterate until x becomes 0")
x = 6
while x:
    print(x)
    x -= 1

#4 Iterate until list is empty 
print("\n4.while loop Iterate until list is empty :")
List1 = ['red', 'green', 'blue']
print("List1: ",List1,"\n")
while List1:
    print("from List1 '",List1.pop(),"' is poped")
    
    print("then remaining List1 is : ",List1,"\n")
    
# 5.Prints blue green red

print("\n5.while loop Iterate until string is empty")
x = 'blue'
while x:
    print(x)
    x = x[1:]
    
# Prints blue
# Prints lue
# Prints ue
# Prints e

"""Break in while Loop
Python break statement is used to exit the loop immediately.
It simply jumps out of the loop altogether, and the program continues after the loop.
"""
#6.Break in while-Loop, string and descending order using -= operator
print("\n6.Break in while-Loop, string and descending order using -= operator")
y=""
x=9
while x:
    y=y+str(x)
    #print("line 52- y=",y)
    x -= 1
    if(x==3): 
        break
    #print("line 56- y=",y)
print("line 57- y=",y)

#7.Break in while_Loop, list descending order of loop using -= operator
print("\n7.Break in while_Loop, list descending order of loop using -= operator")
y=[]
x=9
while x:
    y.append(x)
    #print("line 52- y=",y)
    x -= 1
    if(x==3): 
        break   
    print("line 56- y=",y)
print("line 70- y=",y)

#8.Break in while_Loop, string ascending order of loop using += operator
print("\n8.Break in while_Loop, string ascending order of loop using += operator")
y=""
x=1
while x:
    y=y+str(x)
   # print("line 79- ",y)
    x += 1
    if(x==6):
        break
print("line 83- ",y)

#9.Break in while_Loop, list ascending order of loop using += operator
print("\n9.Break in while_Loop, list ascending order of loop using += operator")
y=[]
x=1
while x:
    #y.append(str(x))
    y.append(x)
    #print("line 78- ",y)
    x += 1
    if(x==6):
        break
print("line 78- ",y)

# 8.Skip odd numbers
print("\n8.Skip odd numbers")
y=[]
x=20
while x:
     x -=1
     if (x%2 ==0):
        y.append(x)   
print("line 104- ",y)
print("\n")

#9.Else in While Loop
print("9.Else in While Loop")
y=""
x=9
while x:
    y=y+str(x)
    x -= 1
    #print("line 52- y=",y)
else:
    print('Done!')
print("line 127- y=",y)
print("\n")