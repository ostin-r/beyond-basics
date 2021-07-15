'''
An example of using OOP principles to make a simple game
of tic tac toe.
'''

ALL_SPACES = list('123456789') # The keys for the game board.
X, O, BLANK = 'X', 'O', ' ' # Constants for string values.

def main():
    '''Runs a game of tic tac toe.'''
    print('Welcome to tic tac toe!')
    game_board = GameBoard() # Create a TTT board object
    current_player, next_player = X, O # X starts the game

    while True:
        print(game_board.get_board_string())

        # Keep asking the player to enter a number 1-9.
        move = None
        while not game_board.is_valid_space(move):
            print(f'Enter move for {current_player}. (1-9)')
            move = str(input('>>> '))
        game_board.update_board(move, )



class GameBoard:
    def __init__(self, use_pretty_board=False, use_logging=False):
        '''Create a new game board.'''
        self._spaces = {} # The board is represented by a dictionary
        for space in ALL_SPACES:
            self._spaces[space] = BLANK # All spaces start blank.

    def get_board_string(self):
        '''Return a text representation of the board.'''
        return f'''
        {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
        -+-+-
        {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
        -+-+-
        {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9'''

    def is_valid_space(self, space: str) -> bool:
        '''Returns True if the given space is valid and the space is blank.'''
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def is_winner(self, player):
        s, p = self._spaces, player # Shorter names as "Syntactic Sugar"
        # Check for 3 marks across the three rows, three columns, and two diagonals
        return ((s['1'] == s['2'] == s['3'] == p) # Rows
                (s['4'] == s['5'] == s['6'] == p)
                (s['7'] == s['8'] == s['9'] == p)
                (s['1'] == s['4'] == s['7'] == p) # Columns
                (s['2'] == s['5'] == s['8'] == p)
                (s['3'] == s['6'] == s['9'] == p)
                (s['3'] == s['5'] == s['7'] == p) # Diagonals
                (s['1'] == s['5'] == s['9'] == p))

    def is_board_full(self):
        '''Return True if every space on the board is taken.'''
        for space in ALL_SPACES:
            if self._spaces == BLANK:
                return False
        return True # No spaces are blank, so return True.

    def update_board(self, space, player):
        '''Sets the space on the board to player.'''
        self._spaces[space] = player


if __name__ == '__main__':
    main()