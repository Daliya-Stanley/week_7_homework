from account_hierarchy.insufficient_funds import InsufficientFundsException

class Account:
    # Constructor method to initialize the account with an initial balance, first name, and last name.
    def __init__(self, initial_amount, firstname, lastname):
        self.__balance = initial_amount  # balance is created by us, it is the attribute we are going to change /access in the background
        self.firstname = firstname
        self._lastname = lastname

    # this is called a GETTER - ITS JOB ITS TO GET THE DATA INSIDE THE OBJECT
    def get_balance(self):
        return self.__balance  # as has two __ means that balance is going to be private

    def get_firstname(self):
        return self.firstname  # not having the __ makes it a public field and could be changed from the client

    def get_lastname(self):
        return self._lastname

    # Special method that defines the string representation of the object when printed
    def __str__(self):
        return f"Bank Account Holder: {self.firstname} {self._lastname}\nHas balance: £{self.__balance}"

    # Setter method to update the last name with validation to ensure it's alphabetic.
    def set_lastname(self, lastname):
        if str(lastname).isalpha():
            self._lastname = lastname
        else:
            raise ValueError("Lastname must be alphabetic")  # instantiation

    # Setter method to update the first name with validation to ensure it's alphabetic.
    def set_firstname(self, firstname):
        if str(firstname).isalpha():
            self._lastname = firstname
        else:
            raise ValueError("Firstname must be alphabetic")  # instantiation

        # setters often VALIDATE DATA
        # getters often TRANSLATE DATA

    # behavioural methods
    # Deposit method to increase the balance by a specified amount.
    def deposit(self, amount):
        self.__balance += amount # Increase the private balance attribute by the specified deposit amount

    # Withdraw method to decrease the balance by a specified amount, if sufficient funds are available
    def withdraw(self, amount):
        if amount <= self.__balance: # Check if the withdrawal amount is less than or equal to the current balance
            self.__balance -= amount # Decrease the private balance attribute by the withdrawal amount
        else:
            # If insufficient funds, create an instance of InsufficientFundsException and return the error message.
            x = InsufficientFundsException('This is an error') # Create an exception instance for insufficient funds
            message = x.error_message()# Call the error_message method on the exception to get the message
            return message# Return the error message instead of raising the exception