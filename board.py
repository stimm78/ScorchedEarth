import player

class Board:
    """
    A class to represent the game board.

    Attributes 
    ----------
    board : 2D List
        represents the game board

    Methods
    -------
    print_board() -> None
        Prints current board state
    """
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([None] * 8)

    def print_board(self):
        for row in self.board:
            for elem in row:
                print(elem)
            print()

