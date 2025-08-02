from account import Account

class FixedAccount(Account):
    interest_rate=0.25
    year = 12

    def __init__(self,customer_id,account_type,balance):
        super().__init__(customer_id,account_type,balance)
       
     
    def withdraw(self, amount,year_passed):
       if year_passed>=12:
           interest_amount=self.calculate_interest()
           self.balance+=interest_amount
           if amount<=self._balance:
               print(f"{amount} withdrawed!!!")
               self.balance-=amount
       else:
            return f"You can't withdraw amount from fixed account before {FixedAccount.year} years"
        
    def calculate_interest(self):
        return  f"Interest Amount:{self.balance*FixedAccount.interest_rate*FixedAccount.year}"