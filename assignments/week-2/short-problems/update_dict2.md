# CSc 120: Update a 2-level dictionary

## Definitions

A *two-level dictionary* is analogous to a list-of-lists (aka "2D-list"), except that it involves dictionaries rather than lists:
* A list-of-lists `L` is a list where each element `L[someidx]` is itself a list; and `L[someidx][anotheridx]` gives us a value stored in `L`.
* Analogously, a two-level dictionary `D` is a dictionary-of-dictionaries: `D[somekey]` is itself a dictionary, and `D[somekey][anotherkey]` gives us a value stored in the two-level dictionary `D`. In this example, `somekey` is called the *first-level* key and anotherkey is called the *second-level* key.

In the examples below, DD is assumed to be the following two-level dictionary:
```
  { 'aaa' : { 'bbb' : 'string1', 'ccc' : 'string2', 'ddd' : 'string3' },
    'bbb' : { 'ccc' : 'string4', 'ddd' : 'string5', 'eee' : 'string6', 'fff' : 'string7' },
    'ccc' : { 'aaa' : 'string8', 'bbb' : 'string9' }
  }
```
Thus, we have: `DD['bbb']['ccc']` is the value 'string4', while `DD['ccc']['bbb']` is 'string9'.

## Expected Behavior
Write a function `update_dict2(dict2, key1, key2, value)`, where `dict2` is a two-level dictionary; `key1` is the first-level key; `key2` is the second-level key; and `value` is a value to be stored at `dict2[key1][key2]`. This function should return a dictionary obtained by updating dict2 such that in the resulting dictionary, which we refer to as `newdict2`, the following holds:
    `newdict2[key1][key2] == value.`

## Examples

DD is the two-level dictionary shown above (under **Definitions**).

```
1. update_dict2(DD,'aaa','ccc',12)
return value:
{ 'aaa' : { 'bbb' : 'string1', 'ccc' : 12, 'ddd' : 'string3' },
  'bbb' : { 'ccc' : 'string4', 'ddd' : 'string5', 'eee' : 'string6', 'fff' : 'string7' },
  'ccc' : { 'aaa' : 'string8', 'bbb' : 'string9' }
}

2. update_dict2(DD,'aaa','ggg','string17')
return value:
{ 'aaa' : { 'bbb' : 'string1', 'ccc' : 12, 'ddd' : 'string3', 'ggg' : 'string17' },
  'bbb' : { 'ccc' : 'string4', 'ddd' : 'string5', 'eee' : 'string6', 'fff' : 'string7' },
  'ccc' : { 'aaa' : 'string8', 'bbb' : 'string9' }
}

3. update_dict2(DD,'ggg','aaa','string17')
return value:
{ 'aaa' : { 'bbb' : 'string1', 'ccc' : 12, 'ddd' : 'string3' },
  'bbb' : { 'ccc' : 'string4', 'ddd' : 'string5', 'eee' : 'string6', 'fff' : 'string7' },
  'ccc' : { 'aaa' : 'string8', 'bbb' : 'string9' },
  'ggg' : { 'aaa' : 'string17' }
}
```