'''
Austin Richards 6/17/21

gotchas.py contains examples of common "gotchas" outlined
in Chapter 8 of the textbook "Beyond the Basic Stuff with
Python" by Al Sweigart.

I have each example defined as a function that can be run
to output statements about what went wrong and how it can 
create bugs and other problems.
'''

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

    # EXAMPLE 1 - Infinite loop
    print('Incorrectly adding to list while looping results in:')
    clothes = ['shirt', 'red sock', 'shorts']
    i = 0
    for item in clothes:
        if 'sock' in item:
            clothes.append(item)
            print(clothes)
        
        # counter to break the infinite loop...
        if i > 7:
            break
        i += 1

    print('\nThis can be fixed by modifying a separate list outside of the loop:')
    clothes = ['shirt', 'red sock', 'shorts']
    new_clothes = []
    for item in clothes:
        if 'sock' in item:
            new_clothes.append(item)

    clothes.extend(new_clothes)
    
    print(f'separate list ={new_clothes}')
    print(f'appended list ={clothes}\n')

    # EXAMPLE 2 - Skipped Items



def main():
    loop_list()


if __name__ == '__main__':
    main()
