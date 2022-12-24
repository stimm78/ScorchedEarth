from board import Board
from player import Player

invalid_letters = "Input must be a sequence of [WASD]"
invalid_sequence = "Invalid sequence of moves"
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
    
    def move(self, direction):
        if self.turn:
            if self.is_valid_move(direction, self.player1, self.player2):
                self.burn_squares(self.player1.get_position(), '!')
                self.player1.update_position(direction)
                if not self.game_over:
                    self.board.update_board(self.player1.get_position(), 'A')
        else:
            if self.is_valid_move(direction, self.player2, self.player1):
                self.burn_squares(self.player2.get_position(), '!')
                self.player2.update_position(direction)
                if not self.game_over:
                    self.board.update_board(self.player2.get_position(), 'B')
        self.change_turn()

    def burn_squares(self, position, symbol):
        self.board.update_board(position, symbol)

    def change_turn(self):
        self.turn = not self.turn

    def is_valid_move(self, move, current_player, other_player):
        if move not in ['W','A','S','D']:
            print(invalid_letters)
            return False
        prev_position = current_player.get_position()
        current_player.update_position(move)
        if not current_player.is_valid_position(other_player):
            current_player.set_position(prev_position)
            print(invalid_sequence)
            return False
        current_player.set_position(prev_position)
        return True

    def game_over(self):
        player1_position = self.player1.get_position()
        player2_position = self.player2.get_position()
        if self.board.get_element(player1_position) == '!':
            print(p2_wins)
            return True
        if self.board.get_element(player2_position) == '!':
            print(p1_wins)
            return True
        return False

    def play(self):
        self.board.print_board()
        while True:

            print("Player 1 - Enter your move: ")
            p1_input = input()
            self.move(p1_input)
            self.board.print_board()
            if self.game_over():
                break

            print("Player 2 - Enter your move: ")
            p2_input = input()
            self.move(p2_input)
            self.board.print_board()
            if self.game_over():
                break


