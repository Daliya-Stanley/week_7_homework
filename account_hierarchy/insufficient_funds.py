# from account_hierarchy.account import Account

class InsufficientFundsException:
    def __init__(self, message):
        # super().__init__(initial_amount, firstname, lastname)
        self.__message = message

    def get_message(self):
        return self.__message

    def error_message(self):
        self.__message = "You don't have any overdraft arranged"
        raise ValueError(self.__message)




