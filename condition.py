"""
a=1
b=1
if(b>a): 
    print("b is grater")
else:
    print("a is grater")
if(a == b):
   print("a equal to b") 

a=1
b=1
if(a>b):
    print("a>b")
elif(a<b):
    print("a<b")
elif(a==b):
    print("a==b")
else:
    pass
"""
dir={"first_name":"ra","last_name":"K"}
x = dir.values("ra")
print(x)
y = "first_name"
z = "age"
if(y in x or z not in x):
    dir.update({"first_name":"joe"},{"age": 25})
    print(dir)
elif(y not in x):
    dir.update({"last_name":"l"})
    print(dir)
elif(z not in x):
    dir.update({"age": 25})
    print(dir)
else:
    pass



