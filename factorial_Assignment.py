a = """In a given range of numbers ,
 1. check the result is even and divisible by 10, 
 2. check the result is odd and divisible by 3,
 3. handle else saying none of the above conditions met """
print(a)
#list1=[]
#list2=[]
for x in range(0,100):
    if (x%2 == 0 and x%10 == 0):
        #list1.append(x)
        print(x)
    elif(x%2 != 0 and x%3 == 0):
        #list2.append(x)
       print(x)
    else:
     print("none of the above conditions met")
     #pass
#print(list1)
#print(list2)

print("\n")

##################################################################################

#2. printing above in a list
list1=[]
list2=[]
for x in range(0,100):
    if (x%2 == 0 and x%10 == 0):
        list1.append(x)
        #print(x)
    elif(x%2 != 0 and x%3 == 0):
        list2.append(x)
       #print(x)
    else:
     #print("none of the above conditions met")
     pass
print("\nline 35-",list1)
print("\nline 35-",list2)
print("\n")

##############################################################################################

#3. calculate factorial using for loop 

#a= int(input("enter a integer :"))
a=5
b = 1

for i in range(b,a+b):
        b *= i
print (b)

##############################################################################################

#4. calculate factorial using while loop 

#n=int(input("enter a integer :"))
n=5
num = 1
if(type(a)== int):
    while n >= 1:
        num = num * n
        n -=1
print(num)

##################################################################################33

#5.name with less than 5 characters is not allowed to add in the dictionary
details = {}
first_name = input("Please Enter a First Name : ")
last_name = input("Please Enter a Last Name : ")
while(len(first_name ) > 5 and len(last_name) > 5):
    details.update({"first_name ":first_name})
    details.update({"last_name ":last_name})
    first_name = input("Please Enter a First Name: ")
    last_name = input("Please Enter a Last Name: ")
print (details)