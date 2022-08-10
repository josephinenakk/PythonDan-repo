
#Method	     #Description
"""
1.append()  #Adds an element at the end of the list
2.copy()	#Returns a copy of the list
3.count()	#Returns the number of elements with the specified value
4.extend()	#Add the elements of a list (or any iterable), to the end of the current list
5.index()	#Returns the index of the first element with the specified value
6.insert()	#Adds an element at the specified position
7.pop()	    #Removes the element at the specified position
8.remove()	#Removes the first item with the specified value
9.reverse() #Reverses the order of the list
10.sort()	 #Sorts the list
11.clear()	#Removes all the elements from the list
"""
#########################################################################################
#########################################################################################

continent_and_countries = [["Austria","German","Slovene","Croatian","English"],
["Belize","English" , "Spanish", "Mayan", "Garifuna (Carib)", "Creole"],
["Georgia","Georgian", "Russian", "Armenian", "Azerbaijani", "Abkhaz"],
["India","Hindi", "English", "Bengali", "Gujarati","Marathi"," Oriya"," Tamil","Telugu"],
["Israel","Hebrew"," Arabic", "English", "Russian"],
["Italy","Italian" ,"German" , "French" ,"Slovene"],
["Mongolia","Mongolian","Turkic", "Russian", "Chinese"] ]

# 1.append()
continent_and_countries1=["Switzerland", "German","French", "Italian", "Romansch"]
continent_and_countries .append(continent_and_countries1)
print("Append method example ==" ,continent_and_countries )
print("\n")

# 2.copy()
x =continent_and_countries.copy()
print("copy method example = ",x)
print("\n")

# 3.count()
y=continent_and_countries.count("English")
print("count method example = ", y)
z=continent_and_countries[3].count("English")
print("count method example with index = ", z)
print("\n")

# 4.extend()
continent_and_countries.extend(["Georgia","Hawaii"])
print("extend method example = ",continent_and_countries)
print("\n")

#5.index()
i =continent_and_countries.index("Georgia")
print("index method example  = ",i)
print("\n")

#6.insert() 
continent_and_countries.insert(0,"English")
print ("insert method example",continent_and_countries)
print("\n")

#7.pop()
continent_and_countries.pop(0)
print ("pop method example",continent_and_countries )
print("\n")


#8.remove() ----by index number
continent_and_countries[3].remove("English")
print ("remove method example",continent_and_countries)
print("\n")

#9.reverse()
continent_and_countries[2].reverse()
print ("reverse method example",continent_and_countries[2])
print("\n")
#print ("reversemethod example",continent_and_countries)

#10.sort()
continent_and_countries[0].sort()
print ("sort method example",continent_and_countries[0])
print("\n")
#print ("sort method example",continent_and_countries)

#11.clear()
continent_and_countries[0].clear()
print ("clear method example",continent_and_countries[0])
print("\n")
print ("sort method example",continent_and_countries)