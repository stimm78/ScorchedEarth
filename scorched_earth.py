import board
import player

class ScorchedEarth():
    """
    A class to represent the game of Scorched Earth

    Attributes:
    -----------
    board : Board
        represents game board
    turn : bool
        true if P1's turn, else P2's turn

    Methods:
    --------
    translate(sequence:string) -> None
        Translates string sequence into indices on board matrix
    move(sequence:string) -> None
        Moves piece according to string sequence if possible

    burn_squares(sequence:string) -> None
        Marks nodes unvisitable
    """
    def __init__(self):
        pass
