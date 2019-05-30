# CSc 120: Find maximum sum of N consecutive numbers

## Expected Behavior
`max_consec_sum(numbers, n)` returns the maximum sum of `n` consecutive elements of `numbers`, a list that contains any mix of `ints` and `floats`.

Assume that `1 <= n <= len(numbers)` and that `numbers` has at least one element.

## Challenge
See if you can write this function with only one loop, i.e., only a single for or while. Look at [hint](https://docs.python.org/3/library/functions.html) for a function that will help.

## Examples

```
>>> max_consec_sum([10,2,-3,4,3],1)
10

>>> max_consec_sum([10,2,-3,4,3],2)
12

>>> max_consec_sum([10,2,-3,4,3],3)
9

>>> max_consec_sum([10,2,-3,4,3],4)
13

>>> max_consec_sum([10,2,-3,4,3],5)
16
```

