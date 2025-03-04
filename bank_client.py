from account_hierarchy.account import Account
from account_hierarchy.saving_account import SavingAccount

# try block
try:
    ivon = SavingAccount(20000, 'Ivon', 'Kruse', 0.03)

    # using new method from SavingAccount class - calculating annual interest on fixed deposit
    calculated_interest = ivon.add_fd_annual_interest()
    print(calculated_interest)

    # deposit and withdraw inherited from Account class
    balance_after_deposit = ivon.deposit(30)
    print(ivon)

    balance_after_withdraw = ivon.withdraw(24000)
    print(ivon)

except ValueError as ex:
    print('Sorry, but you have insufficient funds')
    print(ex)
except Exception as ex:
    print('Sorry, there appears to be a problem')
    print(ex)

finally:
    print('Thank you')




