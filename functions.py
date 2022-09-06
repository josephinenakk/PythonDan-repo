"""
            -----  Python Functions -----
1.A function is a block of code which only runs when it is called.
2.with Functions ita able to code reuse.
3.Python provides several built-in functions such as print(), len() or type(), 
but you can also define your own functions to use within your programs
"""
#1.Create a Function
print("\nline 9- 1.Create a Function")
def hello():
    print("hi there")
#2. call the function
hello()

'''
Answer:
line 9- 1.Create a Function
hi there
'''
#---------------------------------------------------------------------------------------------
#A.Pass Arguments
#3.Pass single argument to a function
print("\nline 23- 3.Pass single argument to a function")
def hello1(name):
    print('Hello,', name)
hello1('BobCat')
hello1('SamMat')

'''
Answer:
line 23- 3.Pass single argument to a function
Hello, BobCat
Hello, SamMat
'''
#---------------------------------------------------------------------------------------------
#4. Pass two arguments
print("\nline 37- 4. Pass two arguments")
def details(name, job):
    print(name, 'is a', job)
details('Matthew', 'developer')

'''
Answer:
line 37- 4. Pass two arguments
Matthew is a developer
'''
#---------------------------------------------------------------------------------------------
#Types of Arguments
#a. Positional Arguments
#b. Keyword Arguments
#c. Default Arguments
#d. Variable Length Positional Arguments (*args)
#f. Variable Length Keyword Arguments (**kwargs)

#5.Positional Arguments
#The most common are positional arguments, whose values are copied to their corresponding parameters in order.
print("\nline 57- 5.Positional Arguments")
def person1(name, job):
    print(name, 'is a', job)
person1("Dinakar","funtional developer")

'''
Answer:
line 57- 5.Positional Arguments
Dinakar is a funtional developer
'''
#---------------------------------------------------------------------------------------------
#6.Keyword Arguments
print('\nline 69- Keyword arguments can be put in any order')
def person2(name, job):
    print(name, 'is a', job)
person2(name='Bob', job='developer')
person2(job='developer', name='Bob')
'''
Answer:
line 69- Keyword arguments can be put in any order
Bob is a developer
Bob is a developer
'''
#---------------------------------------------------------------------------------------------
#7.Default Arguments
#You can specify default values for arguments when defining a function.
#  The default value is used if the function is called without a corresponding argument.
# Set default value 'developer' to a 'job' parameter
print("\nline 85- Default Arguments")
def person3(name, job='developer'):
    print(name, 'is a', job)
person3('Luke', 'manager')
person3('Luke')
'''
Answer:
line 85- Default Arguments
Luke is a manager
Luke is a developer
'''
#---------------------------------------------------------------------------------------------
#8.Variable Length Arguments (*args and **kwargs)
#Variable length arguments are useful when you want to create functions that take unlimited number of arguments.
#This feature is often referred to as var-args.
#*args
print('\nline 101- 8.Variable Length Arguments')
def many(*args):
    print(args)
many(1, 54, 60, 8, 98, 12)

'''
Answer:
line 101- 8.Variable Length Arguments
(1, 54, 60, 8, 98, 12)
'''
#---------------------------------------------------------------------------------------------
#9.**kwargs
"""**kwargs
The ** syntax is similar, but it only works for keyword arguments.
It collects them into a new dictionary, where the argument names are the keys, 
and their values are the corresponding dictionary values."""
print('\nline 117- 9.**kwargs')
def dict(**kwargs):
    print(kwargs)
dict(name='Bob', age=25, job='dev')

'''
Answer:
line 117- 9.**kwargs
{'name': 'Bob', 'age': 25, 'job': 'dev'}
'''
#---------------------------------------------------------------------------------------------
#10.Return Value
print('\nline 129- 10.Return Value')
def math1_addition(a,b):
    return(a+b)
print(math1_addition(4,5))

'''
Answer:
line 129- 10.Return Value
9
'''
#---------------------------------------------------------------------------------------------
#11. Return Multiple Values
print('\nline 141- 11. Return Multiple Values')
def math2_addition(a,b):
    return(a+b, a-b)
print(math2_addition(4,5))

'''
Answer:
line 141- 11. Return Multiple Values
(9, -1)
'''
#---------------------------------------------------------------------------------------------
#11.Unpack returned tuple
print('\nline 153- #11.Unpack returned tuple')
def math3_addition(a, b):
    return a+b, a-b
add, sub = math3_addition(4, 5)
print(add)
print(sub)

'''
Answer:
line 153- #11.Unpack returned tuple
9
-1
'''
#---------------------------------------------------------------------------------------------
#12.Docstring
"""
You can attach documentation to a function definition by including a string literal
just after the function header. Docstrings are usually triple quoted to allow 
for multi-line descriptions.
"""
print('\nline 173- 12.Docstring')
def hello():
    """This function prints
       message on the screen"""  
    print('Hello, World!')

hello()
help(hello)
print(hello.__doc__)

'''
Answer:
line 173- 12.Docstring
Hello, World!
Help on function hello in module __main__:

hello()
    This function prints
    message on the screen

This function prints
       message on the screen
'''
#---------------------------------------------------------------------------------------------
#13.Nested Functions
print('\nline 198- 13.Nested Functions')
def gol(a,b):
    def gol2(c,d):
        return(c+d)
    return gol2(a,b)
print(gol(1,2))

'''
Answer:
line 198- 13.Nested Functions
3
'''
#---------------------------------------------------------------------------------------------
#14. Recursion
#A recursive function is a function that calls itself 
# and repeats its behavior until some condition is met to return a result.
print('\nline 214- 14. Recursion')
def exampl(num):
    if(num<=0):
        print(num,"from if")
    else:
        print(num,"from else")
        exampl(num-1)
exampl(5)

'''
Answer:
line 214- 14. Recursion
5 from else
4 from else
3 from else
2 from else
1 from else
0 from if
'''
#---------------------------------------------------------------------------------------------
#15. Assigning Functions to Variables
print('\nline 235- 15. Assigning Functions to Variables')
def goodday():
    print('from goodday') 
hi = goodday
hi()

'''
Answer:
line 235- 15. Assigning Functions to Variables
from goodday
'''
#---------------------------------------------------------------------------------------------
#16.Assigning multiple Functions to single Variable
print('\nline 248-16.Assigning multiple Functions to single Variable ')
def findSquare(x):
    return x ** 2

def findCube(x):
    return x ** 3
exponent = {'square': findSquare, 'cube': findCube}
print(exponent['square'](3))
print(exponent['cube'](3))
print({'square':exponent['square'](3),'cube': exponent['cube'](3)})

'''
Answer:
line 248-16.Assigning multiple Functions to single Variable
9
27
{'square': 9, 'cube': 27}
'''
#---------------------------------------------------------------------------------------------
#17.Python Function Executes at Runtime
print('\nline 268- 17.Python Function Executes at Runtime')
x = 0
if x:
    def hello():
        print('Hello, World!')
else:
    def hello():
        print('Hello, Universe!')
hello()

'''
Answer:
line 268- 17.Python Function Executes at Runtime
Hello, Universe!
'''
#---------------------------------------------------------------------------------------------