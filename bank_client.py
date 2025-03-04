from account_hierarchy.account import Account
from account_hierarchy.saving_account import SavingAccount

# Using a try block to handle potential errors that might occur during execution
try:
    ivon = SavingAccount(20000, 'Ivon', 'Kruse', 0.03)

    # Applying the fixed deposit annual interest and storing the result
    balance_after_interest = ivon.add_fd_annual_interest()
    print(balance_after_interest)

    # Depositing 30 into Ivon's account
    balance_after_deposit = ivon.deposit(30)
    print(ivon)

    # Attempting to withdraw 24,000 from the account
    balance_after_withdraw = ivon.withdraw(24000)
    print(ivon) # Printing the account details after withdrawal

# Handling a ValueError, which may occur if there are insufficient funds during withdrawal
except ValueError as ex:
    print('Sorry, but you have insufficient funds')# Error message for insufficient funds
    print(ex)

# Handling any other unexpected exceptions that may occur
except Exception as ex:
    print('Sorry, there appears to be a problem')
    print(ex)
# The finally block runs **no matter what**, even if an error occurs
finally:
    print('Thank you')



# What This Code Does:
# Creates a savings account for Ivon with a balance of £20,000 and an interest rate of 3%.
# Calculates and prints the interest earned based on the balance.
# Deposits £30 into the account and prints the updated details.
# Attempts to withdraw £24,000, which might fail if funds are insufficient.
# Handles errors:
# If the withdrawal fails due to insufficient funds, a friendly error message is shown.
# If any other unexpected error occurs, a general error message is displayed.
# Ensures the program always prints "Thank you" regardless of whether an error occurs.
