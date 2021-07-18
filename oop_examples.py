'''
Examples from chapter 15 of Beyond the Basic Stuff for understanding OOP
Austin Richards, 7/13/21

The first example of classes uses the class WizCoin, a representation of
a fictional currency made of galleons, sickles, and knuts; all of differing
value.
'''

class WizCoinException(Exception):
    '''The WizCoin class raises this when the module is misused'''
    pass


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        '''Create a new WizCoin object with galleons, sickles, and knuts.'''
        self._galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # NOTE: __init__ methods NEVER have a return statement


    @property
    def galleons(self):
        '''Returns the number of galleons in this object.'''
        return self._galleons


    @galleons.setter
    def galleons(self, amount):
        if not isinstance(amount, int):
            raise WizCoinException('galleons attribute must be set to an int, not ' \
                + amount.__class__.__qualname__)
        if amount < 0:
            raise WizCoinException('amount must be greater than 0')
        self._galleons = amount


    @property
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


class ClassWithProperties:
    def __init__(self):
        self.someAttribute = 'some initial value'

    @property
    def someAttribute(self): # This is the "getter" method.
        print('Getter method used.')
        return self._someAttribute

    @someAttribute.setter
    def someAttribute(self, value): # This is the "setter" method.
        print('Setter method used.')
        self._someAttribute = value

    @someAttribute.deleter
    def someAttribute(self): # This is the "deleter" method.
        print('Deleter method used.')
        del self._someAttribute


def main():
    purse = WizCoin(1, 2, 3)
    print(purse.galleons)
    purse.galleons = 5
    print(purse.galleons)


if __name__ == '__main__':
    main()