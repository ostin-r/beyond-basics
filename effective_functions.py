'''
Austin Richards 6/21/21

effective_functions.py contains examples from chapter 10:
Writing Effective Functions
'''

def star_example():
    '''
    An example of how * can be used to pass multiple arguments to a function,
    and how ** can be used to pass multiple key-value pairs as keyword arguments.
    '''
    foods = ['oranges', 'tacos', 'almonds']
    print(foods)
    print(*foods)

    kwargs_for_print = {'sep':'-'}
    print(*foods, **kwargs_for_print)


def product(*args):
    '''
    An example of a variadic function that outputs the product
    of any amount of numbers using *.
    '''
    result = 1
    for number in args:
        result *= number
    return result


def my_min_function(*args):
    '''
    An example of a function that can take both multiple arguments
    and a single list as an argument.
    '''
    if len(args) == 0:
        raise ValueError('my_min_function() args is an empty sequence')
    elif len(args) == 1:
        print(args[0])
        return args[0]
    else:
        values = args

    smallest_value = float('-inf')

    for i, value in enumerate(values):
        if i == 0 or value < smallest_value:
            smallest_value = value
    
    print(smallest_value)
    return smallest_value


def element_function(**kwargs):
    '''
    An example of using keyword arguments to make a function
    more readable (as opposed to doing many arguments by default)

    This example creates molecules when the user passes individual
    atoms to the function.
    '''
    if kwargs['hydrogen'] == 2 and kwargs['oxygen'] == 1:
        return 'water'


def print_lower(*args, **kwargs):
    '''
    An example of using *args and **kwargs to create a
    "wrapper function" that sends arguments to another function
    that does most of the work.

    This function lowers the case of all string arguments
    and still allows the user to pass keyword arguments that are
    then handed over to print().
    '''
    args = list(args)
    for i, value in enumerate(args):
        args[i] = value.lower()
    
    return print(*args, **kwargs)


total_count = 0 # global for add_to_total

def add_to_total(amount):
    '''
    Just one example of a function with "side effects"- any effects
    that are created by the function outside of it's own code.

    This function modifies a global variable, total_count
    '''
    global total_count
    total_count += amount
    return total_count


def call_it_twice(func, *args, **kwargs):
    '''
    call_it_twice is an example of a higher order function that
    is used to execute another function twice.
    '''
    func(*args, **kwargs)
    func(*args, **kwargs)


def lambda_functions():
    '''
    A couple ways lambda functions can be used.
    '''
    rectangle_area = lambda side: side[0] * side[1]
    print(rectangle_area([12, 14]))

    # lambda functions are also commonly used to be passed to other functions
    rectangles = [[1, 2], [3, 4], [82, 2], [5, 8], [9, 3]]
    rects_sorted = sorted(rectangles, key=lambda side: side[0] * side[1])
    print(rects_sorted)


def type_hinting(number: int, name: str) -> str:
    '''
    Type hinting is cool!
    '''
    spam: list = [1, 3, 5]

    number += 1
    return name + 'a'


def main():
    pass

if __name__ == '__main__':
    main()