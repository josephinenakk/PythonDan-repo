a =[1,2,3,4,5,[[1,2,3]]]
b =[5,6]
a.extend(b) # ANSWER: [1, 2, 3, 4, 5, [1, 2, 3], 5, 6]
print(a)

a.append(7) 
print(a)  # ANSWER:[1, 2, 3, 4, 5, [1, 2, 3], 5, 6, 7]

a.extend("abc")
print(a) # ANSWER:[1, 2, 3, 4, 5, [1, 2, 3], 5, 6, 7, 'a', 'b', 'c']

a.pop()
print(a) # ANSWER:[1, 2, 3, 4, 5, [1, 2, 3], 5, 6, 7, 'a', 'b']

a.pop(4) # takes element index
print(a) # ANSWER:[1, 2, 3, 4, [1, 2, 3], 5, 6, 7, 'a', 'b']

print("To print a",a[0:])

print("To Skipping even index values",a[::2]) #strating index 0 so no to need mention ,s.index::index -1

print("To Skipping two values",a[::3]) 
print("To Skipping three values",a[::4]) 
print("printing a=",a)

a[4][0].append(4)
print("appending 4 in list of list=",a)



