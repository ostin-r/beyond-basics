'''
Austin Richards 6/28/21

performance.py includes examples of the timeit and cProfile
modules
'''
import timeit
import cProfile

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


def cprofile_example():
    pass


def main():
    timeit_example()

if __name__ == '__main__':
    main()