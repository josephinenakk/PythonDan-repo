#######    Python Dictionary Methods     #########
print("Python Dictionary Methods ******************************************")
"""
     Method: Description
1.	copy():	Returns a copy of the dictionary.
2.	fromkeys(): Returns a dictionary with the specified keys and value.
3.	get(): Returns the value of the specified key.
4.	items(): Returns a list containing a tuple for each key value pair.
5.	keys(): Returns a list containing the dictionary's keys.
6.	pop(): Removes the element with the specified key.
7.	popitem(): Removes the last inserted key-value pair.
8.	setdefault(): Returns the value of the specified key. If the key does not exist: insert the key, with the specified value.     
9.	update(): Updates the dictionary with the specified key-value pairs.
10.	values(): Returns a list of all the values in the dictionary.
11.	clear()	: Removes all the elements from the dictionary.
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

#1.copy() Returns a copy of the dictionary.
x=dictinary_var.copy()
print("\n line 31- 1.Using copy method to print dictinary_var= \n",x)
"""
ANSWER:
{'first_name': 'joe', 'age': 46, 'height': 134, 'weight': 67, 'marital_status': True, 'pets': 'two', 'no_of_childern': 2}
"""
#2.fromkeys() for each first list item  it will take it as key and  assign all list items of second as value .
x=('first_name', 'age', 'height', 'weight')
y=('joe')
OneWayFoCreateDictonary = dict.fromkeys(x, y)
print("\n line 40- 2.Using formkey creating Dictonary= \n",OneWayFoCreateDictonary)
""" 
ANSWER:
 {'first_name': 'joe', 'age': 'joe', 'height': 'joe', 'weight': 'joe'}
 """
#3.get()	Returns the value of the specified key.
y=dictinary_var.get("marital_status")
print("\n line 47- 3.Using get method finding the value of marital_status= \n ",y)
"""
ANSWER:
True
"""
#4.items() Returns a list containing a tuple for each key value pair.
z = dictinary_var.items()
print("\n line 54- 4.Using items method: \n",z)
"""
ANSWER:
dict_items([('first_name', 'joe'), ('age', 46), ('height', 134), ('weight', 67), ('marital_status', True), ('pets', 'two'), ('no_of_childern', 2)])
"""
#5.keys()	Returns a list containing the dictionary's keys.
k = dictinary_var.keys()
print("\n line 61- 5.Using keys method to get keys of dictinary= \n",k)
"""
ANSWER:
dict_keys(['first_name', 'age', 'height', 'weight', 'marital_status', 'pets', 'no_of_childern'])
"""
#6.pop() Removes the element with the specified key.
x=dictinary_var.pop("pets")
print("\n pop key= ",x)
print("line 69- 6.Using pop method removing pets: \n",dictinary_var)
"""
ANSWER:
pop key=  two
 {'first_name': 'joe', 'age': 46, 'height': 134, 'weight': 67, 'marital_status': True, 'no_of_childern': 2}
"""

#7.popitem() Removes the last inserted key-value pair.
dictinary_var.popitem()
print("\n line 78- 7.Using popitem thats pop last item = \n ",dictinary_var)
"""
ANSWER:
  {'first_name': 'joe', 'age': 46, 'height': 134, 'weight': 67, 'marital_status': True}
  """

#8.setdefault() , it doesn't change the value of key but if key does't exit it appends the key value.
x=dictinary_var.setdefault("first_name","Ammulu")
print("\nline 86- 8.1 From setdefault method with old key doesn't change the value of key 'first_name' = ",x) 
print( dictinary_var)
x=dictinary_var.setdefault("nick_name","Ammulu")
print("\nline 89- 8.2 From setdefault method with new key ,if key does't exit it appends the key value.'nick_name' =  ",x)
print( dictinary_var)
"""
ANSWER:
key exitn in dictionary it doesn't change the value of key  "first_name" =  joe
{'first_name': 'joe', 'age': 46, 'height': 134, 'weight': 67, 'marital_status': True}

if the key does't exit in dictionary them it appends the key value.'nick_name' =   Ammulu
{'first_name': 'joe', 'age': 46, 'height': 134, 'weight': 67, 'marital_status': True, 'nick_name': 'Ammulu'}
"""
#9.update() Updates the dictionary with the specified key-value pairs.
dictinary_var.update({"color":"Green"})
print("\n line 101- 9. From update method= \n", dictinary_var)
"""
ANSWER:
 {'first_name': 'joe', 'age': 46, 'height': 134, 'weight': 67, 'marital_status': True, 'nick_name': 'Ammulu', 'color': 'Green'}
 """
#10.values()  Returns a list of all the values in the dictionary.
z=dictinary_var.values()
print("\n line 108- 10. from values method printing all values= \n",z,"\n")
"""
ANSWER:
 dict_values(['joe', 46, 134, 67, True, 'Ammulu', 'Green'])
 """