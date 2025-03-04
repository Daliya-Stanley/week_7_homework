# from account_hierarchy.account import Account

# Define the custom exception class InsufficientFundsException.
class InsufficientFundsException:
    # Constructor method to initialize the exception with a custom message.
    def __init__(self, message):
        # Initialize the private message attribute to store the error message.
        self.__message = message

    # Getter method to retrieve the message.
    def get_message(self):
        return self.__message

    # Method to generate an error message related to insufficient funds and raise a ValueError.
    def error_message(self):
        self.__message = "You don't have any overdraft arranged"
        raise ValueError(self.__message)




