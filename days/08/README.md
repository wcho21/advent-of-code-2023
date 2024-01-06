# README

## How to solve

### Part 1

Simply traverse given "nodes", following the "instructions".
We can count how many times we moved.
This is the answer.

### Part 2

If we manually count the number of steps, it seems to loop infinitely.
This is because the process requires infeasibly large number of steps.

Actually each of end label (which end with "Z") have its period, and appears independently of with each other.
So, the required number of steps are the least common multipler of the periods.
