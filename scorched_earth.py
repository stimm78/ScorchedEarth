from board import Board
from player import Player

invalid_sequence = "Invalid sequence of moves"
invalid_input= "Input string must be in the format [1-2] [WASD] with a space in between."
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
        self.player2 = Player(False, [Board.BOARD_SIZE-1,Board.BOARD_SIZE-1])
    
    def move(self, direction, num_moves, current_player):
        if self.is_valid_move(direction, num_moves, current_player):
            for i in range(num_moves):
                self.burn_squares(current_player.get_position())
                current_player.update_position(direction)
                if self.game_over():
                    print("Game over.")
                    return
            if current_player == self.player1:
                self.board.update_board(current_player.get_position(), 'A')
            else:
                self.board.update_board(current_player.get_position(), 'B')
        else:
            print(invalid_sequence)

    def is_valid_move(self, direction, num_moves, current_player):
        if direction not in ['W','A','S','D'] or num_moves not in [1,2]:
            print(invalid_input)
            return False
        current_position = current_player.get_position()
        if direction == 'W':
            return self.board.BOARD_SIZE > current_position[0] - num_moves >= 0
        elif direction == 'A':
            return self.board.BOARD_SIZE > current_position[1] - num_moves >= 0
        elif direction == 'S':
            return self.board.BOARD_SIZE > current_position[0] + num_moves >= 0
        elif direction == 'D':
            return self.board.BOARD_SIZE > current_position[1] + num_moves >= 0

    def burn_squares(self, position, symbol='!'):
        self.board.update_board(position, symbol)

    def change_turn(self):
        self.turn = not self.turn

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
            elif player1_position == player2_position:
                print(p2_wins) 
                return True
        return False

    def is_valid_input(self, input_list):
        if len(input_list) != 2:
            print(invalid_input)
            return False
        if not input_list[0].isdigit():
            print(invalid_input)
            return False
        return True

    def play(self):
        self.board.print_board()
        while True:
            print("Player 1 - Enter your move [1-2] [WASD]: ", end="")
            p1_input = input().split()
            while not self.is_valid_input(p1_input) or not self.is_valid_move(p1_input[1],int(p1_input[0]),self.player1):
                print("Player 1 - Enter your move [1-2] [WASD]: ", end="")
                p1_input = input().split()
            self.move(p1_input[1],int(p1_input[0]), self.player1)
            self.board.print_board()
            if self.game_over():
                return

            print("Player 2 - Enter your move [1-2] [WASD]: ", end="")
            p2_input = input().split()
            while not self.is_valid_input(p2_input) or not self.is_valid_move(p2_input[1],int(p2_input[0]),self.player2):
                print("Player 2 - Enter your move [1-2] [WASD]: ", end="")
                p2_input = input().split()
            self.move(p2_input[1],int(p2_input[0]), self.player2)
            self.board.print_board()
            if self.game_over():
                return


