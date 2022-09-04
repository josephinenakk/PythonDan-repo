"""
Method:Description
1. add():Adds an element to the set
2. clear():Removes all the elements from the set
3. copy():Returns a copy of the set
4. difference():Returns a set containing the difference between two or more sets
5. difference_update():Removes the items in this set that are also included in another, specified set
6. discard():Remove the specified item
7. intersection():Returns a set, that is the intersection of two or more sets
8. intersection_update():Removes the items in this set that are not present in other, specified set(s)
9. isdisjoint():Returns whether two sets have a intersection or not
10. issubset():Returns whether another set contains this set or not
11. issuperset():Returns whether this set contains another set or not
12. pop():Removes an element from the set
13. remove():Removes the specified element
14. symmetric_difference():Returns a set with the symmetric differences of two sets
15. symmetric_difference_update():inserts the symmetric differences from this set and another
16. union():Return a set containing the union of sets
17. update():Update the set with another set, or any other iterable
"""
#1. add():Adds an element to the set
set1 = {"pineapple","apple", "banana", "cherry"}
set1.add("orange")
print(set1)         #{'apple', 'cherry', 'orange', 'pineapple', 'banana'}

#3. copy():Returns a copy of the set
cars = {"Honda", "Acura", "BMW"}
cars1 = cars.copy()
print(cars1)       #{'Acura', 'BMW', 'Honda'}

#4. difference():Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) 
print(z)           #{'cherry', 'banana'}#

#5. difference_update():Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) 
print(x)           #{'cherry', 'banana'}

#6. discard():Remove the specified item
y = {"google", "microsoft", "apple"}
y.discard("apple") 
print(y)           #{'google', 'microsoft'}

#8. intersection_update():Removes the items in this set that are not present in other, specified set(s)
#get the common elements in both sets and strore in first set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","cherry"}
x.intersection_update(y) 
print(x) #{'apple', 'cherry'}

#9. isdisjoint():Returns boolian value whether two sets have a intersection or not
#True:  both sets don't have common elements
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) 
print(z) #True

#10. issubset():Returns whether another set contains this set or not
#True: all element of set x is in set y
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) 
print(z)   #True

#11. issuperset():Returns whether this set contains another set or not
#True: all element of set y is in set x
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) 
print(z)    #True

#12. pop():Removes an element from the set
# it pop an random elements  each time you run pop it pops different element>
fruits = {"apple", "banana", "cherry"}
fruits.pop() 
print(fruits)  #{'cherry', 'banana'}

#13. remove():Removes the specified element
# removes a spacific element of set
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
print(fruits)          # {'apple', 'cherry'}

#14. symmetric_difference():Returns a set with the symmetric differences of two sets
# removes the commom elements and give you a combination of two sets elements
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","cherry"}
z = x.symmetric_difference(y) 
print(z)               # {'banana', 'microsoft', 'google'}

#15. symmetric_difference_update():inserts the symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","cherry"}
x.symmetric_difference_update(y) 
print(x)   #{'microsoft', 'google', 'banana'}

#16. union():Return a set containing the union of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y) 
print(z) #{'cherry', 'banana', 'google', 'apple', 'microsoft'}

#17. update():Update the set with another set, or any other iterable
#diffent elements 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) 
print(x)

x = {"apple", "banana", "cherry"}
y = ["google", "microsoft", "apple"]
x.update(y) 
print(x) #{'cherry', 'apple', 'banana', 'google', 'microsoft'}

# discord dont trow error if element is not in set, but remove trow error if element is not set.