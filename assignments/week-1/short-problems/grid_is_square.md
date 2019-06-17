# CSc 120: Grid is Square

## Expected Behavior
Write a function `grid_is_square(arglist)`, where `arglist` is a list of lists, that returns `True` if `arglist` has the shape of a square grid, i.e., if the length of each element (i.e., "row") of `arglist` is equal to the number of rows of `arglist`; and `False` otherwise.
You can assume that `arglist` is a list of lists, and do not have to check this.

## Examples

```
grid_is_square([[1,2],[3,4]])
return value: True

grid_is_square([[0,1,2],[3,4]])
return value: False

grid_is_square([[0,1,2,3,4],[3,4,5,6,7],[4,5,6,7,8]])
return value: False

grid_is_square([[1]])
return value: True

grid_is_square([[1,2,3],[3,4,5],[5,6,7]])
return value: True
```