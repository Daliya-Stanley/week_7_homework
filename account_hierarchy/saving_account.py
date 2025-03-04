from account_hierarchy.account import Account

# a savings account IS A KIND OF account
# Defining the SavingAccount class, which is a subclass of Account.
# This means SavingAccount inherits all properties and methods from the Account class.
class SavingAccount(Account):
    # Constructor (__init__) to initialize a new savings account.
    # It takes an initial deposit amount, first and last name of the account holder,
    # and the annual interest rate.
    def __init__(self, initial_amount, firstname, lastname, annual_interest_rate):
        # Calling the parent class (Account) constructor to initialize common attributes.
        super().__init__(initial_amount, firstname, lastname)
        # Private attribute to store the annual interest rate for the fixed deposit.
        self.__fd_annual_interest_rate = annual_interest_rate

    # Getter method to retrieve the annual interest rate.
    def get_annual_interest_rate(self):
        return self.__fd_annual_interest_rate

    # Setter method to update the annual interest rate.
    def set_annual_interest_rate(self, annual_interest_rate):
            self.__fd_annual_interest_rate = annual_interest_rate

    # Method to calculate and return the interest earned on the current balance if it remains unchanged for a year.
    def add_fd_annual_interest(self):
        # Get the current balance from the parent Account class.
        balance = self.get_balance()
        # Calculate the fixed deposit interest based on the annual interest rate
        balance = balance * self.__fd_annual_interest_rate
        # Return a formatted string displaying the interest earned over 12 months.
        return f"Your fixed deposit interest earned is £{balance:.2f}, if the balance remain same over a period of 12 months! "

#
# Inheritance: SavingAccount extends Account, meaning it inherits its methods and attributes.
# Encapsulation: The annual interest rate is stored as a private attribute (__fd_annual_interest_rate).
# Getter & Setter Methods: These allow controlled access to the private annual interest rate.
# Interest Calculation: add_fd_annual_interest() calculates how much interest would be earned over a year if the balance remains unchanged.git 