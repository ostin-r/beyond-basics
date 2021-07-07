'''
Austin Richards 6/28/21

performance.py includes examples of the timeit and cProfile
modules in addition to some examples of determining the 
time complexity of functions.
'''
import timeit
import cProfile
from typing import List

# global variables -----------
spam = 'yes'
# ----------------------------


def timeit_example():
    '''
    Some fun examples of the testing the timing of small snipets
    using the timeit module.
    '''

    print('time to switch variables with XOR:')
    s = 'a, b = 5, 10; a = a ^ b; b = a ^ b; a = a ^ b'
    print(timeit.timeit(s))

    print('time to switch variables with a third variable:')
    s = 'a, b = 5, 10; temp = a; a = b; temp = b'
    print(timeit.timeit(s))

    print('time to switch variables by iterable unpacking:')
    s = 'a, b = 5, 10; a, b = b, a'
    print(timeit.timeit(s))

    print('Time to generate 10,000,000 random numbers from 1 & 100')
    print(timeit.timeit('random.randint(1,100)', 'import random', number=10000000))

    print('Time to print a string:')
    print(timeit.timeit('print(spam)', number=1, globals=globals()))


def add_numbers():
    '''
    A test function for doing an example of the cProfile module.
    '''
    total = 0
    for i in range(1, 1000001):
        total += 1


def cprofile_example():
    '''
    An example of using cprofile.run() to profile the add_numbers function
    '''
    cProfile.run('add_numbers()')


def main():
    reading_list(['hello', 'austin'])

if __name__ == '__main__':
    main()