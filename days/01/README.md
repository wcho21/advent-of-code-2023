# README

## How to solve

### Part 1

For each line, read off all numbers, from zero to nine (zero doesn't appear in the input though).

The numbers may appear only once or more than twice for each line.
In any case, it is possible to find the first and last numbers.
Then combine them to make a single number.
This is the "calibration value" for that line.

Add up the values.
That's the answer.

### Part 2

Now, we need to treat the letters (`one`, `two`, and so on) as "numbers".

The tricky part is that if we spot numbers in a given line, they can overlap.
Consider this, for example: `oneight`.
The "calibration value" for this line will be `28`.

If you examine all overlaps, you'll find that the numbers can overlap by at most one digit.
Moreover, specifically, the letters `o`, `t`, `e`, and `n` can overlap.
So, we can safely replace each the "number" letters with the corresponding digit, leaving overlap-able letters at both ends.
That is, for example, `oneight` is replaced with `o1e8t`, by replacing `one` and `eight` with `o1e` and `e8t`, respectively.

The remaining steps are the same as Part 1, from reading off numbers to adding up the calibration values.
