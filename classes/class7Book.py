class Book:
    """class space"""
    publisher = "P1"
    
    def __init__(self,author,book_name):
        # print (f"{author},{book_name}")
        self.author = author
        self.book_name = book_name
        self.__price = 10

    def edit_private(self,x):
        self.__price = x
        return self.__price

    def display(self):
        return (f"Book Publisher is {Book.publisher} , Book name is {self.book_name} and the author is {self.author}")

b1 = Book("author 1","First_book ")
b2 = Book("author 1","Second_book ")
b3 = Book("author 2","Third_book ")

print (b1.display())
print (b2.display())
print (b3.display())
print (b3.edit_private(4))
