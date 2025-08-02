import csv
from fixed_account import FixedAccount
from savings_account import SavingsAccount
from current_account import CurrentAccount


class UserMenu:
    def __init__(self):
        self.perform_actions()

    def perform_actions(self):
        while True:
            userReply = input("""\nWHAT ACTION DO YOU WANT TO PERFORM?
1 ==> WITHDRAW AMOUNT
2 ==> DEPOSIT AMOUNT
3 ==> CALCULATE INTEREST
4 ==> LOG OUT\n""")

            if userReply == '4':
                print("See you later!!")
                break

            customer_id = input("Enter Customer ID: ").strip()
            account_type = input("Enter account type (savings/current/fixed): ").lower().strip()

            # Load account from CSV
            with open("accounts.csv", 'r') as f:
                reader = csv.DictReader(f)
                accounts = list(reader)

            found = False
            for row in accounts:
                if row["Customer_ID"] == customer_id and row["Account_type"].lower() == account_type:
                    balance = float(row["Balance"])
                    found = True

                    # Create the correct account object
                    if account_type == "fixed":
                        account = FixedAccount(customer_id, "Fixed", balance)
                    elif account_type == "savings":
                        account = SavingsAccount(customer_id, "Savings", balance)
                    elif account_type == "current":
                        account = CurrentAccount(customer_id, "Current", balance)
                    else:
                        print("Invalid account type.")
                        return

                    # Handle user action
                    if userReply == '1':  # Withdraw
                        if account_type == "fixed":
                            year = int(input("Enter years passed: "))
                            amount = float(input("Enter amount to withdraw: "))
                            print(account.withdraw(amount, year))
                        else:
                            amount = float(input("Enter amount to withdraw: "))
                            print(account.withdraw(amount))

                    elif userReply == '2':  # Deposit
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                        print(f"New balance: {account.get_balance()}")

                    elif userReply == '3':  # Calculate Interest
                        print(f"Interest: {account.calculate_interest()}")

                    # Update CSV (after 1, 2 if balance is changed)
                    if userReply in ['1', '2']:
                        for row_to_update in accounts:
                            if row_to_update["Customer_ID"] == customer_id and row_to_update["Account_type"].lower() == account_type:
                                row_to_update["Balance"] = str(account.get_balance())

                        with open("accounts.csv", 'w', newline='') as f:
                            fieldnames = ["Customer_ID", "Account_type", "Balance"]
                            writer = csv.DictWriter(f, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(accounts)

                    break  # Stop after processing one valid account

            if not found:
                print("Account not found.")
