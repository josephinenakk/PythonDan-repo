#######    Python Dictionary Methods     #########
print("Python Dictionary Methods ******************************************")
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
print("\n line 27- printing dictinary_var= \n", dictinary_var)

#1.copy()
x=dictinary_var.copy()
print("\n line 31- 1.Using copy method to print dictinary_var= \n",x)

#2.fromkeys() for each first list item  it will take it as key and  assign all list items of second as value .
x=('first_name', 'age', 'height', 'weight')
y=('joe')
OneWayFoCreateDictonary = dict.fromkeys(x, y)
print("\n line 37- 2.Using formkey creating Dictonary= \n",OneWayFoCreateDictonary)

"""2.Using formkey creating Dictonary=
 {'first_name': 'joe', 
'age': 'joe', 
'height': 'joe',
'weight':'joe'}"""

#3.get()	
y=dictinary_var.get("marital_status")
print("\n line 47- 3.Using get method finding the value of marital_status= \n ",y)

#4.items()
z = dictinary_var.items()
print("\n line 51- 4.Using items method: \n",z)

#5.keys()	
k = dictinary_var.keys()
print("\n line 55- 5.Using keys method to get keys of dictinary= \n",k)

#6.pop()
x=dictinary_var.pop("pets")
print(x)
print("\n line 60- 6.Using pop method removing pets: \n",dictinary_var)

#7.popitem()
dictinary_var.popitem()
print("\n line 64- 7.Using pop method removing pets= \n ",dictinary_var)

#8.setdefault() , it doesn't change the value of key but if key does't exit it appends the key value.
x=dictinary_var.setdefault("first_name","Ammulu")
print("\n line 68- 8.1 From setdefault method with old key 'first_name'= \n",x) 
x=dictinary_var.setdefault("nick_name","Ammulu")
print("\n line 70- 8.2 From setdefault method with new key 'nick_name'= \n ",x)
print( dictinary_var)

#9.update()
dictinary_var.update({"color":"Green"})
print("\n line 75- 9 From update method= \n", dictinary_var)

#10.values()
z=dictinary_var.values()
print("\n line 79- 10. from values method printing all values= \n",z,"\n")