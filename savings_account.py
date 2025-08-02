from account import Account

class SavingsAccount(Account):
    interest_rate=0.1
    withdraw_amount_limit=60000
    def __init__(self,customer_id,account_type,balance):
        super().__init__(customer_id,account_type,balance)
        

    def withdraw(self, amount):
        if amount<self._balance:
            if amount<SavingsAccount.withdraw_amount_limit:
                self._balance-=amount
                return f"{amount} withdrawn! New balance: {self._balance}"
            else:
                return f"{amount} is greater than withdraw amount limit!!!"
        else:
            return "Amount is greater than balance!!!"
        
    def calculate_interest(self):
        return  f"Interest Amount:{self.balance*0.1}"