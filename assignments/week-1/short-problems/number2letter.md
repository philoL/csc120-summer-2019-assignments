# CSc 120: Number to Letter

## Expected Behavior
Write a function `number2letter(n)`, where n is an integer between 0 and 25, that returns the upper-case letter at position n. Here, 'A' is at position 0, 'B' is at position 1, 'C' is at position 2, ... 'Z' is at position 25.

## Programming Comments
The simplest way to solve this problem is using one or more of the constants defined in Python's string module (documented [here](https://docs.python.org/3.5/library/string.html)). If you know how the [ASCII characters](http://www.asciitable.com/) are organized, you can also use the [chr()](https://docs.python.org/3.7/library/functions.html#chr) builtin function. Or you can just program it up yourself, it shouldn't take you more than a line or two of code.

## Examples

```
number2letter(3)
return value: 'D'

number2letter(17)
return value: 'R'
```