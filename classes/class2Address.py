#to understand self
class check:
    def __init__(self):
        print("Address of self in __init__ method = ",id(self))
 
obj = check()
print("Address of class object = ",id(obj),"\n")

"""
Address of self in __init__ method =  2504100954064
Address of class object =  2504100954064 
"""

class Address:
    city = None
    def __init__(self): #inintilising self
         pass
    
    def add_city(self,city):
         self.city = city
         print(city)

class CustomerOps(Address):
    
    customer_information = {}
    las_cust_num = 1

    def __init__(self):
        pass
    def add(self,name):
         self.customer_information.update({self.las_cust_num:name})
         self.las_cust_num+=1
         #self.add_city(name)

    def get(self,num):
         print(self.customer_information[num])

    def update(self,name):
         self.customer_information.update({self.las_cust_num:name})
    
    def remove(self,num):
         del self.customer_information[num]

bank_1 = CustomerOps()
bank_1.add("name 1")
bank_1.add("name 2")
bank_1.add_city("city 1")
print ("\nline-48:",bank_1.customer_information,"\n")

bank_1.get(2)
bank_1.update("na")
print ('\nline-52:update("na"): ',bank_1.customer_information)
bank_1.remove(2)
print ("\nline-54:remove(2)",bank_1.customer_information,"\n")