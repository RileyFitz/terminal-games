from Deck import Deck
from string import ascii_uppercase

class Solitaire():
    def __init__(self):
        self.deck = Deck()
        self.board = [[],[],[],[],[],[],[]]
        self.aces = [[],[],[],[]]
        self.win = False
        self.temp_stock = []
        self.stock_flips = 0
        
    def fresh_deal(self):
        self.deck.reset_deck()
        self.deck.shuffle_deck()
        for rows in range(7):
            for columns in range(rows,7):
                self.board[columns].append(self.deck.pop())
        for card in self.deck.deck_list:
            card.revealed = True
        

    def print_board(self):
        print('BOARD')
        for column in self.board:
            if len(column) > 0:
                column[-1].revealed = True
        print("   1    2    3    4    5    6    7")
        print_board_object = self.generate_print_board_object()
        for j in range(self.find_max_list()):
            row = ascii_uppercase[j] + "  "
            for i in range(7):
                row += print_board_object[i][j] + "  "
            print(row)
            row = ""
        print('\n')

    def print_aces(self):
        print("ACES")
        print("Spades  Hearts  Dmnds  Clubs")
        rtn_str = ""
        for i in range(4):
            if len(self.aces[i])==1:
                rtn_str += self.aces[0][i].short() + "      "
            else:
                rtn_str += "Empty   "
        print(rtn_str)
        print('\n')

    def print_stock(self):
        print('STOCK')
        try:
            print(f'Top of Stock: {self.temp_stock[-1]}')
        except:
            print(f'No stock card is flipped yet, pop one!')
        print(f'There are {len(self.deck.deck_list)} cards left in the stock')
        print(f'You have flipped the stock {self.stock_flips} times')
        print('\n')

    def generate_print_board_object(self):
        print_board = []
        for i in range(7):
            print_board.append(["   "]*self.find_max_list())
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                char = "" if self.board[i][j].short()[0]=="1" else " "
                print_board[i][j] = self.board[i][j].short() + char
        return print_board

    def find_max_list(self):
        list_len = [len(i) for i in self.board]
        return max(list_len)
    
    def get_valid_user_move(self):
        valid_move = False
        valid_from = False
        valid_to = False
        while not valid_move:
            while not valid_from:
                move_from_row, move_from_col = self.get_valid_move_input()
                valid_from = self.validate_move_from(move_from_row, move_from_col)
            move_to_row, move_to_col = self.get_valid_move_input()
            #valid_to = self.validate_move_to(move_to_row, move_to_col) # exists, top of stack, opposite color of move card
            #valid_move = valid_from and valid_to
            valid_move = True # for dev
        # Move cards and any that may lie below, AKA moving stacks.

    def validate_move_from(self, row, col):
        # Check if card exists, and is revealed.
        try:
            # If spot has revealed attribute, it exists.
            if (self.board[col][row].revealed):
                return True
            print("This card has not been revealed yet. Try again.")
            return False
        except:
            print("This position does not contain a card. Try again.")
            return False
    
    def get_valid_move_input(self):
        while True:
            user_input = input("Enter a 2-character string (letter and number): ")
            if len(user_input) == 2 and user_input[0].isalpha() and user_input[1].isdigit():
                return int(ord(user_input[0]) - ord('a')), int(user_input[1])-1
            else:
                print("Invalid input. Please try again.")
    
    def user_action(self):
        print("Please choose to pop the stock(1) or make a move(2)")
        action = self.get_user_action()
        if (action == 1):
            print("Popping has not yet been implemented")
        else:
            self.get_valid_user_move()

    def get_user_action(self):
        while True:
            user_input = input("Enter 1(pop) or 2(move): ")

            if user_input == "1" or user_input == "2":
                return user_input
            else:
                print("Invalid input. Please enter 1 or 2.")

    def display_board(self):
        self.print_board()
        self.print_aces()
        self.print_stock()

def main():
    """Set up game steps"""
    game = Solitaire()
    game.fresh_deal()
    #while not game.win:
    game.display_board()
    # Decide pop or move
    game.user_action()
    ##get and validate user input
    game.get_valid_user_move()
    ##check win
    print("main")

if __name__=="__main__":
    main()
