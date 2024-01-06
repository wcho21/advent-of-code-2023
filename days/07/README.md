# README

## How to solve

### Part 1

This is a sorting problem, becuase it asks to determine "ranks".
To sort the cards, we can provide a key function as the problem states, that is, sort first by the "strength", and then by the card numbers.

The sum of product of "bid" and "rank" is the answer.

### Part 2

The only change is the interpretation of "J" card.
Parse the "J" cards as the lowest number, and when determining the "strength", increase the count of the most common label by the number of "J" cards.
Again, sort by the order the problem stated.
The rest steps remains the same.
