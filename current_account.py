from account import Account

class CurrentAccount(Account):
    def __init__(self,customer_id,account_type,balance):
        super().__init__(customer_id,account_type,balance)
        

    def withdraw(self, amount):
        if amount<self._balance:
            self._balance-=amount
            return f"{amount} withdrawn! New balance: {self._balance}"
        else:
            return f"{amount} is greater than withdraw amount limit!!!"
    
    def calculate_interest(self):
        return "There is no interest on Current Account balance"