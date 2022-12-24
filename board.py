import player

class Board:
    """
    A class to represent the game board.

    Attributes 
    ----------
    board_size : integer
        Represents size of the board
    board : 2D List
        Represents the game board

    Methods
    -------
    print_board() -> None
        Prints current board state

    update_board(coordinates:[x,y], value:string) -> None
        Update board with value at coordinates
    """
    board_size = 8

    def __init__(self):
        self.board = []
        for i in range(Board.board_size):
            self.board.append(['-'] * Board.board_size)

    def print_board(self):
        for row in self.board:
            for elem in row:
                print(elem)
            print()

    def update_board(self, coordinates, value):
        self.board[coordinates[0]][coordinates[1]] = value

