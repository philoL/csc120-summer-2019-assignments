# CSC 120: Programming Style

Programs are read much more often than they are written, so it is important to pay attention to its style. This document lists (some of) the style requirements for programming assignments in this class. This list is non-exhaustive: you will be penalized if you violate these requirements; however, you may also be penalized if your code uses poor style (in the latter case, you will get a warning first, and penalized if the style does not improve in subsequent assignments).
For CSc 120, we will generally follow the style guidelines given in PEP 8 -- Style Guide for Python Code. In particular, you should adhere to the rules given below.

NOTE: These rules will be expanded as the semester progresses and we cover new topics. When this happens, you will be informed of the change.

Docstrings
The style guidelines below refer to docstrings. A docstring for a function is a special kind of string that begins with, and ends with, three double-quote (") characters, and which provides documentation about the program entity it is attached to. Examples of docstrings are available here.
I. What you write
Layout:
Indentation: 4 spaces per level.
Line length: 79 characters.
Use blank lines (sparingly) to indicate logical sections in your code.
Comments: Your code should be appropriately commented.
At the very beginning of each Python file you submit, you should place a docstring giving summary information about the program as a whole. This summary should include the following information:
Name of file
Name of author
Purpose of the program
Course no., section no. semester
For example:

"""
    File: pokemon.py
    Author: Charm Ander
    Purpose: Compute the maximum average values for various Pokemon attributes 
        and answer queries about them.
"""
        
For functions and methods, state what they do, any preconditions the require, and any postconditions on the return value.
For each function, this information should be given in the form of a docstring (see above). The docstring should be placed immediately after the "def function_name(...):" line and should minimally include	the following information:

a brief (one or two line) summary of what the function does;
what its arguments and return value (if any) are;
any assumptions made by the function, i.e., any pre-condition that must be met in order for the function to work correctly; and
what we can expect to be true after the function has finished execution, i.e., its post-condition;
For example:

def sum_csv_string(csv_string):
    """Add the numbers in a string of comma-separated values.
  
    Parameters: csv_string is a string of comma-separated numeric values.
  
    Returns: A number that is the sum of the values in the argument string.
  
    Pre-condition: csv_string is a string.
  
    Post-condition: The return value is a number."""
          
For your convenience, a template is available here.

If the purpose or behavior of a piece of code is not obvious, comment it. However, don't just state the obvious—this only adds visual clutter. For example, the following comment is clutter:
x = x + 1    # increment x
Naming conventions:
Names to avoid
Class names should use the CapWords convention (aka CamelCase or StudlyCaps).
Function and method names should be lowercase, with underscores separating words as necessary. 
(We will add to these rules when we discuss objects and classes.)
Variable names should follow the same rules as function and method names.
Constants whould be written with all capital letters, with words separated by underscores. E.g.:
PI = 3.1416
DEFAULT_SIZE = 64
List comprehensions:
Don't use list comprehensions for code that has side effects.
List comprehensions should not be nested.
List comprehensions should not be "too long". For the purposes of this class, "too long" = "more than one line long".
II. How you write
Avoid redundancy. If you see the very similar code sequences—i.e., code that either looks similar, or behaves similarly—appear in more than one place, consider pulling them into a function.
Exception: Small fragments of trivial code, e.g., two or three statements to initialize or increment a few variables.

Avoid unnecessary complexity. Everything else being the same, simple code and data structures are better than complicated ones. Therefore, If a data structure or algorithm discussed in class (lectures or discussion sections) does what you need to do, then—unless explicitly required by an assignment spec—you should not resort to something significantly more complex.
