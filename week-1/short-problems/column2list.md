# CSc 120: Column to List

## Expected Behavior
Write a function `column2list(grid, n)`, where `grid` is a list of lists and `n` is an integer, that returns a list consisting of the element at position `n` of each row of `grid`.
You can assume that `0 ≤ n < len(r)` for each row (i.e., element) of grid.

## Examples

```
In the examples below, x is assumed to be the following list of lists:
       [ [ 'aa', 'bb', 'cc', 'dd' ],
        [ 'ee', 'ff', 'gg', 'hh', 'ii', 'jj' ],
        [ 'kk', 'll', 'mm', 'nn' ] ]

column2list(x,3)
return value: ['dd', 'hh', 'nn' ]

column2list(x,0)
return value: [ 'aa', 'ee', 'kk' ]
```