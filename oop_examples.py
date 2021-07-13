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