# CSc 120: Word Grid

## Target
This problem involves learning to use Python’s random number generator

## File Names
Your program should be in a file named `word_grid.py`

## Expected Behavior
Your program should read two integer values from the input: a **grid size** `N` and a **random number seed** `S`; use S to initialize the random number generator (i.e., S is the “seed”); create an N × N grid of randomly generated upper-case letters; and print out the grid of letters one row per line. Write a program, in a file named word-grid.py, that behaves as follows:

1. Write a function `init()` that does the following:
	1. Use the `input()`​ function to read in the value of N as the first value read in.
	2. Use the `input()`​ function to read in the value of S as the second value read in.
	3. Initialize the random number generator with the value S. You will have to import the module​ random:
		```
		import random
		```
		or
		```
		from random import *
		```
		The initialization is done by calling ​
		```
		random.seed(​ S ).
		```

	Note that your code should not prompt the user for input (that is, you should not supply a string to display to the user). Your program will simply read in two numbers and treat the first one as the grid size N (which needs to be an integer) and the second one as the seed S (which needs to be a string). Use the following code to initialize N and S, and then intialize the random number generator:

	```
        N = int(input())
        S = input()
        random.seed(S)
    ```

2. Write a function ​`make_grid(​ N )` that creates and returns an N × N grid of randomly generated letters:
each row of the grid is represented as a list of length N; and
the grid then consists of a list of N such rows.
	```
	For example: the grid

	a	b	c
	d	e	f
	g	h	i

	is represented as the list of lists

	[ [‘a’, ‘b’, ‘c’], [‘d’, ‘e’, ‘f’], [‘g’, ‘h’, ‘i’] ]
	```

3. Write a function​ `print_grid( G )` that takes a grid (i.e., list of lists) G and prints it out one row per line, with a single comma after each letter except for the last one in the row.
	```
	For example, the grid

	[ [‘p’, ‘q’, ‘r’, ‘s’], [‘t’, ‘u’, ‘v’, ‘w’], [‘x’, ‘y’, ‘z’, ‘a’], [‘b’, ‘c’, ‘d’, ‘e’] ]

	is printed out as

	p,q,r,s
	t,u,v,w
	x,y,z,a
	b,c,d,e
	```

**Note**: The indentation in this example is just to improve readability. The output from your print_grid() function should not have any whitespace at the beginning of any line for indentation purposes.

4. Write the​ main()​ function to do the following:
	1. call `init()`;
	2. call `make_grid()` ​ with the appropriate input argument ; and
	3. call `print_grid()` with the grid returned by make_grid() to print it out.

## Programming Requirements
When converting from a random number to a letter, do not use a big ​if-statement. See the Number to letter problem for this.

## Development Strategy
The representation of a grid of letters as a list of lists has been explained above. The key issue is to generate letters using the random number generator (initialized with the seed value S read in from the input).
	* You can use the function random.randint( m, n ) to generate a random integer between the values m and n. For example, random.randint(10, 20) ​ will generate a random integer between 10 and 20. Given this, think of how you can call random.randint(...)​ to generate values such that all possible (upper-case) letters, and only those letters, can be generated?
	* Once you have the random number returned by random.randint(...), you have to convert it to a letter. Use your solution for the number to letter problem for this.

**Comment**: If you are lazy like me and don't like unnecessary typing, you can import from the random library as follows:

	from random import *

after which you can simply refer to **randint(...)**, i.e., without having to type the prefix **random.randint(...)**.


