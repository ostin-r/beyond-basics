'''
Austin Richards 6/17/21

gotchas.py contains examples of common "gotchas" outlined
in Chapter 8 of the textbook "Beyond the Basic Stuff with
Python" by Al Sweigart.

I have each example defined as a function that can be run
to output statements about what went wrong and how it can 
create bugs and other problems.
'''
import copy
import time

def loop_list():
    '''
    Iterating over a list that you are modifying can result in 
    a infinite loop, or skipping over items in the list. Loops
    where a list must be modified must contain a list outside
    of the loop.

    This function contains two examples: One where adding an 
    item results in an infinite loop, and one where deleting
    an item results in items in the list being skipped.
    '''

    # Example 1: Infinite Loop
    clothes = ['shirt', 'red sock', 'shorts']
    i = 0
    for item in clothes:
        if 'sock' in item:
            clothes.append(item) 
            print(clothes)
        
        # counter to break the infinite loop
        if i > 7:
            break
        i += 1


    # Example 1 Solution
    print('\nThis can be fixed by modifying a separate list outside of the loop:')
    clothes = ['shirt', 'red sock', 'shorts']
    new_clothes = []
    for item in clothes:
        if 'sock' in item:
            new_clothes.append(item)

    clothes.extend(new_clothes)
    
    print(f'separate list ={new_clothes}')
    print(f'appended list ={clothes}\n')


    # Example 2: Skipped Index
    fruits = ['apple', 'banana', 'orange', 'apple', 'apple']
    print(f'Original list = {fruits}')

    for i, fruit in enumerate(fruits):
        if fruit != 'apple':
            del fruits[i]
    print(fruits)

    # Example 2 Solution
    fruits = ['apple', 'banana', 'orange', 'apple', 'apple']
    apples = []
    for i, fruit in enumerate(fruits):
        if fruit == 'apple':
            apples.append(fruit)
    print(apples)
    

    # Example 2 Solution, #2
    apples = [fruit for fruit in fruits if fruit == 'apple']
    print(apples)


def copy_mutables():
    '''
    Copying a mutable using only assignment (=) can yield many 
    bugs- the python module copy is equipped with copy and 
    deepcopy for avoiding this.  Displayed here are some of the
    pitfalls of copying mutable objects:
    '''

    # Example 1: Modification of Original List
    test = ['orange', 'apple', 'water bottle']
    test_copy = test
    test_copy[2] = 'soda pop'
    print(test, test_copy)

    # Example 1 Solution - copy.copy()
    test = ['orange', 'apple', 'water bottle']
    test_copy = copy.copy(test)
    test_copy[2] = 'soda pop'
    print(test, test_copy)

    # Example 2: Modification of Original List within List
    test = [[1, 2], [4, 8], 'hello']
    test_copy = copy.copy(test)
    test_copy[1][0] = 5
    print(test, test_copy)

    # Example 2 Solution - copy.deepcopy()
    test = [[1, 2], [4, 8], 'hello']
    test_copy = copy.deepcopy(test)
    test_copy[1][0] = 5
    print(test, test_copy)


def add_item_bad(item, items = ['mop', 'bucket']):
    '''
    Setting mutable items for default agruments can lead to
    bugs because the list will be created in the def statement
    and will continue to be referenced and modified every time
    the function is called.  Instead of returning a new list 
    when the function is called, the list just keeps getting
    bigger.
    '''
    items.insert(1, item)
    return items


def add_item_good(item, items = None):
    '''
    A solution to add_item_bad setting a default argument as a list.
    '''
    if items is None:
        items = ['mop', 'bucket']
    items.insert(1, item)
    return items


def test_add_item():
    '''
    An illustration of add_item_bad (bad example) and add_item_good (good example)
    '''
    # the list initialized in add_item_bad is continually referenced and a new list is not created
    first_cleaning_items = add_item_bad('cloth')
    print(first_cleaning_items)

    second_cleaning_items = add_item_bad('towel')
    print(second_cleaning_items)

    # a new list is created for each new assignment of first_cleaning_items, second_cleaning_items
    first_cleaning_items = add_item_good('cloth')
    print(first_cleaning_items)

    second_cleaning_items = add_item_good('towel')
    print(second_cleaning_items)


def string_concatenate():
    '''
    Building strings through concatenation is usually not a problem
    on a small scale.  However, since one is creating an entirely
    new string object whenever concatenation is used (and it is then
    immediately discarded on the next iteration), this creates much more
    work for the CPU than is necessary.

    Note: I found that this was only significant for list lengths above
    1 million items for my machine.
    '''
    LIST_LENGTH = 1000000

    concatenate_start = time.time()
    final_string = ''

    for i in range(LIST_LENGTH):
        final_string += 'hello '

    concatenate_finish = time.time()

    concatenate_time = concatenate_finish - concatenate_start
    print(f'time to concatenate 1,000,000 strings = {concatenate_time} s')

    # Solution: create a list to store items in then use .join() to convert to string
    append_start = time.time()
    final_string = []

    for i in range(LIST_LENGTH):
        final_string.append('hello')

    final_string = ' '.join(final_string)
    append_finish = time.time()

    append_time = append_finish - append_start
    print(f'time to append and join 1,000,000 strings = {append_time} s')
    print(f'Appending and joining is {round(concatenate_time/append_time, 3)} times faster')


def main():
    string_concatenate()


if __name__ == '__main__':
    main()
