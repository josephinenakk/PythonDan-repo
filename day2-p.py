# 1.How Python Stores the values in its memory?
"""
Variables are nothing but reserved memory locations to store values. 
That is when you create a variable you reserve some space in memory.
Python optimizes memory utilization by allocating the same object reference 
to a new variable if the object already exists with the same value.
 """

# 2. What is a variable Why we need one ?
""" 
A Python variable is a symbolic name that is a reference or pointer to an object.
Once an object is assigned to a variable, you can refer to the object by that name.
"""
# 3. How to declare a variable ?
"""
a = "gfinejoe"
b = 3
"""

# 4. comments in python.
"""
1. #singleline comment
""" 
""" 2. multilinecomment """
''' 3. multilinecomment  '''
""" 

"""

# 5. python syntax.
"""
print ("name") #print statement example
"""
# 6. indentation in Python.
"""
Indentation refers to the spaces at the beginning of a code line. 
Where in other programming languages the indentation in code is for readability only, 
the indentation in Python is very important. Python uses indentation to indicate a block of code.
"""

# 7. GitHub
  #https://github.com/josephinenakk/PythonDan-repo.git

 
# 8. Create individual  branch

python_batch_details = [
    ["x","y",10,["z","a","b"],["masters"]],
    ["x","y",10,["z","a","b"],["masters"]],
    ["x","y",10,["z","a","b"],["masters"]],

]

fourth_person_details = ["x","y",8,["rick","john","yes"],["masters"]]



# pybde = [[],[],[],3,False]

python_batch_details.append(fourth_person_details)
python_batch_details.append(4)
python_batch_details.append(True)

python_batch_details.insert(0,"Instructor")
print(python_batch_details)

continent_and_countries = [["Austria","German","Slovene","Croatian","English"],
["Belize","English" , "Spanish", "Mayan", "Garifuna (Carib)", "Creole"],
["Georgia","Georgian", "Russian", "Armenian", "Azerbaijani", "Abkhaz"],
["India","Hindi", "English", "Bengali", "Gujarati","Marathi"," Oriya"," Tamil","Telugu"],
["Israel","Hebrew"," Arabic", "English", "Russian"],
["Italy","Italian" ,"German" , "French" ,"Slovene"],
["Mongolia","Mongolian","Turkic", "Russian", "Chinese"] ]
#7.pop()
a=continent_and_countries.pop(0)
print ("pop method example",a ,'\n')
#print("\n")
print(continent_and_countries)