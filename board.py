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
    BOARD_SIZE = 10

    def __init__(self):
        self.board = [['-' for i in range(Board.BOARD_SIZE)] for j in range(Board.BOARD_SIZE)]
        for i in range(Board.BOARD_SIZE):
            for j in range(Board.BOARD_SIZE):
                if i == 0 or j == 0 or i == Board.BOARD_SIZE - 1 or j == Board.BOARD_SIZE - 1:
                    self.board[i][j] = '!'
        self.board[1][1] = 'A'
        self.board[Board.BOARD_SIZE-2][Board.BOARD_SIZE-2] = 'B'

    def print_board(self):
        for row in self.board:
            for elem in row:
                print(elem, end=" ")
            print()

    def update_board(self, coordinates, value):
        self.board[coordinates[0]][coordinates[1]] = value

    def get_element(self, coordinates):
        return self.board[coordinates[0]][coordinates[1]]

