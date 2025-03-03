from account_hierarchy.insufficient_funds import InsufficientFundsException

class Account:
    # this is a CONSTRUCTOR
    def __init__(self, initial_amount, firstname, lastname):
        self.__balance = initial_amount  # balance is created by us, it is the attribute we are going to change /acces in the background
        self.firstname = firstname
        self._lastname = lastname

    # this is called a GETTER - ITS JOB ITS TO GET THE DATA INSIDE THE OBJECT
    def get_balance(self):
        return self.__balance  # as has two __ means that balance is going to be private

    def get_firstname(self):
        return self.firstname  # not having the __ makes it a public field and could be changed from the client

    def get_lastname(self):
        return self._lastname


    def __str__(self):
        return f"Bank Account Holder: {self.firstname} {self._lastname}\nHas balance: £{self.__balance}"



    #   best practice put __ to everything, making it readable only and then create a setter if you want it to be writeable
    #   setters write to data

    def set_lastname(self, lastname):
        if str(lastname).isalpha():
            self._lastname = lastname
        else:
            raise ValueError("Lastname must be alphabetic")  # instantiation

    def set_firstname(self, firstname):
        if str(firstname).isalpha():
            self._lastname = firstname
        else:
            raise ValueError("Firstname must be alphabetic")  # instantiation

        # setters often VALIDATE DATA
        # getters often TRANSLATE DATA

    # behavioural methods
    def deposit(self, amount):
        self.__balance += amount


    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            # raise ValueError('Insufficient funds')
            # return InsufficientFundsException.error_message(self.firstname)
            x = InsufficientFundsException('This is an error')
            message = x.error_message()
            return message