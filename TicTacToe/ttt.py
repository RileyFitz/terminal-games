from string import digits
from os import system, name

class ttt_board():
    def __init__(self):
        self.xTurn = True
        self.winner = ""
        self.board_state = ["1","2","3","4","5","6", "7","8","9"]
        self.clear_scr = True

    def print_board(self):
        '''
        Prints board in interface. Clears screen by default.
        '''
        if self.clear_scr:
            self.clear_screen()
        for i in range(2):
            print(f' {self.board_state[i*3]} | {self.board_state[i*3+1]} | {self.board_state[i*3+2]}')
            print(' __|___|__')
        print(f' {self.board_state[6]} | {self.board_state[7]} | {self.board_state[8]}')
        print(f'It is {"X" if self.xTurn else "O"}\'s turn!')

    def clear_screen(self):
        if name == 'nt':
            system('cls')
        else:
            system('clear')
        print('\n')

    def toggle_clear_scr(self):
        self.clear_scr = not self.clear_scr

    def check_winner(self):
        '''
        Checks all winning move possiblities, and for stalemate.
        Changes winner accordingly.
        '''
        player = 'X' if self.xTurn else 'O'
        for i in range(3):
            # Row check.
            if self.board_state[i*3] == self.board_state[i*3+1] == self.board_state[i*3+2] == player:
                self.winner = player
            # Column check.
            if self.board_state[i] == self.board_state[i+3] == self.board_state[i+6] == player:
                self.winner = player

        # Diagonals.
        if self.board_state[0] == self.board_state[4] == self.board_state[8] == player:
            self.winner = player
        if self.board_state[2] == self.board_state[4] == self.board_state[6] == player:
            self.winner = player

        # Check stalemate.
        for i, x in enumerate(self.board_state):
            if x in digits:
                return # Skip bc there are open spots.
        self.winner = 'T'

    def get_validated_move(self):
        '''
        Retrieves and ensures a valid move in entered by the player.
        Checks for valid numeral, and open space.
        '''
        accepted_chars = digits[1:10] # Returns string of digits 1-9.
        while True:
            try:
                attempt = input("Select space: ")
                if attempt in accepted_chars and len(attempt) == 1:
                    if self.board_state[int(attempt)-1] != 'O' and self.board_state[int(attempt)-1] != 'X':
                        return int(attempt)-1

                print(f' The value \'{attempt}\', is not valid. Try {accepted_chars}..')
            except Exception as e:
                print(f' Huh... you were able to get the following error..\n{e}\n')
                print(f' However, this is not valid. Try {accepted_chars}..')

    def initiate_game(self):
        '''
        This starts an entire self hosted game.
        Currently there is no interupt built in.
        This function will progress to a completetion state.
        '''
        while self.winner == "":
            self.print_board()
            move = self.get_validated_move()
            self.board_state[move] = 'X' if self.xTurn else 'O'
            self.check_winner()
            self.xTurn = not self.xTurn
        self.print_board()
        print('\n 3 in a row!!!')
        print(f' The winner is {self.winner}!')

if __name__=='__main__':
    game = ttt_board()
    game.initiate_game()
