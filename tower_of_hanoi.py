'''
A practice project by Al Sweigart- copied from Chapter 14 of 
Beyond the Basics with Python.  This is an exercise in understanding
the structure of typical OOP programs.

TOWER OF HANOI, a stack-moving puzzle game
'''

import copy
import sys

TOTAL_DISKS = 5 # More disks means a more difficult puzzle

# Start with all the disks on tower A
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))

def main():
    pass


def get_player_move(towers: list) -> list:
    '''Asks the player for a move. Returns (from_tower, to_tower).'''

    while True: # Keep asking the player until they enter a valid move.
        print('Enter the letters of "from" tower and "To" tower, or QUIT')
        print('(e.g., AB moves a disk from tower A to tower B.')
        print()
        response = input('> ').upper().strip()

        if response == "QUIT":
            print('Thanks for playing!')
            sys.exit()

        # Make sure the response is valid.
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of the following: AB, AC, BA, BC, CA, CB')
            continue

        # Switch to more descriptive response names.
        from_tower, to_tower = response[0], response[1]

        if len(towers[from_tower]) == 0:
            # The "from" tower cannot be empty.
            print('You selected a tower with no disks.')
            continue
        elif len(towers[to_tower]) == 0:
            return from_tower, to_tower
        elif towers[to_tower][-1] < towers[from_tower][-1]:
            print("You can't put larger disks on top of smaller ones.")
            continue
        else:
            # This is a valid move, so return the selected towers:
            return from_tower, to_tower


def display_towers(towers: list) -> None:
    '''Display the three towers and their disks.'''

    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                display_disk(0) # Display the bare pole.
            else:
                display_disk(tower[level]) # Display the disk.
        print()

    # Display the tower labels: A, B, and C.
    empty_space = ' ' * TOTAL_DISKS
    print('{0} A{0}{0} B{0}{0} C\n'.format(empty_space))


def display_disk(width: int) -> None:
    '''Display the disk of a given width. A width of 0 means no disk.'''
    empty_space = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        # display the section of the pole without a disk
        print(f'{empty_space}||{empty_space}', end='')

    else:
        # display the disk with a number label
        disk = "@" * width
        number_label = str(width).rjust(2, '_')
        print(f'{empty_space}{disk}{number_label}{disk}{empty_space}', end='')


if __name__ == '__main__':
    main()