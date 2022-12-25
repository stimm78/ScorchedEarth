class Board:
    """
    A class to represent the game board.

    Attributes 
    ----------
    (class) board_size : integer
        Represents size of the board
    board : 2D List
        Represents the game board

    Methods
    -------
    print_board() -> None
        Prints current board state

    update_board(coordinates:list, value:string) -> None
        Update board with value at coordinates

    get_element(coordinates:list) -> string
        Returns element at coordinate
    """
    BOARD_SIZE = 8

    def __init__(self):
        self.board = [['-' for i in range(Board.BOARD_SIZE)] for j in range(Board.BOARD_SIZE)]
        self.board[0][0] = 'A'
        self.board[Board.BOARD_SIZE-1][Board.BOARD_SIZE-1] = 'B'

    def print_board(self):
        for row in self.board:
            for elem in row:
                print(elem, end=" ")
            print()

    def update_board(self, coordinates, value):
        self.board[coordinates[0]][coordinates[1]] = value

    def get_element(self, coordinates):
        return self.board[coordinates[0]][coordinates[1]]

