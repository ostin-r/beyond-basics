'''
Four-in-a-Row, by Al Sweigart al@inventwithpython.com
A tile-dropping game to get four in a row.  Similar to Connect Four.
'''

import sys

# Constants for displaying the board.
EMPTY_SPACE = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'

# Note: Update BOARD_TEMPLATE and COLUMN_LABELS if BOARD_WIDTH is changed.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABELS) == BOARD_WIDTH

# The template string for displaying the board:
BOARD_TEMPLATE = '''
1234567
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
+-------+
'''

def main():
    pass


def is_winner(player_tile, board):
    '''
    Returns True if player_tile contains four tiles in a row on 
    board.  Returns False otherwise.
    '''
    pass




# If this program was run instead of imported, play the game:
if __name__ == '__main__':
    main()