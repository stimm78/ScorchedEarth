import board
import random

invalid_letters = "Input must be a sequence of [WASD]"
invalid_sequence = "Invalid sequence of moves"

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
    is_valid_move(board:Board, sequence:string, other:Player) -> bool
        Returns True if sequence is a valid move
    is_valid_position(board:Board, other_player:Player): -> bool
        Returns True if current Player's position is valid
    is_player_one() -> bool
        Return True if player is p1
    get_dice_roll() -> int
        Return the result of a dice roll (1-6), which represents the number of moves
    """

    def __init__(self, player_identity, position):
        self.player_identity= player_identity
        self.position = position

    def is_valid_move(self, board, sequence, other):
        for character in sequence:
            if character not in ['W','A','S','D']:
                print(invalid_letters)
                return False

            if character == 'W':
                self.position[1] += 1
            elif character == 'A':
                self.position[0] -= 1
            elif character == 'S':
                self.position[1] -= 1
            elif character == 'D':
                self.position[0] += 1
            if not self.is_valid_position(board, other):
                print(invalid_sequence)
                return False
            
        return True

    def is_valid_position(self, board, other_player):
        if self.position[0] < 0 or self.position[1] < 0 or self.position[0] > board.board_size-1 or self.position[1] > board.board_size - 1:
            return False
        elif self.position == other_player.position:
            return False 
        return True

    def is_player_one(self):
        return self.player_identity == True
    
    def get_dice_roll(self):
        return random.randint(1,6)


