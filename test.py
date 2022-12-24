from board import Board
from player import Player
from scorched_earth import ScorchedEarth
import pytest

game = ScorchedEarth()

def test_valid_move():
    assert game.is_valid_move('S',2,game.player1) == False

