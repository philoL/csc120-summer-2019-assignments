# CSc 120: Invert a Dictionary

## Expected Behavior
Write a function `invert_dict(origdict)` that behaves as follows. Its argument origdict is a dictionary. This function returns a new dictionary constructed as follows:
1. Let `origdict_keys` be the list of the keys of `origdict` and `origdict_vals` the list of the values that these keys are mapped to in `origdict`.

2. Construct a dictionary `newdict` with the following properties:
    * The set of keys of `newdict` is `origdict_vals`, and the set of values of `newdict` is `origdict_keys`.
    * for any `k` in `origdict_keys`, if `origdict[k] == val`, then `newdict[val] = k`. In other words, `newdict` is a mirror image of `origdict`. In other words, `invert_dict()` inverts the mapping between keys and values.

3. Return the dictionary `newdict` so constructed.

## Examples

```
1. Suppose origdict = { 'a':12, 'b':93, 'c':47}. Then the value returned by invert_dict is the dictionary
    { 12:'a', 93:'b', 47:'c' }

2. Let origdict = { 345:'pqr', 456:'abc', 123:'wxy', 234:'ijk'}. Then the value returned by this function is the dictionary
    { 'pqr':345, 'abc':456, 'wxy':123, 'ijk':234 }.

3. Let origdict = { (11,22,33):'uvw', (11,43,27):'abc', (22,11,19):'lmn' }. Then the value returned by this function is the dictionary
    { 'uvw':(11,22,33), 'abc':(11,43,27), 'lmn':(22,11,19) }.

```