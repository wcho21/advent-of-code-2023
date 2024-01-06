# README

## How to solve

### Part 1

Suppose that the time $t$ and the distance (the "record") $l$ is given.

For holding time $h$, the traveled distance is $(t - h)h$.
So, we can immediately determine whether the traveled distance is greater than $l$ for each holding time $h$.

We may solve the problem in a brute force manner, by examining all holding times, and actually it's feasible enough.
However, we can get the answer way much faster using binary search and simple math.

Imagine that there is a (virtual) array, which has a holding time as index and a traveled distance as value.
With this array, we can use binary search algorithm to find the least index where the value is greater than the given key value.

If we find when the traveled distance is maximum, we can derive a formula.
For the given time $t$, there are $t$ possible holding times from 1 to $t$.
Suppose that the traveled distance is maximum when the holding time $h$ is $h_m$, and it is the least time to beat when $h = h_l$.
Then there are at least $h_m - (h_l - 1)$ ways to beat, since for $h = 1, \dots, h_l-1$, the traveled distance is not enough to beat.

```
time:    1   2   3   4   5   6   7  ...
                h_l         h_m
beat?:   n   n   y   y   y   y      ...
```

The traveled distance formula $(t - h)h$ is a quadratic function, so the traveled distance reaches its maximum at $h = t/2 \thinspace (= h_m)$.
The shape of the graph is a parabola, which means the values for $h = 1, \dots, h_m$ in the first half will appear again for the second half.
Therefore the number of ways to beat is $2(h_m - (h_l - 1))$, provided that the value at $h = h_m$ appears twice.
If the time $t$ is even, actually the peak value occurs twice, so we can use the formula as it is, but the time is even, it occurs only once, so taking this into consideration, the formula becomes $2(h_m - (h_l - 1))-1$.

Now the answer can be calculated simply using the formula, which is $2(t/2 - (h_l - 1))$ for even-number $t$, and $2(t/2 - (h_l - 1))-1$ for odd-number $t$, where $h_l$ can be found using binary search.

### Part 2

The only change is how to interpret the input, and the rest remains the same.
Apply the formula above to the single number.
