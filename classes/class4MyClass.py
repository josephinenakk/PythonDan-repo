#Python Context Managers and the "with" Statement (__enter__ & __exit__)
class MyClass:

     def __init__(self):
         self.name = "lao"
     # def __enter__(self):
#     #     print ("Hello")

#     # def __exit__(self, exc_type, exc_val, exc_tb):
#     #     print ("World")

#     def __repr__(self):
#         return f"Hello {self.name}"



print (MyClass())

# # with MyClass() as cls:
# #     print ("My class")



# # A simple Person class

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         rep = 'Person(' + self.name + ',' + str(self.age) + ')'
#         return rep


# # Let's make a Person object and print the results of repr()

# # person = Person("John", 20)
# # print(repr(person))