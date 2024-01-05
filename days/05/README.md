# README

## How to solve

### Part 1

Each category has "maps".
Here we parse each "map" as a closure, which takes a value and returns the mapped value if it falls within the mapping interval.

Note that a map can fail if a value to map is not within the mapping interval.
So each value will be tagged with the context of the category which it belongs to.
For example, when a "seed" value is successfully mapped to "soil" value, the mapped value will contain the "soil" as a context.
When the mapping fails, the "seed" context will remain.
If all mapping failed, an identity function, which only changes the category but keeps the same value, will be applied.

For each category, all "maps" can be prepared in this way.
Now when we map the seeds and subsequently map the mapped values for the next category, we have "location numbers".
Pick the minimum.
This is the answer.

### Part 2

The "ranges" are very large, so it may infeasible to solve by considering all the values within the intervals (though I found someone did solve in a brute force way using CUDA.)

Note that we may consider only lower bounds of the given intervals, since we're interested in the minimum number only ("the lowest location number" in the problem).
Actually, however, we also need to keep upper bounds of the intervals, because a mapping interval might only cover part part of an interval, not the whole, and divide the interval, which makes a new lower bound for the divided interval.

```
seed interval: 30 to 50
soil map: 40 to 60 -> 65 to 85

[seed]
 30        50
  .---------.
  |         |
  `---------`
       ^
      40

[soil]
 30   40   50   60 65 75
  .----.    .----.  .--.
  |    |    |    |  |  |
  `----`    `----`  `--`
                    ^^^^
             (divided and mapped)
```

In the actual codes, we're going to interpret ranges as half-open (right-open) intervals.
Then we can conviniently handle ranges using $[a, b) = [a, c) + [c, b)$.

Now it becomes clear how to solve in a feasible way.
For each category, divide the given intervals for partial mapping (if necessary), and do the mapping.
From the mapped "location numbers", get the minimum, which is "the lowest location number".
