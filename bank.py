from customer import Customer
from savings_account import SavingsAccount
from fixed_account import FixedAccount
from current_account import CurrentAccount
import csv
import os  # <== Needed to check file existence and size


class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []
        self.run()

    def run(self):
        while True:
            action = input("""What action do you want to perform?\n
1 ==> ADD CUSTOMER
2 ==> REMOVE CUSTOMER
3 ==> FIND CUSTOMER
4 ==> ADD ACCOUNT
5 ==> LOG OUT\n""").strip()

            if action == '1':
                self.add_customer()
            elif action == '2':
                self.remove_customer()
            elif action == '3':
                self.find_customer()
            elif action == '4':
                self.add_account()
            elif action == '5':
                print("See you later!!!")
                break
            else:
                print("OOPS!! That doesn't seem right.")

    def add_customer(self):
        name = input("Enter customer name: ").lower().strip()
        email = input("Enter email address: ").lower().strip()
        phone = input("Enter phone: ").strip()

        customer = Customer(name, email, phone)
        self.customers.append(customer)

        file_path = 'customers.csv'
        file_exists = os.path.exists(file_path)
        is_empty = os.stat(file_path).st_size == 0 if file_exists else True

        with open(file_path, 'a', newline='') as f:
            fieldnames = ['Name', 'Email', 'Phone', 'Customer_ID']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if is_empty:
                writer.writeheader()
            writer.writerow({
                'Name': customer.name,
                'Email': customer.email,
                'Phone': customer.phone,
                'Customer_ID': customer.customer_id
            })

        print("Customer added successfully!")

    def remove_customer(self):
        id = input("Enter customer ID to remove: ").strip()
        self.customers = [c for c in self.customers if c.customer_id != id]

        with open('customers.csv', 'r') as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader if row['Customer_ID'] != id]

        with open('customers.csv', 'w', newline='') as f:
            fieldnames = ['Name', 'Email', 'Phone', 'Customer_ID']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print("Customer removed if ID existed.")

    def find_customer(self):
        id = input("Enter customer ID: ").strip()
        with open('customers.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Customer_ID'] == id:
                    print("Customer Found:")
                    print(row)
                    return
        print("Customer not found.")

    def add_account(self):
        customer_id = input("Enter customer ID: ").strip()
        account_type = input("Enter account type (savings/current/fixed): ").lower().strip()

        account = None

        if account_type == "savings":
            balance = float(input("Enter balance:"))
            account = SavingsAccount(customer_id, "Savings",balance)
        elif account_type == "current":
            balance = float(input("Enter balance:"))
            account = CurrentAccount(customer_id, "Current",balance)
        elif account_type == "fixed":
            balance = float(input("Enter amount to be fixed over the period of 12 years: "))
            account = FixedAccount(customer_id, "Fixed", balance)
        else:
            print("Wrong account type!!!")
            return  # Exit without saving

        self.accounts.append(account)

        file_path = 'accounts.csv'
        file_exists = os.path.exists(file_path)
        is_empty = os.stat(file_path).st_size == 0 if file_exists else True

        with open(file_path, 'a', newline='') as f:
            fieldnames = ['Customer_ID', 'Account_type','Balance']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if is_empty:
                writer.writeheader()
            writer.writerow({
                'Customer_ID': account.customer_id,
                'Account_type': account.account_type,
                'Balance': account.balance
            })

        print("Account added successfully!")

