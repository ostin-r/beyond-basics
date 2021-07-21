"""
Examples from chapter 15 of Beyond the Basic Stuff for understanding OOP
Austin Richards, 7/13/21

The first example of classes uses the class WizCoin, a representation of
a fictional currency made of galleons, sickles, and knuts; all of differing
value.
"""
import collections.abc
import operator

class WizCoinException(Exception):
    """The WizCoin class raises this when the module is misused"""
    pass


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # NOTE: __init__ methods NEVER have a return statement

    @property
    def galleons(self):
        """Returns the number of galleons in this object."""
        return self._galleons

    @galleons.setter
    def galleons(self, amount):
        if not isinstance(amount, int):
            raise WizCoinException(
                "galleons attribute must be set to an int, not "
                + amount.__class__.__qualname__
            )
        if amount < 0:
            raise WizCoinException("amount must be greater than 0")
        self._galleons = amount

    @property
    def value(self):
        """The value in knuts of all the coins in this WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weight(self):
        """Returns the weight of the coins in grams"""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

    def _comparison_operator_helper(self, operator_function, other):
        """A helper method for our comparison dunder methods."""
        if isinstance(other, WizCoin):
            return operator_function(self.value, other.value)
        elif isinstance(other, (int, float)):
            return operator_function(self.value, other)
        elif isinstance(other, collections.abc.Sequence):
            other_value = (other[0] * 17 * 29 + other[1] * 29 + other[2])
            return operator_function(self.value, other_value)
        elif operator_function == operator.eq:
            return False
        elif operator_function == operator.ne:
            return True
        else:
            return NotImplemented

    def __eq__(self, other): # Equal operator
        return self._comparison_operator_helper(operator.eq, other)

    def __ne__(self, other): # ne is "Not Equal"
        return self._comparison_operator_helper(operator.ne, other)

    def __lt__(self, other): # lt is "Less Than"
        return self._comparison_operator_helper(operator.lt, other)

    def __le__(self, other): # le is "Less than or Equal"
        return self._comparison_operator_helper(operator.le, other)

    def __gt__(self, other): # gt is "Greater Than"
        return self._comparison_operator_helper(operator.gt, other)

    def __ge__(self, other): # ge is "Greater than or Equal"
        return self._comparison_operator_helper(operator.ge, other)

    def __repr__(self):
        """Returns a string of an expression that recreates this object."""
        return f"{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})"

    def __str__(self):
        """Returns a human readable string representation of this object."""
        return f"{self.galleons}g, {self.sickles}s, {self.knuts}k"

    def __add__(self, other):
        """Adds the coins in WizCoin objects."""
        if not isinstance(other, WizCoin):
            return NotImplemented

        return WizCoin(
            other.galleons + self.galleons,
            other.sickles + self.sickles,
            other.knuts + self.knuts,
        )

    def __sub__(self, other):
        """Subtracts the coins in WizCoin objects."""
        if not isinstance(other, WizCoin):
            return NotImplemented

        return WizCoin(
            self.galleons - other.galleons,
            self.sickles - other.sickles,
            self.knuts - other.knuts,
        )

    def __mul__(self, number):
        """Multiplies each coin type by the given non-negative integer."""
        if not isinstance(number, int):
            return NotImplemented
        if number < 0:
            raise WizCoinException('Cannot multiply by negative numbers')

        return WizCoin(
            self.galleons * number,
            self.sickles * number,
            self.knuts * number
        )

    def __rmul__(self, number):
        """Multiplies the coin amounts by the given non-negative integer"""
        return self.__mul__(number)

    def __bool__(self):
        if self.galleons == 0 and self.sickles == 0 and self.knuts == 0:
            return False
        return True

    def __iadd__(self, other):
        """Add the amounts in another WizCoin object to another"""
        if not isinstance(other, WizCoin):
            return NotImplemented
        
        # The self object is modified in place here
        self.galleons += other.galleons
        self.sickles += other.sickles
        self.knuts += other.knuts
        return self # in-place dunder methods (almost) always return self.

    def __imul__(self, number):
        """Multiply the amount of all coins in this object."""
        if not isinstance(number, int):
            return NotImplemented
        if number < 0:
            return WizCoinException('Cannot multiply by negative numbers')

        self.galleons *= number
        self.sickles *= number
        self.knuts *= number
        return self


class BankAccount:
    def __init__(self, account_holder):
        # Bank account methods can access self._balance, but code outside this
        # class should not.
        self._balance = 0
        self._name = account_holder
        with open(self._name + "Ledger.txt", "w") as ledger_file:
            ledger_file.write("Balance is 0\n")

    def deposit(self, amount):
        if amount <= 0:
            return  # Negative deposits are not valid
        self._balance += amount
        with open(self._name + "Ledger.txt", "a") as ledger_file:
            ledger_file.write(f"Deposit is {str(amount)}\n")
            ledger_file.write(f"Balance is {self._balance}\n")

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return
        self._balance -= amount
        with open(self._name + "Ledger.txt", "a") as ledger_file:
            ledger_file.write(f"Withdrawal is {str(amount)}\n")
            ledger_file.write(f"Balance is {self._balance}\n")


def main():
    purse = WizCoin(19, 19, 221)
    tip_jar = WizCoin(1, 0, 0)
    print(purse - tip_jar)


if __name__ == "__main__":
    main()
