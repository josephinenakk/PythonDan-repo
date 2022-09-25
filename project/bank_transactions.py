"""authentication (accountnumber,password)
        deposit money (accountnumber,money)
        withdraw money (accountnumber,money)
        transfer money within the bank (accountnumber,payee account number,money)
"""
from bank_actions import pass_check,acc_check,customer_information1,customer_information2

def authentication():
    acc_check()
    pass_check()

def deposit(amount):
    authentication()
    customer_information1[1234]["balance"]+=amount
    print(customer_information1)

#deposit(90)

def withdraw_money(amount1):
    authentication()
    if(customer_information1[1234]["balance"]>=amount1):
        customer_information1[1234]["balance"]-=amount1
        print(customer_information1)
    else:
        print("Balance amount is less than withdrawing amount ")
#withdraw_money(67)

def transfer_money(amount2):
    authentication()
    if(customer_information1[1234]["balance"]>=amount2):
        customer_information1[1234]["balance"]-=amount2
        print(customer_information1)
        customer_information2[2345]["balance"]+=amount2
        print(customer_information2)
#transfer_money(10)


def choice1():
    choice =int(input("\nselect below number :\n1 deposit money \n2 withdraw money \n3 transfer money \nEnter numner for above options:"))
    if (choice == 1):
        amount=int(input("Enter the amount to deposit : "))
        deposit(amount)
    elif(choice == 2):
        amount=int(input("Enter the amount to withdraw money : "))
        withdraw_money(amount)
    elif(choice==3):
        amount=int(input("Enter the amount to transfer money : "))
        transfer_money(amount)
    else:
        print("\n\n******************\nwrong option")
        choice1()
        
choice1()

"""
Answer:
select below number :
1 deposit money
2 withdraw money
3 transfer money
Enter numner for above options:3
Enter the amount to transfer money : 20
Enter account_number:1234
Enter password:0000
{1234: {'name': 'Mark', 
'dob': '12-12-1992',
 'account_number': 1234, 
 'password': 0, 'balance': 23, 
 'address': {'street': '47th',  'door_no': 243, 'city': 'Salt Lake', 'pincode': 456},
  'ssn': 12345}}
{2345: {'name': 'AC', 'dob': '12-12-1988', 
'account_number': 2345,
 'password': 0, 
 'balance': 63, 
 'address': {'street': '50th', 'door_no': 43, 'city': 'Lake', 'pincode': 908},
  'ssn': 67890}
"""
#******************************************************************************************************