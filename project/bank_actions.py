customer_information1 ={
            1234:{   
                                        "name":"Mark",      # only characters no symbols
                                        "dob":"12-12-1992",           # dd-mm-yyyy
                                        "account_number":1234, # integer only
                                        "password":0000,    #4 digit number
                                        "balance":43,       # integer only
                                        "address":{
                                                    "street":"47th",
                                                    "door_no":243,
                                                    "city":"Salt Lake",
                                                    "pincode":456
                                                },       # door no, street, city, pincode
                                        "ssn":12345         # 5 digit number
                                    
                            } }
customer_information2 ={
            2345:{   
                                        "name":"AC",      # only characters no symbols
                                        "dob":"12-12-1988",           # dd-mm-yyyy
                                        "account_number":2345, # integer only
                                        "password":0000,    #4 digit number
                                        "balance":43,       # integer only
                                        "address":{
                                                    "street":"50th",
                                                    "door_no":43,
                                                    "city":"Lake",
                                                    "pincode":908
                                                },       # door no, street, city, pincode
                                        "ssn":67890         # 5 digit number
                                    
                            } }
# 1.add customer
# 2.get customer details 
# 3.update customer 
# 4.delete customer 

import datetime
from tabnanny import check 
customer_information = {}
last_account_number = 45390   # 5 digit number

def customer_info_validation(pincode,ssn,dob,name): # pincode, ssn, dob, name 
    for element in ["_",",",".","1","2","3","4","5","6","7","8","9","0"]:
        if (element in name):
            return False,"Name contains symbol or number"
    
    if len(ssn) != 5:
        return False,"invalid ssn"

    elif len(dob.split("-")) != 3:
        return False,"Invalid date"
        
    elif len(dob.split("-")[0]) != 2 or int(dob.split("-")[0]) > 30:
    
        return False,"Invalid date or date out of range"
    
    elif len(dob.split("-")[1]) != 2 or int(dob.split("-")[1]) > 12:
        return False,"Invalid month or month out of range"
    
    elif len(dob.split("-")[2]) != 4 or (datetime.date.today().year - int(dob.split("-")[2]) < 18):
        return False,"Invalid year or less than 18 years"

    elif (len(pincode) != 3):
        return False,"invalid pincode"
    else:
        return True,None

def address():
    door_no = input("Door no : ")
    street = input("Street : ")
    city = input("City : ")
    pincode = input("Pincode (3 digit:) ")   # 3 digit
    return {"door_no":door_no,"street":street,"city":city,"pin":pincode}

def add_customer():
    global last_account_number
    print ("Custome info here .... ")
    name = input("Name : ")
    dob = input("Date of birth (dd-mm-yyyy) : ")
    password=9999
    account_number = last_account_number
    initial_deposit = input("Initial Doposit Amount : ")
    addr = address()
    ssn = input("Enter ssn (5 digit number)")

    validated = customer_info_validation(addr["pin"],ssn,dob,name)
    
    if (validated[0]):
        customer_information.update(
            {
                account_number:{
                                    "name":name,
                                    "dob":dob,
                                    "password":password,
                                    "balance":initial_deposit,
                                    "ssn":ssn,
                                    "address":addr

                                }
            }
        )
        
        last_account_number+=1
    else:
        print ("Adding customer failed",validated[1])
    print ("customer_information:",customer_information)
    
def acc_check():
     account_number=int(input("Enter account_number:"))
     if(customer_information1[1234]["account_number"]!=account_number):
        print("account_number is not valied number")
        acc_check()
        #return account_number

def pass_check():
     password=int(input("Enter password:"))
     if(customer_information1[1234]["password"]!=password):
        print("password is not valied number")
        pass_check()

def get_customer():
    acc_check()
    pass_check()
    print(customer_information1)
    #print(customer_information1[1234]["password"]== password1)
    #print(type(customer_information1[1234]["password"]))
    #print((customer_information1[1234]==account_number))
    #print(type(customer_information1[1234]))
    
def update_customer():
    acc_check()
    pass_check()
    choice = input("Select 1. Password Update, 2. Address Update:")
    if(choice == "1"):
        password = input("Enter 4 digit number")
        customer_information1[1234]["password"]= password
        print(customer_information1)
    elif(choice == "2"):
       addr1= address()
       customer_information1[1234]["address"].update(addr1)
       print(customer_information1)

#update_customer()

def delete_customer():
    acc_check()
    pass_check()
    del customer_information1[1234]
    print(customer_information1)
    
#*******************************************************************************************************