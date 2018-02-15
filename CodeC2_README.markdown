# CSC220 Coding Challenge 2: gene splicing
## Objective: 
Given two strings representing snippets of genes (letters ACGT), 
identify the shortest string that could contain them both as subsequences.

## Installation and set-up
- Download the file and run it in Python 3.
- Note: This program is written with regard to Python 3, so you might want to run it in Python 3!

## Running the tests
- Input: Two strings of genes, case insensitive, but needs the characters in both strings to be only from ["A","C","G","T"].
- Output: Outputs the shortest string that could contain them both as subsequences, and its length. If A Union B has the same length as B union A and is not the basic full length, return both strings.

### Example 1: Successfully concatenated
```
Nene-2:desktop Nene$ python test1.py
Please enter a string of genes: acgggggg
Please enter another string of genes: gggtTA 

******************************************** 
 string 1 – acgggggg string 2 – gggtTA 
 shortest string that has both as substring 
 acggggggtTA (length 11)
********************************************
```

### Example 2: Exception thrown out
```
Nene-2:desktop Nene$ python test1.py
Please enter a string of genes: FTYUJDHVBGHJ
Please enter another string of genes: DSHCJUDJSBF

Traceback (most recent call last):
  File "test1.py", line 60, in <module>
    main()
  File "test1.py", line 57, in main
    raise ValueError("The input string of genes is not valid")
ValueError: The input string of genes is not valid
```

## Efficiency test
In our code, we discuss the problem in two cases, each of which contains only one for-loop. Therefore, the time complexity for two loops is O(2n), and our solution is more efficient than using recursion(O(2^n)).

## References
Inspired by:
- https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
- https://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python


## Contributers
Fanghui He, Yining Hua, Yvonne Zhu, Qiaqia Ji
