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
    this range because new objects are created for each.

    Interestingly, I could only coax this esoteric issue
    out when using the "for" loop below- notice that 
    "c is d" still yields True.  This is not the case 
    whenever I run this in a shell though.  I suspect this
    is because of a similar implementation feature to 
    string interning.
    '''
    a = 0
    b = 0
    print(f'a is b: {a is b}')

    c = 257
    d = 257
    print(f'c is d: {c is d}')

    for x, y in zip(range(256, 258), range(256, 258)):
        print(x is y)


def string_interning():
    '''
    String interning is an implementation feature that recognizes
    when the same string is assigned to a different variable.  The
    program saves space by assigning both variables to the same 
    object.
    '''
    spam = 'grass'
    eggs = 'grass'
    print(spam is eggs)


def all_of_nothing():
    '''
    Python's all() function is used to determine if all values
    within a list are truthy. However, it will still return True
    if it is passed an empty list.

    It is therefore better to describe the all() function as
    being able to tell you "there are not False values in this
    list"
    '''
    test = [21, 8, 19]
    test_boolean = [i > 22 for i in test]
    print(all(test_boolean))

    test_boolean = [i > 7 for i in test]
    print(all(test_boolean))

    print(all([]))

    # doing a list comprehension can further muddle this feature and cause bugs
    test = []
    print(all([i < 10 for i in test]))
    print(all([i > 10 for i in test]))
    print(all([i == 10 for i in test]))


def boolean_integers():
    '''
    Since True and False are both in a subclass of 
    Int, they behave in the same way that 1 (True) or
    0 (False) does.
    '''
    assert True == 1
    assert False == 0

    values = [1, 2, 3]
    print(values[True])
    print(values[False])

    print(12 * -True)
    print(12 * False)


def main():
    boolean_integers()

if __name__ == '__main__':
    main()