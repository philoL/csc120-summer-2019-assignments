# CSc 120: Shuffle a Dictionary

## Expected Behavior
Write a function `shuffle_dict(somedict)` that behaves as follows. Its argument somedict is a dictionary. This function returns a new dictionary constructed as follows:
1. Let `sorted_keys` be the sorted list of the keys of somedict.
2. Let `sorted_vals` be the sorted list of the values that these keys are mapped to in somedict.
3. Construct a dictionary `shuffled_dict` that maps `sorted_keys[0]` to `sorted_vals[0]`, `sorted_keys[1]` to `sorted_vals[1]`, `sorted_keys[2]` to `sorted_vals[2]`, ... `sorted_keys[n]` to `sorted_vals[n]`.
4. Return the dictionary `shuffled_dict` so constructed.

**Note**: You can get the set of values in a dictionary `somedict` using `somedict.values()`. This is analogous to the keys() method that gives the keys in a dictionary. In each case, you then need to use `list()` to obtain a list.

## Examples

```
1. Suppose somedict = { 'a' : 12, 'b' : 93, 'c' : 47}. Then, sorted_keys is the list of keys of this dictionary in sorted order, so
      sorted_keys = ['a', 'b', 'c'].

  sorted_vals is the sorted list of values that these keys are mapped to, i.e.,
      sorted_vals = [12, 47, 93].

  Then the value returned by the function shuffle_dict is the dictionary
      { 'a' : 12, 'b' : 47, 'c' : 93 }

2. Let somedict = { 345:'pqr', 456:'abc', 123:'wxy', 234:'ijk'}. Then:
      sorted_keys = [123, 234, 345, 456]
      sorted_vals = ['abc', 'ijk', 'pqr', 'wxy']

   So the value returned by this function is the dictionary
      {123:'abc', 234:'ijk', 345:'pqr', 456:'wxy'}.

3. Let somedict = { (11,22,33):'uvw', (11,43,27):'abc', (22,11,19):'lmn' }. Then:
    sorted_keys = [(11, 22, 33), (11, 43, 27), (22, 11, 19)]
    sorted_vals = ['abc', 'lmn', 'uvw']

  So the value returned by this function is the dictionary
      {(11,22,33):'abc', (11,43,27):'lmn', (22,11,19):'uvw'}.

```