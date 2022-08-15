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
list_exampl = [ "New York", "Los Angles", "Boston", "Denver","Alabama","colorado" ,"New York"]
# 1.append()
list_exampl.append("Florida")
print("Append method example ==" ,list_exampl )

# 2.copy()
x=list_exampl.copy()
print(" 2.copy() = ",x)

# 3.count()
y=list_exampl.count("Boston")
print("3.count() = ", y)
z=list_exampl.count("New York")
print("3.count() = ", z)

# 4.extend()
list_exampl.extend(["Georgia","Hawaii"])
print("4.extend() = ",list_exampl)

#5.index()
i =list_exampl.index("Georgia")
print("5.index() = ",i)

#6.insert()

