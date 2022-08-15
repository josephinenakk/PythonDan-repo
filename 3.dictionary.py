#######    Python Dictionary Methods     #########
"""
Method				Description
1.	copy()		Returns a copy of the dictionary.
2.	fromkeys()	Returns a dictionary with the specified keys and value.
3.	get()		Returns the value of the specified key.
4.	items()		Returns a list containing a tuple for each key value pair.
5.	keys()		Returns a list containing the dictionary's keys.
6.	pop()		Removes the element with the specified key.
7.	popitem()	Removes the last inserted key-value pair.
8.	setdefault()	Returns the value of the specified key. If the key does not exist: insert the key,     with the specified value.     
9.	update()	Updates the dictionary with the specified key-value pairs.
10.	values()		Returns a list of all the values in the dictionary.
11.	clear()		Removes all the elements from the dictionary.
"""


dictinary_var = {
                 "first_name":"joe",
                 "age":46,
                 "height":134,
                 "weight":67,
                 "marital_status":True,
                 "pets":"two",
                 "no_of_childern":2
                 }
print(dictinary_var,"\n")

#1.	copy()
x=dictinary_var.copy()
print("1.Using copy method to print dictinary_var",x,'\n')

#2.	fromkeys() for each first list item  it will take it as key and  assign all list items of second as value .
x=('first_name', 'age', 'height', 'weight')
y=('joe')
OneWayFoCreateDictonary = dict.fromkeys(x, y)
print("2.Using formkey creating Dictonary=",OneWayFoCreateDictonary)

"""2.Using formkey creating Dictonary=
 {'first_name': 'joe', 
'age': 'joe', 
'height': 'joe',
'weight':'joe'}"""

#3.	get()	
y=dictinary_var.get("marital_status")
print("3.Using get method finding the value of marital_status: ",y,'\n')

#4.	items()
z = dictinary_var.items()
print("4.Using items method: ",z,'\n')

#5.	keys()	
k = dictinary_var.keys()
print("5.Using keys method to get keys of dictinary:",k,'\n')

#6. pop()
x=dictinary_var.pop("pets")
print(x)
print("6.Using pop method removing pets: ",dictinary_var,'\n')

#7.	popitem()
dictinary_var.popitem()
print("7.Using pop method removing pets: ",dictinary_var,'\n')

#8.	setdefault() , it doesn't change the value of key but if key does't exit it appends the key value.
x=dictinary_var.setdefault("first_name","Ammulu")
print("8.1 From setdefault method with old key= ",x,'\n') 
x=dictinary_var.setdefault("nick_name","Ammulu")
print("8.2 From setdefault method with new key= ",x,'\n')

#9.	update()
dictinary_var.update({"color":"Green"})
print("9 From update method= ", dictinary_var,'\n')

#10.values()
z=dictinary_var.values()
print("10. from values method printing all values=",z)