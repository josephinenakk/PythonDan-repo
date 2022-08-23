#  Python List or Array Methods.
"""
Method: Description
1.append(): Adds an element at the end of the list.
2.copy(): Returns a copy of the list.
3.count(): Returns the number of elements with the specified value.
4.extend(): Add the elements of a list (or any iterable), to the end of the current list.
5.index(): Returns the index of the first element with the specified value.
6.insert(): Adds an element at the specified position.
7.pop(): Removes the element at the specified position.
8.remove(): Removes the first item with the specified value.
9.reverse(): Reverses the order of the list.
10.sort(): Sorts the list.
11.clear(): Removes all the elements from the list.
"""
list_example = [ "New York", "Los Angles", "Boston", "Denver","Alabama","colorado" ,"New York"]
# 1.append():Adds an element at the end of the list
list_example.append("Florida")
print('\n line 18- 1. Append-Adds an element at the end of the list ("Florida")=\n' ,list_example )
"""
ANSWER:
 line 18- Append-Adds an element at the end of the list ("Florida")=
 ['New York', 'Los Angles', 'Boston', 'Denver', 'Alabama', 'colorado', 'New York', 'Florida']
"""
# 2.copy():Returns a copy of the list
x=list_example.copy()
print("\n line 27- 2. Returns a copy of the list =\n",x)
"""
ANSWER:
line 27- 2. Returns a copy of the list =
 ['New York', 'Los Angles', 'Boston', 'Denver', 'Alabama', 'colorado', 'New York', 'Florida']
"""

# 3.count():Returns the number of elements with the specified value.
y=list_example.count("Boston")
z=list_example.count("New York")
print('\n list_exampl = ',list_example)
print(' line 38- 3.count  "Boston" in list_example = ', y)
z=list_example.count("New York")
print(' line 40- 3.count "New York" in list_example = ', z)
"""
ANSWER:
 list_exampl =  ['New York', 'Los Angles', 'Boston', 'Denver', 'Alabama', 'colorado', 'New York', 'Florida']
 line 38- 3.count  "Boston" in list_example =  1
 line 40- 3.count "New York" in list_example =  2
 """
# 4.extend(): Add the elements of a list (or any iterable), to the end of the current list (append added only one element at end)
list_example.extend(["Georgia","Hawaii"])
print("\n line 49- 4.extend Add the elements of a list to the end of the current list =\n",list_example)
"""
ANSWER
line 49- 4.extend Add the elements of a list to the end of the current list =
['New York', 'Los Angles', 'Boston', 'Denver', 'Alabama', 'colorado', 'New York', 'Florida', 'Georgia', 'Hawaii']
"""
#5.index():Returns the index of the first element with the specified value.
i =list_example.index("Georgia")
print('\n ',list_example)
print(' line 56- 5.index Returns the index of the first element with the specified value"Georgia" =',i)
"""
ANSWER
['New York', 'Los Angles', 'Boston', 'Denver', 'Alabama', 'colorado', 'New York', 'Florida', 'Georgia', 'Hawaii']
 line 56- 5.index Returns the index of the first element with the specified value"Georgia" = 8
 """
#6.insert(): Adds an element at the specified position.
"""Syntax: list.insert(pos, elmnt)
Parameter:
pos-(Required) A number specifying in which position to insert the value
elmnt-(Required) An element of any type (string, number, object etc.)
"""
print(list_example)
list_example.insert(0, "USA")
print('\n line 72- 6.insert Adds an element at the specified position(0, "USA")=\n', list_example)
"""
ANSWER:
line 71- 6.insert Adds an element at the specified position(0, "USA")=
['USA', 'New York', 'Los Angles', 'Boston', 'Denver', 'Alabama', 'colorado', 'New York', 'Florida', 'Georgia', 'Hawaii']
"""
#7.pop(): Removes the element at the specified position.
"""Syntax:list.pop(pos)
Parameter :
pos(Optional) ,A number specifying the position of the element you want to remove, default value is -1, which returns the last item
"""
print("\n",list_example)
list_example.pop(7)
print(' line 85- 7. poping "New York" at index 7 =\n', list_example)
"""
ANSWER:
['USA', 'New York', 'Los Angles', 'Boston', 'Denver', 'Alabama', 'colorado', 'New York', 'Florida', 'Georgia', 'Hawaii']
line 85- 7. poping "New York" at index 7 =
['USA', 'New York', 'Los Angles', 'Boston', 'Denver', 'Alabama', 'colorado', 'Florida', 'Georgia', 'Hawaii']
"""
#8.remove(): The remove() ,removes the first occurrence of the element with the specified value.
#Removes the  specified value, it finds  specified value according to index order , it removes first item that matches with sspecified value in the list.
"""Syntax : list.remove(elmnt)
Parameter :
elmnt(Required) Any type (string, number, list etc.) The element you want to remove.
"""
print('\n',list_example)
list_example.remove('Los Angles')
print('\n line 100- Removes the first item in the list  with the specified value "Los Angles"=\n',list_example)
"""
ANSWER:
 line 100- Removes the first item in the list  with the specified value "Los Angles"=
 ['USA', 'New York', 'Boston', 'Denver', 'Alabama', 'colorado', 'Florida', 'Georgia', 'Hawaii']
 """
#9.reverse(): Reverses the order of the list.
#Syntax: list.reverse()
print('\n',list_example)
list_example.reverse()
print('line 110- the reverse,reverses the sorting order of the elements=\n',list_example)

#10.sort(): Sorts the list.
#10.a.Sort the list alphabetically:
print('\n',list_example)
list_example.sort()
print(' line 110- 10.a Sort the list alphabetically=\n',list_example)
"""
ANSWER:
['Hawaii', 'Georgia', 'Florida', 'colorado', 'Alabama', 'Denver', 'Boston', 'New York', 'USA']
 line 11o- 0.a.Sort the list alphabetically=
 ['Alabama', 'Boston', 'Denver', 'Florida', 'Georgia', 'Hawaii', 'New York', 'USA', 'colorado']
"""
#10.b Sort the list descending:
# list.sort(reverse=True|False, key=myFunc)
'''
Parameter:
reverse	(Optional) reverse=True will sort the list descending. Default is reverse=False
key	(Optional) A function to specify the sorting criteria(s)
'''
print('\n',list_example)
list_example.sort(reverse=True)
print(' line 131- 10.b Sort the list with reverse=True option =\n',list_example)
"""
ANSWER:
 ['Alabama', 'Boston', 'Denver', 'Florida', 'Georgia', 'Hawaii', 'New York', 'USA', 'colorado']
 line 131- 10.b Sort the list with reverse=True option =
 ['colorado', 'USA', 'New York', 'Hawaii', 'Georgia', 'Florida', 'Denver', 'Boston', 'Alabama']
"""

#10.c Sort the list by the length of the values:
print('\n',list_example)
def myFunc(e):
  return len(e)
list_example.sort(key=myFunc)
print(' line 145- 10.c Sort the list by the length of the values =\n',list_example)
"""
ANSWER: 
['colorado', 'USA', 'New York', 'Hawaii', 'Georgia', 'Florida', 'Denver', 'Boston', 'Alabama']
 line 145- 10.c Sort the list by the length of the values =
 ['USA', 'Hawaii', 'Denver', 'Boston', 'Georgia', 'Florida', 'Alabama', 'colorado', 'New York']
 """

#10.d Sort a list of dictionaries based on the "year" value of the dictionaries:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
print('\n',cars)
cars.sort(key=myFunc)
print(' line 165- 10.dSort a list of dictionaries based on the "year" value of the dictionaries =\n',cars)
"""
ANSWER:
 [{'car': 'Ford', 'year': 2005}, {'car': 'Mitsubishi', 'year': 2000}, {'car': 'BMW', 'year': 2019}, {'car': 'VW', 'year': 2011}]
 line 165- 10.dSort a list of dictionaries based on the "year" value of the dictionaries =
 [{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]
"""
#10.e Sort the list by the length of the values and reversed:
print('\n',cars)
cars.sort(reverse=True, key=myFunc)
print(' line 175- Sort the list by the length of the values and reversed=\n',cars)
"""
ANSWER: 
[{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]
line 172- Sort the list by the length of the values and reversed=
[{'car': 'BMW', 'year': 2019}, {'car': 'VW', 'year': 2011}, {'car': 'Ford', 'year': 2005}, {'car': 'Mitsubishi', 'year': 2000}]
 """
#11.clear(): Removes all the elements from the list.


