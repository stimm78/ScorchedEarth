from board import Board
import random


class Player:
    """
    A class to represent a player in Scorched Earth

    Attributes:
    -----------
    player_identity : bool
        True if player 1, False if player 2
    position : list[x,y]
        Represents position of the player

    Methods:
    --------
    is_valid_move(board:Board, move:string, other:Player) -> bool
        Returns True if sequence is a valid move
    is_valid_position(other_player:Player): -> bool
        Returns True if current Player's position is valid
    is_player_one() -> bool
        Return True if player is p1
    get_dice_roll() -> int
        Return the result of a dice roll (1-6), which represents the number of moves (TODO)
    """

    def __init__(self, player_identity, position):
        self.player_identity = player_identity
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def update_position(self, move):
        if move == 'W':
            self.position[1] += 1
        elif move == 'A':
            self.position[0] -= 1
        elif move == 'S':
            self.position[1] -= 1
        elif move == 'D':
            self.position[0] += 1

    def is_valid_position(self, other_player):
        current_position = self.get_position()
        # Check for out of bounds
        if current_position[0] < 0 or current_position[1] < 0 or current_position[0] > Board.board_size-1 or current_position[1] > Board.board_size - 1: 
            return False
        # Check if square is occupied by other player
        elif current_position == other_player.get_position():
            return False 
        return True

    def is_player_one(self):
        return self.player_identity == True
    
    def get_dice_roll(self):
        return random.randint(1,6)


