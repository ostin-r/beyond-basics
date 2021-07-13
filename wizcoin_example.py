'''
An example of creating a WizCoin object from a separate file.

The source file four this is oop_examples.py
'''
import oop_examples as wizcoin

purse = wizcoin.WizCoin(2, 8, 25)
print(f'Total Value: {purse.value()} knuts')
print(f'Total Weight: {purse.weight()} grams')