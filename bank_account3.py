"""Python Learnings Bank
    Please enter account number - 8943  # This account number should be 4 digit
    Please enter valid account number
    Account doesnt exists!! please try again
    Please enter your pin - 45 # pin number should always be 2 digit
       Welcom Mr Mark / Ms Leena
       please select from following options
            1. withdrawl
            2. balance display
            if 2 -> Your account has 34$
            if 1->  please enter amount you want to withdraw - 35
            if withdrawl amount is in the range please update the balance in the dictionary 
            else display insufficient funds message
        you want to continue 1 or 2 
        to exit press 3"""
        
people = {1234: {'name': 'Mark', 'balance': 27, 'Gender': 'Male','pin':45},
          4567: {'name': 'Marie', 'balance': 22, 'Gender': 'Female','pin':32}}
def gettingAccountNumber():
    global x
    x=input("Account number:")
    if (len(x)!=4 and int(x) not in people.keys()):
        print("\nPlease Enter Valid")
        gettingAccountNumber()
def getPin():
    global x
    x=int(x)
    y=input("Pin Number:")
    if(len(y)!=2 and people[x]["pin"]!=int(y)):
        print("\nPlease Enter Valid")
        getPin()
def welcome():
    global x
    x=int(x)
    if(people[x]["Gender"]=='Male'):
         print("\nwelcom Mr.",people[x]["name"])
    else:
        print("\nwelcom Mrs.",people[x]["name"])
gettingAccountNumber()
getPin()
welcome()

def withdraw_money():
    w_amount = int(input('How much money you want to withdraw :$'))
    if w_amount > people[x]['balance']:
            print('Your account does not have that much money')
    else:
            people[x]['balance'] = people[x]['balance'] - w_amount
            print(f'${w_amount} has been withrawn from your account your total balance left is $ {people[x]["balance"]}')
            print('')

def balance():
    print('your account your total balance left is:', {people[x]["balance"]})

funtion=input( "\nEnter for Withdrawl= 1 or Balance= 2  or Quit= 3:")
def start():
    if(funtion == '1'):
        print("withdrawing Money")
        withdraw_money()
    elif(funtion =="2"):
        print("Cheking Balance")
        balance()
    elif(funtion=="3"):
        print("good bye")
start()