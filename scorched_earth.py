from board import Board
from player import Player

INVALID_MOVE= "Invalid move. Path is scorched."
INVALID_INPUT= "Input string must be formatted [1-2] [WASD] to move (Ex: 2 D) or [R] to resign."

PLAYER1_PROMPT = "Player A - Enter your move [1-2] [WASD] or (R)esign: "
PLAYER2_PROMPT = "Player B - Enter your move [1-2] [WASD] or (R)esign: "

PLAYER1_WINS = "Player A wins."
PLAYER2_WINS = "Player B wins."
GAME_OVER = "Game over."

class ScorchedEarth():
    """
    A class to represent the game of Scorched Earth
    Attributes:
    -----------
    board : Board
        Represents game board
    turn : bool
        True if P1's turn, else P2's turn
    player1 : Player
        Initializes player 1
    player2 : Player
        Initializes player 2
    winner : Player
        Represents winner of game

    Methods:
    --------
    move(direction:string, num_moves:int, current_player:Player) -> None
        Moves player's piece [num_moves] places in [direction]

    is_valid_move(direction:string, num_moves:int, current_player:Player) -> bool
        Returns whether [current_player]'s move is valid

    burn_squares(position:list, symbol:string) -> None
        Marks nodes unvisitable

    change_turn() -> None
        Update player turn

    set_winner() -> None
        Set winner of game

    get_winner() -> Player
        Return winner of game 

    checkmated(player:Player) -> Player
        Return whether player is checkmated

    game_over() -> bool
        Checks for win conditions and prints game_over messages

    is_valid_input() -> bool
        Checks whether user input is valid

    play() -> None
        Simulates a game
    """
    def __init__(self):
        self.board = Board()
        self.turn = True
        self.player1 = Player(True, [1,1])
        self.player2 = Player(False, [Board.BOARD_SIZE-2,Board.BOARD_SIZE-2])
        self.winner = None
    
    def move(self, num_moves, direction, current_player): # moves current_player num_moves in direction, and updates board
        for _ in range(int(num_moves)):
            self.burn_squares(current_player.get_position())
            current_player.update_position(direction)
            if self.captured():
                break
        if current_player == self.player1:
            self.board.update_board(current_player.get_position(), 'A')
        else:
            self.board.update_board(current_player.get_position(), 'B')

    def is_valid_move(self, num_moves, direction, current_player): # checks for valid input, then check incrementally for valid move
        current_position = current_player.get_position()
        pos = current_position
        for i in range(1,int(num_moves)+1):
            if direction == 'W':
                pos = [current_position[0] - i, current_position[1]]
            elif direction == 'A':
                pos = [current_position[0], current_position[1] - i]
            elif direction == 'S':
                pos = [current_position[0] + i, current_position[1]]
            elif direction == 'D':
                pos = [current_position[0], current_position[1] + i]
            if self.board.get_element(pos) == 'A' or self.board.get_element(pos) == 'B':
                return True
            elif self.board.get_element(pos) == '!':
                print(INVALID_MOVE)
                return False
        return True

    def is_valid_input(self, input_list):
        if len(input_list) != 2:
            print(INVALID_INPUT)
            return False
        if not input_list[0].isdigit():
            print(INVALID_INPUT)
            return False
        if int(input_list[0]) not in [1,2] or input_list[1] not in ['W', 'A', 'S', 'D']:
            print(INVALID_INPUT)
            return False
        return True

    def burn_squares(self, position, symbol='!'):
        self.board.update_board(position, symbol)

    def change_turn(self):
        self.turn = not self.turn

    def set_winner(self, player):
        self.winner = player

    def get_winner(self):
        return self.winner

    def checkmated(self): # Check for win by checkmate, and set winners
        player1_position = self.player1.get_position()
        player2_position = self.player2.get_position()
        p1_position_1 = [player1_position[0] - 1, player1_position[1]]
        p1_position_2 = [player1_position[0], player1_position[1] - 1]
        p1_position_3 = [player1_position[0] + 1, player1_position[1]]
        p1_position_4 = [player1_position[0], player1_position[1] + 1]
        p2_position_1 = [player2_position[0] - 1, player2_position[1]]
        p2_position_2 = [player2_position[0], player2_position[1] - 1]
        p2_position_3 = [player2_position[0] + 1, player2_position[1]]
        p2_position_4 = [player2_position[0], player2_position[1] + 1]
        if self.board.get_element(p1_position_1) == '!' and self.board.get_element(p1_position_2) == '!' and self.board.get_element(p1_position_3) == '!' and self.board.get_element(p1_position_4) == '!':
            self.set_winner(self.player2)
            return True
        if self.board.get_element(p2_position_1) == '!' and self.board.get_element(p2_position_2) == '!' and self.board.get_element(p2_position_3) == '!' and self.board.get_element(p2_position_4) == '!':
            self.set_winner(self.player1)
            return True
        return False

    def captured(self): # Check for win by capture and set winners
        player1_position = self.player1.get_position()
        player2_position = self.player2.get_position()
        if self.turn:
            if player1_position == player2_position:
                self.set_winner(self.player1)
                return True
        else:
            if player1_position == player2_position:
                self.set_winner(self.player2)
                return True
        return False

    def game_over(self):
        return self.checkmated() or self.captured()

    def resign(self, input): # Checks for resign input, prints corresponding messages
        if self.turn:
            if input == ['R']:
                self.set_winner(self.player2)
                print(PLAYER2_WINS)
                return True
        else:
            if input == ['R']:
                self.set_winner(self.player1)
                print(PLAYER1_WINS)
                return True
        return False

    def play(self):
        grid = self.board
        grid.print_board()
        while not self.game_over():
            # Player 1 Turn
            print(PLAYER1_PROMPT, end="")
            p1_input = input().split()
            if self.resign(p1_input):
                return
            while not self.is_valid_input(p1_input) or not self.is_valid_move(p1_input[0], p1_input[1], self.player1):
                print(PLAYER1_PROMPT, end="")
                p1_input = input().split()
                if self.resign(p1_input):
                    return
                
            self.move(p1_input[0], p1_input[1], self.player1)
            grid.print_board()
            if self.game_over():
                break
            self.change_turn()

            # Player 2 Turn
            print(PLAYER2_PROMPT, end="")
            p2_input = input().split()
            if self.resign(p2_input):
                return
            while not self.is_valid_input(p2_input) or not self.is_valid_move(p2_input[0], p2_input[1], self.player2):
                print(PLAYER2_PROMPT, end="")
                p2_input = input().split()
                if self.resign(p2_input):
                    return
                
            self.move(p2_input[0], p2_input[1], self.player2)
            grid.print_board()
            if self.game_over():
                break
            self.change_turn()

        if self.get_winner() == self.player1:
                print(PLAYER1_WINS)
        else:
            print(PLAYER2_WINS)
        print(GAME_OVER)
        return

