# CSc 120: Sum a CSV String

## Expected Behavior
Write a function `sum_csv_string(csv_string)` that behaves as follows. Its argument csv_string is a string of comma-separated values, with each value in the string being a sequence of decimal digits. It returns an integer that is the sum of the numerical values in the string.

## Examples

```
sum_csv_string("11,22,33")
return value: 66 (= 11 + 22 + 33)

sum_csv_string("11,22,-33")
return value: 0 (= 11 + 22 + –33)

sum_csv_string("976")
return value: 976
```