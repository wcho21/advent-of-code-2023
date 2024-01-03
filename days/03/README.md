# README

## How to solve

### Part 1

There are numbers and symbols to read, but some numbers are not adjacent to any symbols.
So, first, we are going to read off all numbers and symbols from the input, the "schematic" in the problem, and filter out those non-adjacent numbers.

To do this filtering, we need coordinates for each number and symbol.
Thus, we're going to parse numbers and symbols into "tokens", which consist of value (number or symbol) and its coordinates.

Now we can filter out the non-adjacent numbers.
We can do that in a brute force way, but here we do that in better method, so-called two-pointer technique.
The brute force method has a squared time complexity, since it compares all numbers with all symbols.
However, the two-pointer technique reduces it to linear time complexity.

Now we have adjacent numbers, which are the "part numbers" in the problem.
Add up all the numbers.
This is the answer.

### Part 2

This part requires numbers adjacent only to the gear symbols.

In Part 1, we've parsed numbers into "tokens", and during parsing, we've attached each number to a symbol to which the number is adjacent.
So, we can filter out all the number tokens which are not adjacent to gear symbols.

After that, we get a "gear ratio" number for each gear symbol and add them up.
We need to find gear symbols having two adjacent numbers only, so we take such gear symbols while adding up the gear ratios.
Finally, the sum of the gear ratios is the answer.
