from board import Board
from player import Player

invalid_letters = "Input must be [WASD]"
invalid_numbers = "Input must be [123]"
invalid_sequence = "Invalid sequence of moves"
invalid_input= "Input string must be in the format [1-3] [WASD] with a space in between."
p1_wins = "Player 1 wins"
p2_wins = "Player 2 wins"

class ScorchedEarth():
    """
    A class to represent the game of Scorched Earth

    Attributes:
    -----------
    board : Board
        represents game board
    turn : bool
        true if P1's turn, else P2's turn
    player1 : Player
        initializes player 1
    player2 : Player
        initializes player 2

    Methods:
    --------
    is_valid_move(board:Board, move:string, other:Player) -> bool
        Returns True if move is a valid move

    move(direction:string, player:Player) -> None
        Moves player's piece according to string [WASD] if possible

    burn_squares(player:Player) -> None
        Marks nodes unvisitable

    play() -> None
        Starts the game
    """
    def __init__(self):
        self.board = Board()
        self.turn = True
        self.player1 = Player(True, [0,0])
        self.player2 = Player(False, [Board.board_size-1,Board.board_size-1])
    
    def move(self, direction, num_moves):
        if self.turn:
            if self.is_valid_move(direction, num_moves, self.player1):
                for i in range(num_moves):
                    self.burn_squares(self.player1.get_position())
                    self.player1.update_position(direction)
                    if self.game_over():
                        break
                if not self.game_over():
                    self.board.update_board(self.player1.get_position(), 'A')
        else:
            if self.is_valid_move(direction, num_moves, self.player2):
                for i in range(num_moves):
                    self.burn_squares(self.player2.get_position())
                    self.player2.update_position(direction)
                    if self.game_over():
                        break
                if not self.game_over():
                    self.board.update_board(self.player1.get_position(), 'A')
        self.change_turn()

    def burn_squares(self, position, symbol='!'):
        self.board.update_board(position, symbol)

    def change_turn(self):
        self.turn = not self.turn

    def is_valid_move(self, direction, num_moves, current_player):
        if direction not in ['W','A','S','D']:
            print(invalid_letters)
            return False
        if num_moves not in [1,2,3]:
            print(invalid_numbers)
            return False
        prev_position = current_player.get_position()
        for i in range(num_moves):
            current_player.update_position(direction)
            if not current_player.is_valid_position():
                current_player.set_position(prev_position)
                print(invalid_sequence)
                return False
        return True

    def game_over(self):
        player1_position = self.player1.get_position()
        player2_position = self.player2.get_position()

        if self.turn:
            if self.board.get_element(player1_position) == '!':
                print(p2_wins)
                return True
            elif player1_position == player2_position:
                print(p1_wins)
                return True
        else:
            if self.board.get_element(player2_position) == '!':
                print(p1_wins)
                return True
            elif player2_position == player1_position:
                print(p2_wins)
                return True
        return False
    
    def is_valid_input(self, input_string):
        if len(input_string) != 2:
            print("Input string must be in the format [1-3] [WASD] with a space in between.")
            return False
        if not input_string[0].isdigit():
            return False
        return True

    def play(self):
        while True:
            self.board.print_board()
            print("Player 1 - Enter your move [1-3] [WASD]: ", end="")
            p1_input = input().split()
            while not self.is_valid_input(p1_input) or not self.is_valid_move(p1_input[1],int(p1_input[0]),self.player1):
                print("Player 1 - Enter your move [1-3] [WASD]: ", end="")
                p1_input = input().split()
            self.move(p1_input[1],int(p1_input[0]))
            if self.game_over():
                break

            self.board.print_board()
            print("Player 2 - Enter your move [1-3] [WASD]: ", end="")
            p2_input = input().split()
            while not self.is_valid_input(p2_input) or not self.is_valid_move(p2_input[1],int(p2_input[0]),self.player2):
                print("Player 2 - Enter your move [1-3] [WASD]: ", end="")
                p2_input = input().split()
            self.move(p2_input[1],int(p2_input[0]))
            if self.game_over():
                break


