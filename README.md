# Scorched Earth

An original turn-based strategy game built in Python.

## Rules

Players start on opposite corners of the board, with Player A starting
in the top left corner and Player B starting in the bottom right corner.

Alternating each turn, players input a command to move their avatar along
the grid. Every move leaves behind a "scorched" area that neither player
can touch. A player loses if they are captured by the other player or is
"checkmated" with no possible moves (surrounded by "scorched" areas)

## Usage

GUI/TUI WIP

CLI: 
```python main.py```

## CLI Input Format
Command input format: [number] [string]

[number] is 1 or 2, [string] is WASD

* [number] denotes number of moves
* [string] denotes direction

