# CSc 120: Find words with a specific pattern of consonants and vowels

## Expected Behavior
`cv_match(sentence, pattern)` returns a list of the words in sentence whose pattern of consonants and vowels matches pattern, a string of 'c's and 'v's.

## Programming Comments
Use `str.split` to break sentences into a list of words.

If you find yourself about to write code like if letter == "a" or letter == "e" ..., consider using the in operator instead. Example:
```
>>> "b" in "abc"
True
```

## Examples

```
>>> cv_match("Tim has a pet rat named Nip", "cvc")
['Tim', 'has', 'pet', 'rat', 'Nip']

>>> cv_match("Put the loot in your boot", "cvvc")
['loot', 'your', 'boot']

>>> cv_match("This will have no matches", "vvv")
[]
```

Vowels are a, e, i, o, and u. All other letters are consonants. Assume sentences are simply one or more words separated by spaces and have no punctuation or any other non-alphabetic characters.

Matches are on the basis of a whole word and are case-insensitive.

Assume the pattern has at least one character.

