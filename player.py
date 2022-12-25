from board import Board
import random


class Player:
    """
    A class to represent a player. 

    Attributes:
    -----------
    player_identity : bool
        True if player 1, False if player 2

    position : list[row,col]
        Represents position of the player

    Methods:
    --------
    get_position() -> list
        Returns the position of the player

    set_position(position:list) -> None
        Sets the position of player to specified position

    update_position(move: string) -> None
        Updates the position of player according to input in [WASD]

    is_valid_position(): -> bool
        Returns True if current Player's position is valid, False otherwise

    is_player_one() -> bool
        Return True if player is p1, False if player is p2 (Unused)

    get_dice_roll() -> int
        Return the result of a dice roll (1-6) (Unused)
    """

    def __init__(self, player_identity, position):
        self.player_identity = player_identity
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def update_position(self, direction):
        current_position = self.get_position()
        if direction == 'W':
            current_position[0] -= 1
        elif direction == 'A':
            current_position[1] -= 1
        elif direction == 'S':
            current_position[0] += 1
        elif direction == 'D':
            current_position[1] += 1

    def is_valid_position(self):
        current_position = self.get_position()
        # Check for out of bounds
        if current_position[0] < 0 or current_position[1] < 0 or current_position[0] > Board.BOARD_SIZE-1 or current_position[1] > Board.BOARD_SIZE - 1: 
            return False
        return True

    def is_player_one(self):
        return self.player_identity == True

    def get_dice_roll(self):
        return random.randint(1,6)


