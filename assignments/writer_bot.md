# CSc 120: Writer Bot

## Background
Suppose that you were given the task of generating random English text that is—at least somewhat—coherent and readable. You certainly couldn't simply pick random words from a dictionary, since the choice of the parts of speech (nouns, verbs, adverbs, etc.) would be random and the result would be a nonsensical string of words. Likewise, if you randomly selected words from a book, you will have narrowed the choice of words to the vocabulary from the book, but if there is no information on how the words should be sequenced so that the generated text mimics the structure of the English language, the result will again be nonsense.

However, if you could base the generated text on the characteristics of the original text, such as the frequency of combinations of words, then the resulting text would replicate those characteristics.
Markov chain analysis does precisely that. It determines the probability of words that are likely to follow combinations of words. Text generated based on those probabilities will have similar statistical properties of the original. The theory of Markov chain analysis can be found [here](https://en.wikipedia.org/wiki/Markov_chain).

## Markov Chain Algorithm

The Markov chain analysis groups sequences of words into prefixes (of a specified size) and determines the set of words that will follow each prefix. A word that follows a prefix is a suffix.

For example, consider the lyrics of the Monty Python song Eric Half-a-Bee:

```
Half a bee philosophically
Must, ipso facto, half not be.
But half the bee has got to be
Vis a vis, its entity. Do you see?
But can a bee be said to be
Or not to be an entire bee
When half the bee is not a bee
Due to some ancient injury?
```

We can build a table of all of the possible two word prefixes and the suffixes that follow. Since the resulting table is quite large, we will only show the table for a few of the prefixes that help to illustrate the discussion:

|         Prefix        |        Suffixes        |
|:---------------------:|:----------------------:|
| Half a                | bee                    |
| a bee                 | philosophically        |
|                       | be                     |
|                       | Due                    |
| bee philosophically   | Must                   |
| philosophically Must, | ipso                   |
| Must, ipso            | facto                  |

We can see that the phrase "Half a" is always followed by bee, but "a bee" can be followed by "philosophically", "be", or "Due".

To generate the text, the Markov chain algorithm will construct phrases by randomly choosing one of the suffixes that follows a given prefix, according to the table that is generated from the text.

For prefixes of length two, the algorithm can be described in pseudocode as follows:

```
create an empty list tlist of for the generated text
set w1 and w2 to the first two words in the text
add w1 and w2 to tlist
set the prefix to w1 w2
while the prefix is in the table
   randomly chose w3, one of the successors of prefix w1 w2 in the text
   append w3 to tlist
   set the prefix to w2 w3
```

To illustrate, the algorithm will start by adding "Half a" to tlist. The only option for a suffix is "bee", which is then appended to tlist. The current prefix changes to "a bee" and the loop repeats. This time, there are three options for suffixes: "philosophically", "be", or "Due". If we suppose that "Due" is chosen, then "Due" is appended to tlist and the prefix changes to "bee Due". The generated text in tlist at this point is:

```
   [ 'Half', 'a', 'bee', 'Due' ]
```

The text generation continues until the last suffix is reached, or until a sufficient amount of text has been generated. (This is explained further in the Expected Behavior section.)

Your program will read a file from input, use the Markov chain analysis to create a table of prefixes and suffixes, and use the pseudocode above to generate new text based on the table of prefix and frequencies.

## Definitions

### Word
In this problem, we want to keep the punctuation. We want "hurried" to be distinct from "hurried!" so that the generated text will retain some of the grammatical information of the original. A word is therefore defined as a sequence of characters surrounded by white space.

### NONWORD
Notice that the generated text must start with "Half a", since those are the first two words of the text. But to build the table, every word must have a prefix. The prefixes for "Half" and "a" at the beginning are boundary cases that would need to be considered in the algorithm. However we can avoid complicating the algorithm to handle these boundaries cases by introducing an artificial word that will never be encountered in the text. We'll define this as NONWORD and we will prime the first two prefixes to be "NONWORD NONWORD" and "NONWORD Half " . Our partial table from the example above would become the following:

|         Prefix        |        Suffixes        |
|:---------------------:|:----------------------:|
| NONWORD NONWORD       | Half                   |
| NONWORD Half          | a                      |
| Half a                | bee                    |
| a bee                 | philosophically be Due |
| bee philosophically   | Must                   |
| philosophically Must, | ipso                   |
| Must, ipso            | facto                  |

### Multiplicity
In the example text shown, each prefix/suffix pair occurs only once in the text. In this case, we say that the suffix has a multiplicity of 1. However, in larger texts, a prefix/suffix pair may occur many times. If the pair occurs 4 times, we say that the suffix has a multiplcity of 4. During text generation, if a suffix has a higher multiplicity, it has a greater chance of being chosen. This means the statistical properties of the original text are maintained.
