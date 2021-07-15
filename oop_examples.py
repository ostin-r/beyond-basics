'''
Examples from chapter 15 of Beyond the Basic Stuff for understanding OOP
Austin Richards, 7/13/21

The first example of classes uses the class WizCoin, a representation of
a fictional currency made of galleons, sickles, and knuts; all of differing
value.
'''

class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        '''Create a new WizCoin object with galleons, sickles, and knuts.'''
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # NOTE: __init__ methods NEVER have a return statement

    def value(self):
        '''The value in knuts of all the coins in this WizCoin object.'''
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weight(self):
        '''Returns the weight of the coins in grams'''
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)


class BankAccount:
    def __init__(self, account_holder):
        # Bank account methods can access self._balance, but code outside this
        # class should not.
        self._balance = 0
        self._name = account_holder
        with open(self._name + 'Ledger.txt', 'w') as ledger_file:
            ledger_file.write('Balance is 0\n')

    
    def deposit(self, amount):
        if amount <= 0:
            return # Negative deposits are not valid
        self._balance += amount
        with open(self._name + 'Ledger.txt', 'a') as ledger_file:
            ledger_file.write(f'Deposit is {str(amount)}\n')
            ledger_file.write(f'Balance is {self._balance}\n')

    
    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return
        self._balance -= amount
        with open(self._name + 'Ledger.txt', 'a') as ledger_file:
            ledger_file.write(f'Withdrawal is {str(amount)}\n')
            ledger_file.write(f'Balance is {self._balance}\n')


def main():
    # The following creates a bank account ledger file and tracks deposits/withdrawals
    account = BankAccount('Austin')
    account.deposit(100)
    account.withdraw(12)


if __name__ == '__main__':
    main()