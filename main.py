from bank import Bank
from user_menu import UserMenu

while True:
    reply = input("Logging as:\nAdmin==>1\nCustomer==>2\nLog out==>3\n")

    if reply == '1':
        password = input("Enter Password: ")
        if password == '123':
            Bank()
            break
        else:
            print("Incorrect password")
    elif reply == '2':
        UserMenu()
        break
    else:
        print("Incorrect option")
