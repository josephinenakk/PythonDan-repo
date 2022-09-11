"""# Can you 
{1234:{
        name: Mark
        balance : 34
        pin:45 }
    4567:{
        name
        balance
        pin  }}
    Python Learnings Bank
   * Please enter account number - 8943  # This account number should be 4 digit
    * Please enter valid account number
    *Account doesnt exists!! please try again
    *Please enter your pin - 45 # pin number should always be 2 digit
       * Welcom Mr Mark / Ms Leena
        please select from following options
            1. withdrawl
            2. balance display
            if 2 -> Your account has 34$
            if 1->  please enter amount you want to withdraw - 35
            if withdrawl amount is in the range please update the balance in the dictionary 
            else display insufficient funds message
        you want to continue 1 or 2 
        to exit press 3
"""


people = {1234: {'name': 'Mark', 'balance': 27, 'Gender': 'Male','pin':45},
          4567: {'name': 'Marie', 'balance': 22, 'Gender': 'Female','pin':32}}

def gettingAccountNumber():
    global x
    x=input("Enter Account number:")
    if (len(x)==4 and int(x) in people.keys()):
        pass
    else:
        print("Account number is not valied ,Enter correct Account number:",gettingAccountNumber())
    x=int(x)
    y=input("Enter Pin Number:")
    if(len(y)==2 and people[x]["pin"]==int(y)):
        x=int(x)
        if(people[x]["Gender"]=='Male'):
         print("welcom Mr.",people[x]["name"])
        else:
            print("welcom Mrs.",people[x]["name"])
    else:
        print("Account pin is not valied ,Enter correct pin:",gettingAccountNumber())
gettingAccountNumber()
def withdraw_money():
    w_amount = int(input('How much money you want to withdraw : '))
    if w_amount > people[x]['balance']:
            print('Your account does not have that much money')
    elif w_amount == 0:
            print('What you are fooling around here')
    else:
            people[x]['balance'] = people[x]['balance'] - w_amount
            print(f'{w_amount} has been withrawn from your account your total balance left is {people[x]["balance"]}')
            print('')

def balance():
    print('your account your total balance left is:', {people[x]["balance"]})

funtion=input( "For withdrawl enter 1 or For balance enter 2  or For quit 3:\n")

def start():
    if(funtion == '1'):
        withdraw_money()
    elif(funtion =="2"):
        balance()
    elif(funtion=="3"):
        print("good bye")
start()


