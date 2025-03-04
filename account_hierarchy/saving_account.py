from account_hierarchy.account import Account

# a savings account IS A KIND OF account
# SavingAccount class inherits from Account class
class SavingAccount(Account):
    def __init__(self, initial_amount, firstname, lastname, annual_interest_rate):
        super().__init__(initial_amount, firstname, lastname)
        self.__fd_annual_interest_rate = annual_interest_rate

    # getters and setters for new parameter in class (annual interest rate)
    def get_annual_interest_rate(self):
        return self.__fd_annual_interest_rate

    def set_annual_interest_rate(self, annual_interest_rate):
            self.__fd_annual_interest_rate = annual_interest_rate

    # behaviour
    # calculating what your interest on your fixed deposit will be
    def add_fd_annual_interest(self):
        #.get_balance() method inherited from Account class
        balance = self.get_balance()
        balance = balance * self.__fd_annual_interest_rate
        return f"Your fixed deposit interest earned is £{balance:.2f}, if the balance remain same over a period of 12 months! "


