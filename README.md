# Maze-Solver
A practise exercise using Python for loops to solve a maze

The maze is a grid with walls ('X'), open paths (' '), a start point ('S'), and an end point ('E').

The program finds a path from 'S' to 'E' using loops.

## Maze Representation
Here's an example of a maze represented in maze.txt:

```
"X", "X", "X", "X", "X", "X", "X"
"X", "S", " ", " ", " ", " ", "X"
"X", " ", "X", "X", " ", "X", "X"
"X", " ", "X", " ", " ", " ", "X"
"X", " ", " ", " ", "X", "E", "X"
"X", "X", "X", "X", "X", "X", "X"
```

## Example output

Maze before solving:
```
XXXXXXX
XS    X
X XX XX
X X   X
X   XEX
XXXXXXX
```

Maze after solving:
```
XXXXXXX
X**** X
X XX*XX
X X **X
X   XEX
XXXXXXX
```

