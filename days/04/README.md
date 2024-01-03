# README

## How to solve

### Part 1

For a scratchcard, think of the number lists like (mathematical) sets.
Specifically, treat the left and right number lists on the card--winning number list and game number list--as sets.

Now, the matching numbers are simply the intersection of the two sets, and the "point" is the size of the intersection.

Total up the points.
This is the answer.

### Part 2

At this point, it turned out that there's no such thing as "points", so we'll call them "scores" instead.

The solution is simple.
Just repeat the following steps for each card, in increasing order of the card index.
For the scratchcards below the current one, simply increment the number of copies by the score of the current scratchcard.

After that, add up all the number of scratchcards, which is the answer.
