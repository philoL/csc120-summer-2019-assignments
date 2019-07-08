# CSc 120: Converting to Base 2

Converting between base 10 and base 2 is a common problem in computer science. The base 10 number 233 is **11101001** in base 2, as can be seen from the expression below:

      1 x 2^7 + 1 x 2^6 + 1 x 2^5 + 0 x 2^4 + 1 x 2^3 + 0 x 2^2 + 0 x 2^1 + 1 x 2^0

A simple algorithm for finding the base 2 representation of a base 10 number is the following: repeatedly divide the decimal number by 2 and keep track of the remainder. The first division by 2 tells whether the number is even or odd. An even value will have a remainder of 0 and therefore a 0 in the ones place. The division process is shown below:

     233/ 2 = 116 rem 1
           116 / 2 = 58  rem 0
                  58 / 2 = 29 rem = 0
                         29 / 2 = 14 rem = 1
                               14 / 2 = 7  rem 0
                                   7 / 2 = 3 rem = 1
                                        3 / 2 = 1 rem = 1
                                            1 / 2 = 0 rem = 1


Note that the first remainder computed is actually the last digit in the sequence. In other words, the digits are produced in the reverse order of their written sequence, which makes a stack perfectly suited to storing the remainders throughout this iterative process.

Write a function convert_to_base2(n) that takes a non-zero integer n and returns a string representing the integer n in base 2.  Use a stack as auxillary storage in your solution. The stack class is show below for reference.


      class Stack:
          def __init__(self):
              self._items = []

          def push(self, item):
              self._items.append(item)

          def pop(self):
              return self._items.pop()

          def is_empty(self):
              return self._items == []

          def __str__(self):
              return str(self._items)

