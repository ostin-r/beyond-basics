'''
Austin Richards 6/19/21

esoteric_gotchas.py is a collection of more nuanced gotchas
copied from chapter 9 of the textbook.
'''

def preallocated_integers():
    '''
    In order to save time, the integers between -5 and 256
    are created at the start of a python program.  Hence,
    any variables created with the same number within this
    range and compared with the "is" operator will return 
    True.  False will be returned for any numbers outside
    this range because new objects are created for them.
    '''
    a = 0
    b = 0
    print(f'a is b: {a is b}')

    # TODO figure out why this doesn't happen in vscode
    c = 12
    d = 12
    print(f'c is d: {c is d}')


def main():
    preallocated_integers()

if __name__ == '__main__':
    main()