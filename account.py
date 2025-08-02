from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self,customer_id,account_type,balance):
        self.__customer_id=customer_id
        self.__account_type=account_type
        self._balance = balance

    @property
    def customer_id(self):
        return self.__customer_id
    @property
    def account_type(self):
        return self.__account_type
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def get_balance(self,value):
        self._balance=value

    def deposit(self,amount):
        self._balance+=amount

    def get_balance(self):
        return self.balance
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def calculate_interest(self):
        pass
