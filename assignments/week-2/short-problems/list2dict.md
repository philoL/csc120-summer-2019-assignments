# CSc 120: List to Dictionary

## Expected Behavior
Write a function `list2dict(list2d)` that behaves as follows. Its argument `list2d` is a 2D list (i.e., list of lists) of strings. It returns a dictionary whose keys are the first elements of each row, and where each such key is mapped to the list consisting of the remaining elements of that row.

## Examples

```
1. Let x1 be the following list of lists:
[ [ 'aa', 'bb', 'cc', 'dd' ],
  [ 'ee', 'ff', 'gg', 'hh', 'ii', 'jj' ],
  [ 'kk', 'll', 'mm', 'nn' ] ]

Then list2dict(x1) returns the dictionary
{ 'aa' : [ 'bb', 'cc', 'dd' ],
  'ee' : [ 'ff', 'gg', 'hh', 'ii', 'jj' ],
  'kk' : [ 'll', 'mm', 'nn' ]
}

2. Let x2 be the following list of lists:
[ [ 'aa', 'bb' ],
  [ 'cc', 'dd' ],
  [ 'ee', 'ff' ],
  [ 'gg', 'hh' ],
  [ 'kk', 'll' ] ]

Then list2dict(x2) returns the dictionary
{ 'aa' : [ 'bb' ],
  'cc' : [ 'dd' ],
  'ee' : [ 'ff' ],
  'gg' : [ 'hh' ],
  'kk' : [ 'll' ]
}

3. Let x3 be the following list of lists:
[ [ 'aa', 'bb' ],
  [ 'cc', 'dd', 'ee' ],
  [ 'ff', 'gg' ],
  [ 'hh', 'ii', jj' ],
  [ 'kk' ] ]

Then list2dict(x3) returns the dictionary
{ 'aa' : [ 'bb' ],
  'cc' : [ 'dd', 'ee' ],
  'ff' : [ 'gg' ],
  'hh' : [ 'ii', 'jj' ],
  'kk' : []
}
```