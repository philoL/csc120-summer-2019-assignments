# CSc 120: Pokemon data analysis

## Introduction
This problem involves some simple data analysis and aims to give you some more practice with combining Python data structures in interesting ways: in this case, using two-level dictionaries (i.e., a dictionary of dictionaries). The data, as it happens, is about [Pokemon](https://www.pokemon.com/us/) (source: www.kaggle.com). You are to write a program to read in Pokemon data from a file and organize it according to Pokemon type (we will only consider **Type 1** for this assignment), then repeatedly read in queries from the user and print out solutions to those queries.

## Input Format
The input file, [Pokemon.csv](Pokemon.csv), is in [CSV format](https://en.wikipedia.org/wiki/Comma-separated_values) ("comma-separated values"). This is a simple file format typically used for tabular data such as that for spreadsheets, and if you want you can open this file in a program like Excel or libreoffice to view the data in an easier-to-read form.
Any line in the input file that begins with the character '#' (without quotes) is a comment line that should be ignored for data analysis.

The first line of the input file, which is a comment line, gives the meaning of the various data columns (in this table, the number at the top of each entry gives its position in a row of comma-separated values, e.g., "Attack" is at position 6):

| 0     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :---: | :---:|  :---: |:---: |:---: |:---: |:---: |:---: |:---: |:---: |:---: |:---: |:---: |
| No. | Name | Type 1 | Type 2 | Total Strength | HP | Attack | Defense | Special Attack | Special Defense | Speed | Generation | Legendary? |

## Expected Behavior
Write a program, in a file **pokemon.py**, that behaves as follows.

1. Read in the name of a data file. Use the `input()` function without suppling a string as a prompt. This file will be a CSV file containing data about Pokemon in the format described above. It can be the full [Pokemon.csv](Pokemon.csv) data file, but you can also specify other input files that contain more or less information (e.g., a smaller file may be useful for testing or debugging).

2. Read the data file specified and organize the data into a data structure that collects together information about different Pokemon types (for this assignment we will consider only the **Type 1** field for this, and ignore Type 2 since this is not defined for all Pokemon).

Note: Do **not** import the csv module for this assignment. (We will use that module in later assignments.)

3. Repeatedly read and process queries from the user (see Queries below) until the user enters an empty line.

## Queries
Your program will read in queries from the user, and for each query, analyze the Pokemon data based on the query and print out the results (see **Output Format** below). The queries and the corresponding analyses are as follows:


| User query | Program action |
| :---: | :---: |
| Total | Compute the Pokemon type(s) that have highest average Total strength.|
| HP | Compute the Pokemon type(s) that have highest average HP. |
| Attack | Compute the Pokemon type(s) that have highest average Attack. |
| Defense | Compute the Pokemon type(s) that have highest average Defense. |
| SpecialAttack | Compute the Pokemon type(s) that have highest average Special Attack. |
| SpecialDefense | Compute the Pokemon type(s) that have highest average Special Defense. |
| Speed | Compute the Pokemon type(s) that have highest average Speed. |
| (empty line) | Terminate query processing |
| anything else | Ignore the query |


Note that, in each case, there may be more than one type of Pokemon with the highest average value computed. You should print out information about each of them according to the output format given below.

Matching the queries entered by the user's with the User query column shown above should be case-insensitive. For example, the user inputs Attack, attack, ATTACK, and AtTaCk should all be processed the same way.

## Output Format
For each Pokemon type identified by your analysis, print out the result as follows:
	`print("{}: {}".format(pokemon_type, max_average))`

where `pokemon_type` is the type of Pokemon, and `max_average` is the average value computed for that Pokemon type for that query (e.g., average total, average HP, average Attack, etc.), which should be equal to the maximum value for that query across all types. If more than one Pokemon type has the same averge for a property, then print each one out, one per line, in alphabetical order of the Pokemon type.


## Programming Requirements
1. Follow the [style guidelines](../../coding-style.md) for this class.

2. Your code should not repeatedly and unnecessarily traverse all the data about all the Pokemon when processing queries. To this end, organize your code and data as follows.
	* **Data organization**
		Use a two-level dictionary (i.e., a dictionary of dictionaries) to implement your Pokemon database, as explained below:
			* At the top level, information should be grouped by Pokemon type: i.e., all of the information about Pokemon belonging to a particular type should be grouped together. A data structure that will do this efficiently is the dictionary.
			* For each Pokemon type, we have to store information about all of the different Pokemon that belong to that type. Again, this can be done efficiently using a dictionary that maps the Pokemon's name to its properties (Total strength, Attack, Defense, etc.).
	* **Code organization**
		Notice that the Pokemon properties you read in do not change during the computation. This means that the average value for any property for any given Pokemon type will remain the same as well. This, in turn, means that the maximum average values will also not change. Thus, these values can all be computed once and saved, with query processing simply looking up the saved values as needed. This approach is closely related to an speedup technique called [memoization](https://en.wikipedia.org/wiki/Memoization).

		Your code should be organized as follows:
		1. After reading in all the Pokemon data: for each Pokemon type, compute the average value for each of its properties across all of the Pokemon that belong to that type. Save this result into a dictionary indexed by Pokemon type.
		2. Next, process the average values obtained in the previous step to compute the maximum average value for each property. Optionally, at this point you can also compute which Pokemon types have the maximum average value for each property.
		3. Use these data to help process user queries until there are no queries to process.


