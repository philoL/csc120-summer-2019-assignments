# CSc 120: Word Search

## Background
Word search is a word game that involves searching for words in a (random) grid of letters. This program simulates the game by searching for words in a grid. The program differs from the physical game in several ways:
	* The physical game is usually played with a 4 × 4 grid. Your program will generalize this to any N × N grid (N ≥ 4), where N is provided by the user as input.
	* The physical game uses a random grid. Your program will read the grid of letters from a file.
	* The physical game is timed: players try to find as many words as they can before a timer runs out. Your program will not have this constraint.
	* The pyhsical game includes words found on all diagonals. We will simplify the word search by eliminating all but one diagonal search.

## Definitions

Given a grid of letters `G` and a list of words `L`, a word in `G` is legal if it meets the following criteria:
	* it is at least **three** letters long;
	* it can be formed from letters in G that are adjacent along a row (two cases: going left-to-right or right-to-left), a column (two cases: going top-to-bottom or bottom-to-top), or a diagonal (one case: going upper-left to lower-right); and
	* it can be found in the list of words `L`.

## File Names
Your program should be in a file named `word_search.py`

## Expected Behavior
Your program should

* Read in, in this order, the **name** of a word-list file and the **name** of a grid-of-letters file. Do not prompt the user, that is, do not supply an argument to input(). Simply read in two file names and treat the first as the name of a word-list file and the second as a grid-of-letters file.
* Read the word-list file into a list and the grid-of-letters file into a square grid. You may assume that these files are organized as follows:
	* the word-list file contains one word per line;
	* the grid-of-letters consists of N lines, each line consisting of N letters separated by whitespace.
* Search this grid for legal words. Matches of words found in the grid against those in the list-of-words should be case-insensitive.
* Collect the legal words found into a list and print them out as indicated under Output format below.

## Examples
When converting from a random number to a letter, do not use a big ​if-statement. See the Number to letter problem for this.
The following is an example of the grid of letters file:

```
    y c o d e j
    h s e y p k
    l p h b w a
    l o b w x z
    w o b a a i
    p l y y c g
```

In this example (and as your program can figure out after reading the first line), N = 6. For this grid, the words your program should print out are:
```
code, cod, ode, lob (horizontal, L-to-R)
bow, yes, doc (horizontal, R-to-L)
spool, pool, way (vertical, top-to-bottom)
loop, loops (vertical, bottom-to-top)
lob, wag (diagonal, top-left to bottom-right)
```

## Input files
You can use the file [WORDS](), which is a list of about 45,000 words, to test your program. However, note that we may also use other word-lists, which may be bigger or smaller than this list, when testing your code. You should test your code using your own word-lists, which can be bigger or smaller than this list and whose words that may or may not be real English words.

## Output format
The words you find should be printed one to a line without any extra whitespace. The order in which they are printed does not matter.

## Development Strategy

* **Data Structures** Organize the list of valid words as a list of strings. Organize the grid as a list of lists.
* Program development
	1. Write a function `​occurs_in(s, L)` that indicates whether the string `s` occurs in a list of words `L` ignoring upper/lower case differences.
	2. Searching horizontally. First, consider the problem of finding words horizontally in the grid going from left to right. Consider the first row in the example shown above:
	```
		y c o d e j
	```
	Notice that this row contains the words cod, code, and ode. Suppose that the row is represented as the list `[‘y’, ‘c’, ‘o’, ‘d’, ‘e’, ‘j’]`. A simple way to explore all the possible words (going L to R) in this list would be as follows (the process for the other rows is similar).
		* Starting at the first element (i.e., ‘y’), check whether the sequence of length 3 starting at that position is a legal word (we start with length 3 because a legal word has to be at least three letters long). Then check for length 4, then for length 5, etc., until you reach the end of the list.
		* Now repeat this step, but starting at the second element (i.e., ‘c’). Notice that this time you will come to the end of the list one step sooner. Then repeat for the third element, and so on.
		* In each of these steps, your code is checking a sequence of list elements (e.g., the sequence of elements ‘c’, ‘o’, ‘d’, ‘e’) to see whether this is a word that occurs in your list of words. How can you use the function concat_list() from the Short Problems for this assignment?
	Next consider the problem of searching for words horizontally going right to left. Suppose we want to search the row ​ `y c o d e j`​ going right to left. This is actually the same as reversing the row, to
	```
		j​ e d o c y
	```
	and then searching left to right (a problem you’ve solved already). The key thing to note here is that you’ve taken the problem of searching R-to-L and converted it into an equivalent problem involving an L-to-R search, for which you’ve already written code.
	3. Searching vertically. Next consider the problem of searching for words vertically, i.e., among columns. Can you use the function column2list() from the Short Problems for this assignment to solve this problem going from top to bottom? Can you figure out a way of using column2list() with list-reversing to solve the problem of searching vertically going from bottom to top?
	4. Searching diagonally. Searching diagonally is the hardest part of this problem, however, we are only considering one case: upper-left to lower-right.
		* If you can extract each diagonal into a list of letters, then you can simply search through this list as you did before—again, reducing this problem to one you’ve already written code to solve.
			* Suppose you start the diagonal at position 0 of row 0, i.e., at grid[0][0]. The diagonal elements are y s h f a g and correspond to the index values: [0][0], [1][1], [2][2], ... How do the x- and y-coordinates change as you go from one element to the next? Why do they change in this way?
			* Suppose you start the diagonal at position 1 in row 0, i.e., grid[0][1]. The diagonal elements are c e b x i (Note: this diagonal is shorter than the previous one) and correspond to the index values: [0][1], [1][2], [2][3], .... How do the x- and y-coordinates change as you go from one element to the next? Why do they change in this way?
			* Repeat this exercise for the diagonal starting at grid[1][0]. Look at how the x- and y-coordinates change between from each element to the next. How does this compare to the way they changed for the other two diagonals you considered (above)?
		Do you see a pattern in how the x- and y-coordinates change between successive elements? Can you use this pattern to extract a diagonal going from the upper-left to lower-right given its starting coordinates into a list?

## Testing
Make sure you test your code thoroughly before you turn it in. Some of the things you may wish to consider during testing are: case-sensitivity; different-sized word lists and/or grids; words occurring in different directions in the grid; and words and grids of different size.
