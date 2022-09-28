"""       1. creating a class      """
class School_supplies:        
    pass
list1=School_supplies()     # creating object from the class 
print("\nline-5:",list1,type(list1))
#line-5: <__main__.School_supplies object at 0x00000281DCAC3FD0> <class '__main__.School_supplies'>

list2=School_supplies()
print("\nline-9:",list2,type(list2),"\n")
#line-9: <__main__.School_supplies object at 0x00000281DCAC3EB0> <class '__main__.School_supplies'>

"""***********************************************************"""
"""           2. creating class with parameters            """

class Transactions:

    transactions = []
    dollar_rate = 79.0

    def __init__(self,amount,payer,payee,bank_name):
        self.amount1 = amount 
        self.payer1 = payer
        self.payee1 = payee
        bank_name = bank_name       # method variable
        print (f"Welcome to {bank_name} Bank")   
        Transactions.transactions.append(self)
    def __repr__(self):
        return(f"{self.amount1},{self.payer1},{self.payee1}")
        ##line-37 repr 1,2,2 <class 'str'> the way return given
        #return(f"{self.amount1}{self.payer1}{self.payee1}")
        #line-37 repr 122 <class 'str'>
    def conversion(self):
        return self.amount1 * Transactions.dollar_rate   
#In Python, __repr__ is a special method used to represent a class’s objects as a string

print ("\nline-35:",Transactions.__dict__) # list of all the class level attributes
# 1. creating instance of class
tra1= Transactions(1,2,2,"Chesse") #constractor, dont need mention self arugment by default it takes the instance working of that class.
print("\nline-40:",tra1.__dict__) 
print(Transactions.conversion(tra1))  # list of all the instance level attributes
#line-40: {'amount1': 1, 'payer1': 2, 'payee1': 2}

#2. geeting method --repr--
tra1=Transactions("r","r","r","RBT")
x=repr(tra1) 
print("\nline-46 repr",x,type(x))
#line-46 repr r,r,r <class 'str'>

#3. All instanceswith same name appending in the list transactions as in creating order
tra1 = Transactions("1",1,1,"US")
print ("\nline-51:",tra1.transactions[0])
#line-44: 1,2,2
print ("\nline-53:",tra1.transactions[1])
#line-53: r,r,r
print ("\nline-55:",tra1.transactions[2])
#line-55: 1,1,1
#print ("\nline-57:",tra1.transactions[3])
#IndexError: list index out of range

#4.list of all instance level attributes
print ("\nline-41:",tra1.__dict__) 
#line-39: {'amount1': '1', 'payer1': 1, 'payee1': 1}

#5. list of all the class level attributes
print("\nline-65:")
for txn1,txn2 in Transactions.__dict__.items():
    print(txn1,":",txn2)
"""
line-65:
__module__ : __main__
transactions : [1,2,2, r,r,r, 1,1,1]
dollar_rate : 79.0
__init__ : <function Transactions.__init__ at 0x00000217C8F3F250>
__repr__ : <function Transactions.__repr__ at 0x00000217C935D990>
__dict__ : <attribute '__dict__' of 'Transactions' objects>
__weakref__ : <attribute '__weakref__' of 'Transactions' objects>
__doc__ : None
"""
#6. a. instance level attributesare not iterable
tra2 =(Transactions(1,2,2,"US")) # list of all instance level attributes not iterable
#for tn in tra2:
     #print (tn)

#b.so making them as iterable object ( converting in dictonary)
print("\nline-84:")
for tn1,tn2 in tra2.__dict__.items():
     print (tn1,":",tn2)
"""
line-84:
amount1 : 1
payer1 : 2
payee1 : 2
"""

#c. convert into string using --resp--
tra2 =Transactions(1,2,2,"US").__repr__()
print(tra2, type(tra2))
#1,2,2 <class 'str'>

#d.converting into string object
tra2 =Transactions(1,2,2,"US").__str__()
print(tra2, type(tra2))

#d. iteration using elements by next 
tra2 =iter(Transactions(1,2,2,"US").__str__())
print(next(tra2)) #1
print(next(tra2)) #,
print(next(tra2)) #2

#e. conversion

