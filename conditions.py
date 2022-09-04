print("\n find which number is greater:")
a=1
b=1
if(b>a): 
    print("line 5 : b is greater")
else:
    print("line 7 : a is greater")

if(a == b):
   print("line 10 : a equal to b") 

print("\nfind which number is greater using if and elif:")

a=1
b=1
if(a>b):
    print("line 17 : a>b")
elif(a<b):
    print("line 19 : a<b")
elif(a==b):
    print("line 21 : a==b")
else:
    pass

print("\nupdate dictionary using if and elif")

dir={"first_name":"ra","last_name":"K"}
x = dir.values()
print("line 29 :",x)

y = "first_name"
z = "age"
if(y in x or z not in x):
    dir.update({"first_name":"joe"})
    print("\nline 35- (updated first_name with joe ) dir :\n", dir)
elif(y not in x):
    dir.update({"last_name":"l"})
    print("\nline 38-(updated with last_name with l)dir :\n ",dir)
elif(z not in x):
    dir.update({"age": 25})
    print("\nline 41-  (updated age with 25) dir :\n ",dir)
else:
    pass

print("\n")

