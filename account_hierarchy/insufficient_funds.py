# from account_hierarchy.account import Account

# doesn't inherit from another class
class InsufficientFundsException:
    def __init__(self, message):
        # super().__init__(initial_amount, firstname, lastname)
        self.__message = message

    # getter
    def get_message(self):
        return self.__message

    # function
    def error_message(self):
        self.__message = "You don't have any overdraft arranged"
        raise ValueError(self.__message)
# when ValueError is raised, this message is returned
# we use this in the account class




