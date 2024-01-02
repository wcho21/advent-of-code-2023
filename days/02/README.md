# README

## How to solve

### Part 1

It may be enough to solve the puzzle by simply counting cubes for each color.
However, we can parse each line into a node representing the game.

Each game is parsed into a list of "Cube Sets" data structure, which is just an array of tables.
The table consists of the cube color and corresponding amount, represented as key and value, respectively.

Then we can judge if each game is "possible" by inspecting the cube sets for the game.
Whenever the game is possible, we add up its ID number.

### Part 2

Since we have parsed each game into "Cube Sets", we can pick the maximum amounts for each cube color, for each game.
The "minimum set of cubes" in the problem actually means these maximum amounts.

The "power" is given by the product of these maximums.
Simply add up the powers.
This is the answer.
