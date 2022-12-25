# ScorchedEarth

An original abstract strategy game built in Python.

## Rules

Players start on opposite corners of the board, with Player 1 starting
in the top left corner and Player 2 starting in the bottom right corner.

Alternating each turn, players input a command to move their avatar along
the grid. Every move leaves behind a "scorched" tile that neither player
can touch. A player loses if they are captured by the other player or touch 
a "scorched" tile on the grid.

## Usage

GUI/TUI WIP

CLI: 
```python main.py```

## CLI Input Format
Command input format: [number] [string]

[number] 1 or 2, [string] is WASD

* [number] denotes number of moves
* [string] denotes direction

