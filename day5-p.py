""" Clone your own repository.
    Write a program to pring 
            biodata of a sample person X
            Name,Age,marital,children,

 "I am learning Python"
 use slicing concepts on the above and print the words
 make sure you have in-line
    push your code to the repository
    share your code link in the group"""


FirstName = "Joseph"                         # String datatype
MiddleName = "Daniel"                            
LastName = "Jos"
Age = 35                                   # Integer
Height_in_centimeters = 170    
Weight_in_kilograms = 90.12               # Float
Marital_status = True
height_in_feet = '5\'11'        # escape sequence in string
No_of_kids = 4  


print ("Name = " + FirstName +" " + MiddleName + " "+ LastName)

print ("Age= " , Age )
print (" Height(cm)= " ,Height_in_centimeters)
print ("weight(kg)=" , Weight_in_kilograms)
print ("Marital Status =" , Marital_status)
print ("Height=", height_in_feet)
print("kids =", No_of_kids)

###################
#2. slicing concepts
Hello ="I am learning Python"
print(Hello[0:5])
print(Hello[0:-1])
print(Hello[5:-2])
print(Hello[-6:20])

##########
#List inside list example
List_example =[ 1,2,3,4,"dan",[54,67,89,"hoe"],"ok",5]
print(List_example [1])
print(List_example [4][2])
print(List_example [5][3][2])
print(List_example [6])
List_example =[ 1,2,3,4,"dan",[54,67,89,"hoe"],"ok",5]
print(List_example [5][3][0:2])# to print ho [starting point : endingpoint+1] but not toget end point too.
#1fistname = "u"
#print(fistname)
print(List_example [5][1])
print(List_example [5][3][0])