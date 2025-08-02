import csv


class Customer:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__customer_id = Customer.generate_customer_id()

    @property
    def name(self):
        return self.__name
    @property
    def email(self):
        return self.__email
    @property
    def phone(self):
        return self.__phone
    @property
    def customer_id(self):
        return self.__customer_id
    @staticmethod
    def generate_customer_id():
        max_id = 0
        with open('customers.csv', 'r')as f:
            reader = csv.DictReader(f)

            for row in reader:
                max_id = max(max_id, int(row['Customer_ID']))
            return max_id+1
