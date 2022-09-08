#           Python Built in Functions

'''**************************************************************************************************'''
#1. abs():Returns the absolute value of a number
x = abs(-7.25)
print(x)            # 7.25
# Return the absolute value of a complex number:
x = abs(3+5j)
print(x)            # 5.830951894845301

'''**************************************************************************************************'''

#2. all():Returns True if all items in an iterable object are true ( not 0)

mylist = [True, True, True]
x = all(mylist)
print(x) # True

mylist = [0, 1, 1]
x = all(mylist)
print(x)
# Returns False because 0 is the same as False

mytuple = (0, True, False)
x = all(mytuple)
print(x)
# Returns False because both the first and the third items are False

myset = {0, 1, 0}
x = all(myset)
print(x)
# Returns False because both the first and the third items are False

mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)
print(x)
# Returns False because the first key is false.
# For dictionaries the all() function checks the keys, not the values.

'''**************************************************************************************************'''

#3. any():Returns True if any item in an iterable object is true

mylist = [False, True, False]
x = any(mylist)
print(x) #True

mytuple = (0, 1, False)
x = any(mytuple)
print(x)
# Returns True because the second item is True

myset = {0, 1, 0}
x = any(myset)
print(x)
# Returns True because the second item is True

mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)
print(x)
# Returns True because the second key is True.
# For dictionaries the any() function checks the keys, not the values.

'''**************************************************************************************************'''
#4. ascii():eturns a readable version of an object. Replaces none-ascii characters with escape character
x = ascii("My name is Ståle")
print(x)
#'My name is St\e5le'

'''**************************************************************************************************'''
#5. bin():Returns the binary version of a number
x = bin(36)
print(x) #0b100100
# The result will always have the prefix 0b

'''**************************************************************************************************'''
#6. bool():Returns the boolean value of the specified object
"""
The object will always return True, unless:
The object is empty, like [], (), {}
The object is False
The object is 0
The object is None
"""
x = bool(1)
print(x) #True

l=[]
x=bool(l)
print(x) #False

'''**************************************************************************************************'''
#7.bytearray():Returns an array of bytes

#7.1 Array of bytes from an iterable list
prime_numbers = [2, 3, 5, 7]
# convert list to bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)
# Output: bytearray(b'\x02\x03\x05\x07')

#7.2 Array of bytes of given integer size
i = 5
arr = bytearray(i)
print(arr)
#bytearray(b'\x00\x00\x00\x00\x00')

#7.3  Array of bytes from a string
string = "Python is interesting."
print(type(string))
# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)
print(type(arr))
"""
<class 'str'>
bytearray(b'Python is interesting.')
<class 'bytearray'>
"""
'''**************************************************************************************************'''
#8. bytes():Returns a bytes object
x = bytes(4)
print(x)
#b'\x00\x00\x00\x00'
# same as bytearray

'''**************************************************************************************************'''
#9.callable():Returns True if the specified object is callable, otherwise False.
#9.1 Check if a function is callable:
def x():
  a = 5
print(callable(x)) #True
#9.2 A normal variable is not callable:
x = 5
print(callable(x)) #False

'''**************************************************************************************************'''
#10. chr():Returns a character from the specified Unicode code.
x = chr(97)
print(x) #a

'''**************************************************************************************************'''
#11. compile():Returns the specified source as an object, ready to be executed.
#compile(source, filename, mode, flag, dont_inherit, optimize)
x = compile('print(55)', 'test', 'eval')
exec(x) #55

x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x) 
#55
#88

'''**************************************************************************************************'''
#12. complex()	Returns a complex number
#Convert the number 3 and imaginary number 5 into a complex number:
x = complex(3, 5)
print(x) #(3+5j)

#Convert a string into a complex number:
x = complex('3+5j')
print(x) #(3+5j)

'''**************************************************************************************************'''
#13. delattr():Deletes the specified attribute (property or method) from the specified object
class Person:
  name = "John"
  age = 36
  country = "Norway"
delattr(Person, 'age')
#print(Person.age)
print(Person.name)  #John
# The Person object will no longer contain an "age" property

'''**************************************************************************************************'''
#14. dict():Returns a dictionary (Array)
x = dict(name = "John", age = 36, country = "Norway")
print(x)
#{'name': 'John', 'age': 36, 'country': 'Norway'}

'''**************************************************************************************************'''
#15. dir():Returns a list of the specified object's properties and methods.
#Display the content of an object:
class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))

'''**************************************************************************************************'''
#16. divmod():Returns the quotient and the remainder when argument1 is divided by argument2
x = divmod(5, 2)
print(x) #remainder of 5 divided by 2= (2, 1)

'''**************************************************************************************************'''
#17. enumerate():Takes a collection (e.g. a tuple) and returns it as an enumerate object.

#enumerate(iterable, start)
#A Number. Defining the start number of the enumerate object. Default 0
#tuple
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))
#[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

x = ('apple', 'banana', 'cherry')
y = enumerate(x,1)
print(list(y))
#[(1, 'apple'), (2, 'banana'), (3, 'cherry')]
#list
x = ['apple', 'banana', 'cherry']
y = enumerate(x,1)
print(list(y))
#set
x = {'apple', 'banana', 'cherry'}
y = enumerate(x,1)
print(list(y))

'''**************************************************************************************************'''
#18. eval():Evaluates and executes an expression
#19. exec():Executes the specified code (or object)
#20. filter():Use a filter function to exclude items in an iterable object.
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x >= 18:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)

'''**************************************************************************************************'''
#21. float():Returns a floating point number
x = float(3)
print(x) #3.0

'''**************************************************************************************************'''
#22. format():Formats a specified value
x = format(0.5, '%')
print(x) #50.000000%
#'x' - Hex format, lower case
x = format(255, 'x')
print(x) #ff

'''**************************************************************************************************'''
#23. frozenset():Returns a frozenset object
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x) #frozenset({'cherry', 'apple', 'banana'})

'''**************************************************************************************************'''
#24. getattr():Returns the value of the specified attribute (property or method)
#24.1 getattr(object, attribute, default)
class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person, 'age')
print(x)
#36
#24.2 Use the "default" parameter to write a message when the attribute does not exist.
class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person, 'page', 'my message')
print(x) #my message

'''**************************************************************************************************'''
#25.globals():Returns the current global symbol table as a dictionary.
x = globals()
print(x)
#Get the filename of the current program:
x = globals()
print(x["__file__"]) #demo_ref_globals2.py

'''**************************************************************************************************'''
#26. hasattr()	Returns True if the specified object has the specified attribute (property/method).
class Person:
  name = "John"
  age = 36
  country = "Norway"
x = hasattr(Person, 'age')
print(x) #True

'''**************************************************************************************************'''
#27.hash():Returns the hash value of a specified object
#28.help():Executes the built-in help system
#29. hex():Converts a number into a hexadecimal value
x = hex(255)
print(x)
#0xff

'''**************************************************************************************************'''
#30. id():Returns the id of an object
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y) #62124610

# This value is the memory address of the object
#  and will be different every time you run the program

'''**************************************************************************************************'''
#31. input():Allowing user input
print("Enter your name:")
x = input()
print("Hello, " + x)

x = input('Enter your name:')
print('Hello, ' + x)
'''
Enter your name:
joe
Hello, joe'''

'''**************************************************************************************************'''
#32. int():Returns an integer number
x = int(3.5)
print(x) #3

'''**************************************************************************************************'''
#33.isinstance():Returns True if a specified object is an instance of a specified object
#33.1Check if the number 5 is an integer:
x = isinstance(5, int)
print(x) #True

#33.2 Check if "Hello" is one of the types described in the type parameter:
x = isinstance("Hello", (str, float, int, str, list, dict, tuple))
print(x) #True

#33.3 Check if y is an instance of myObj:
class myObj:
  name = "John"
y = myObj()
x = isinstance(y, myObj)
print(x) #True

'''**************************************************************************************************'''
#34. issubclass():Returns True if a specified class is a subclass of a specified object.
#Check if the class myObj is a subclass of myAge:
class myAge:
  age = 36
class myObj(myAge):
  name = "John"
  age = myAge
x = issubclass(myObj, myAge) #True

'''**************************************************************************************************'''
#35.iter():Returns an iterator object.
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(list(x))
'''
apple
banana
['cherry']
'''
'''**************************************************************************************************'''
#36. len():Returns the length of an object
#36.1 Return the number of items in a list:
mylist = ["apple", "banana", "cherry"]
x = len(mylist) #3
#36.2 Return the number of characters in a string:
mylist = "Hello"
x = len(mylist) #5

'''**************************************************************************************************'''
#37.list():Returns a list
x = list(('apple', 'banana', 'cherry'))
print(x)
#['apple', banana', 'cherry']

'''**************************************************************************************************'''
#38. locals():Returns an updated dictionary of the current local symbol table
#Get the filename of the current program:
x = locals()
print(x["__file__"])
#demo_ref_globals2.py

'''**************************************************************************************************'''
#39. map():Returns the specified iterator with the specified function applied to each item
#Calculate the length of each word in the tuple:
def myfunc(a):
  return len(a)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
#convert the map into a list, for readability:
print(list(x))

"""
<map object at 0x056D44F0>
[5, 6, 6]
"""

'''**************************************************************************************************'''
#40. max():Returns the largest item in an iterable
#40.1 Return the largest number:
x = max(5, 10)
print(x) #10
#40.2 Return the name with the highest value, ordered alphabetically:
x = max("Mike", "John", "Vicky")
print(x) #Vicky
#40.3Return the item in a tuple with the highest value:
a = (1, 5, 3, 9)
x = max(a) #9

'''**************************************************************************************************'''
#41. memoryview():Returns a memory view object.
#Create and print a memoryview object:
x = memoryview(b"Hello")
print(x) #<memory at 0x03348FA0>
#return the Unicode of the first character
print(x[0]) #72
#return the Unicode of the second character
print(x[1]) #101

'''**************************************************************************************************'''
#42. min():Returns the smallest item in an iterable
#42.1 Return the lowest number:
x = min(5, 10)
print(x) #5

#42.2 Return the name with the lowest value, ordered alphabetically:
x = min("Mike", "John", "Vicky")
print(x) #John

#42.3 Return the item in a tuple with the lowest value:
a = (1, 5, 3, 9)
x = min(a)
print(x) #1

'''**************************************************************************************************'''
#43.next():Returns the next item in an iterable
#43.1 Create an iterator, and print the items one by one:
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x) #apple
x = next(mylist)
print(x) #banana
x = next(mylist)
print(x) #cherry

#43.2 Return a default value when the iterable has reached to its end:
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x) #apple
x = next(mylist, "orange")
print(x)#banana
x = next(mylist, "orange")
print(x)#cherry
x = next(mylist, "orange")
print(x)#orange

'''**************************************************************************************************'''
#44.object():Returns a new object
x = object()
print(dir(x))

x = object()
y=list(dir(x))
for i in y:
  print(i)

'''**************************************************************************************************'''
#45.oct():Converts a number into an octal
x = oct(12)
print(x) #0o14

'''**************************************************************************************************'''
#46. open():Opens a file and returns a file object
'''
open(file, mode)
file:The path and name of the file
mode:A string, define which mode you want to open the file in:
	"r" - Read - Default value. Opens a file for reading, error if the file does not exist
	"a" - Append - Opens a file for appending, creates the file if it does not exist
	"w" - Write - Opens a file for writing, creates the file if it does not exist
	"x" - Create - Creates the specified file, returns an error if the file exist
In addition you can specify if the file should be handled as binary or text mode
	"t" - Text - Default value. Text mode
	"b" - Binary - Binary mode (e.g. images)
'''
f = open("C:/Users/cnakk/OneDrive/Desktop/Python/PythonDan-repo/demofile.txt", "r")
#C:\Users\cnakk\OneDrive\Desktop\Python\PythonDan-repo\demofile.txt
print(f.read())

'''**************************************************************************************************'''
#47.ord():Convert an integer representing the Unicode of the specified character
x = ord("h")
print(x) #104

'''**************************************************************************************************'''
#48.pow():Returns the value of x to the power of y
'''
pow(x, y, z)
x:A number, the base
y:A number, the exponent
z:Optional. A number, the modulus
'''
x = pow(4, 3) #4*4*4
print(x) #64

x = pow(4, 3, 5) #(4*4*4)%5
print(x) #4

'''**************************************************************************************************'''
#49.print()	Prints to the standard output device
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
a = 5
#print("a =", a, sep='00000', end='\n\n\n')
print("a =", a, sep='0', end='')
#see print_demo.py for file = sourceFile example

'''**************************************************************************************************'''
#50.property():Gets, sets, deletes a property
#51.range():Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
'''
range(start, stop, step)
start:Optional. An integer number specifying at which position to start. Default is 0
stop: Required. An integer number specifying at which position to stop (not included).
step:Optional. An integer number specifying the incrementation. Default is 1
'''
#51.1 Create a sequence of numbers from 0 to 5, and print each item in the sequence:
print("\n")
a=[]
x = range(6)
for n in x:
  a.append(n)
print(a)

#51.2 Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
a=[]
x = range(3, 20, 2)
for n in x:
  a.append(n)
print(a)

'''**************************************************************************************************'''
#52.repr():Returns a readable version of an object
#53.reversed():Returns a reversed iterator
#Reverse the sequence of a list, and print each item:
a=[]
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  a.append(x)
print(a)

'''**************************************************************************************************'''
#54.round():Rounds a numbers
#round(number, digits)
#54.1 Round a number to only two decimals
x = round(5.76543, 2)
print(x) #5.77

#54.2 Round to the nearest integer:
x = round(5.76543)
print(x) #6

'''**************************************************************************************************'''
#55. set():Returns a new set object
#Create a set containing fruit names:
x = set(("apple", "banana", "cherry"))
print(x)
# Note: the set list is unordered, so the result will display the items in a random order.
#{'apple', 'cherry', 'banana'}

'''**************************************************************************************************'''
#56. setattr()	Sets an attribute (property/method) of an object
#Change the value of the "age" property of the "person" object:
class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)
# The age property will now have the value: 40
x = getattr(Person, 'age')
print(x)
#40

'''**************************************************************************************************'''
#57.slice():Returns a slice object
#57.1 Create a tuple and a slice object. Use the slice object to get only the two first items of the tuple:
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])
#('a', 'b')

#57.2 Create a tuple and a slice object. Start the slice object at position 3, and slice to position 5, and return the result:
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])
#('d', 'e')

#57.3 Create a tuple and a slice object. Use the step parameter to return every third item:
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])
#('a', 'd', 'g')

'''**************************************************************************************************'''
#58.sorted():Returns a sorted list.
#58.1 , key=key, reverse=reverse)
tup1 = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(tup1)
print(x)
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#58.2 Sort descending:
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)
#['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

'''**************************************************************************************************'''
#59.staticmethod():Converts a method into a static method
#60.str():Returns a string object
#Convert the number 3.5 into an string:
x = str(3.5)
print(type(x))#<class 'str'>
print(x) #3.5

'''**************************************************************************************************'''
#61. sum():Sums the items of an iterator
#sum(iterable, start)
#61.1 Add all items in a tuple, and return the result:
a = (1, 2, 3, 4, 5)
x = sum(a)
print(x) #15

#61.2 Start with the number 7, and add all the items in a tuple to this number:
a = (1, 2, 3, 4, 5)
x = sum(a, 7)
print(x) #22

'''**************************************************************************************************'''
#62.super():Returns an object that represents the parent class
# #Create a class that will inherit all the methods and properties from another class:
class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()
#Hello, and welcome!

'''**************************************************************************************************'''
#63.tuple()	Returns a tuple.
#Create a tuple containing fruit names:
x = tuple(("apple", "banana", "cherry"))
print(x)
#('banana', 'cherry', 'apple')

'''**************************************************************************************************'''
#64.type()	Returns the type of an object.
'''
type(object, bases, dict)
object: Required. If only one parameter is specified, the type() function returns the type of this object
bases: Optional. Specifies the base classes
dict: Optional. Specifies the namespace with the definition for the class
'''
#Return the type of these objects:
a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33

x = type(a)
y = type(b)
z = type(c)

print(x) #<class 'tuple'>
print(y) #<class 'str'>
print(z) #<class 'int'>

'''**************************************************************************************************'''
#65.vars():Returns the __dict__ property of an object
#Return the __dict__ atribute of an object called Person:
class Person:
  name = "John"
  age = 36
  country = "norway"
x = vars(Person)
print(x)

'''**************************************************************************************************'''
#66. zip()	Returns an iterator, from two or more iterators
#zip(iterator1, iterator2, iterator3 ...)
#66.1 Join two tuples together:
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
#use the tuple() function to display a readable version of the result:
print(tuple(x))
#(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))

#66.2 If one tuple contains more items, these items are ignored:
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = zip(a, b)
#use the tuple() function to display a readable version of the result:
print(tuple(x))
#(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
'''**************************************************************************************************'''