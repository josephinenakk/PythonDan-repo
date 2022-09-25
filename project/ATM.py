# lets run this in loop to add atleast 2 users 
# then please modify user 1 password

import bank_actions
#print(customer_information)
while True:

    choice =int(input("\nselect below number :\n1 for add customer\n2 for update info\n3 for read account details\n4 for delete account\nEnter numner for above options:"))
    if (choice == 1):
        bank_actions.add_customer()  
    elif(choice == 2):
        bank_actions.update_customer()
    elif(choice==3):
        bank_actions.get_customer()
    elif(choice==4):
        bank_actions.delete_customer()

    else:
        print ("invlid operation")

#*********************************************************************************************