# CSC220 Coding Challenge 2: gene splicing
## Objective: 
Given two strings representing snippets of genes (letters ACGT), 
identify the shortest string that could contain them both as subsequences.

## Installation and set-up
Download the file and run it in Python 3. Input a string when the code asks for a gene, and input a second string when the code asks for another gene.
Note: This pragram is written with regard to Python 3, so you might want to run it in Python 3!

## Running the tests
- Input: Two strings of genes, case insensitive, but needs the characters in both strings to be only from ["A","C","G","T"].
- Output: Outputs the shortest string that could contain them both as subsequences, and its length. If A Union B has the same length as B union A and is not the basic full length, return both strings.

### Example 1 
Nene-2:desktop Nene$ python gene_splicing.py
Please enter a string of genes: ctatttacg
Please enter another string of genes: ACGTgcta
******************************************** 
 string 1 – CTATTTACG string 2 – ACGTGCTA 
 shortest string that has both as substring 
 ['CTATTTACGTGCTA', 'ACGTGCTATTTACG'] (length 14)
******************************************** 

### Example 2
Nene-2:desktop Nene$ python gene_splicing.py
Please enter a string of genes: actrs
Please enter another string of genes: adwr
Traceback (most recent call last):
  File "gene_splicing.py", line 63, in <module>
    main()
  File "gene_splicing.py", line 14, in main
    raise ValueError("The input string of genes is not valid")
ValueError: The input string of genes is not valid

## Efficiency test
In our code, we discuss the problem in two cases, each of which contains only one for-loop. Therefore, the time complexity for two loops is O(n) (where n is the total length of the two string), and our solution is more efficient than using recursion(O(2^n)).

## References
Inspired by:
https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
https://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python
https://www.tutorialspoint.com/python/list_insert.htm
https://stackoverflow.com/questions/4838504/how-do-i-truncate-a-list

## Contributers
Fanghui He, Yining Hua, Yvonne Zhu, Qiaqia Ji
