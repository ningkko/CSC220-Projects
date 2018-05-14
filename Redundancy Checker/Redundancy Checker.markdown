# CSC220 Coding Challenge 1
## Our project
This is a redundancy checker that 
1. reads all the files in the input directory and
2. prints a report of the lines that are identical in any pair of files

## Installation and set-up
Download the file and run it in Python 3.
Note: This pragram is written with regard to Python 3, so you might want to run it in Python 3!

## Running the tests
- Input: When the commend line asks for a directory, enter the absolute path of the directory you want to test
- Output: A report of redundent lines in all the files in this directory. The first number is the index of the identical line in file 1, the second number is the index of that line in file 2, followed by content of the identical line.

### Example 1 
```
*Input:* /Users/apple/Desktop/csc220/test
Output:
------------------------------
File 1: test1.py
File 2: test2.py
Number of identical lines:  4
------------------------------
***  5 2 def main():
***  7 4 print("hello wojfcskjndzcnad,cn,sndc")
***  10 7 ##this is not a dog
***  11 6 main()
------------------------------
File 1: test1.py
File 2: test3.py
Number of identical lines:  1
------------------------------
***  5 2 def main():
------------------------------
File 1: test1.py
File 2: test4.py
Number of identical lines:  1
------------------------------
***  5 2 def main():
------------------------------
File 1: test2.py
File 2: test3.py
Number of identical lines:  1
------------------------------
***  3 2 def main():
------------------------------
File 1: test2.py
File 2: test4.py
Number of identical lines:  1
------------------------------
***  3 2 def main():
------------------------------
File 1: test3.py
File 2: test4.py
Number of identical lines:  4
------------------------------
***  2 2 def main():
***  6 4 print (a)
***  7 5 print("This is a code in both test 3 and 4")
***  9 6 #This comment appears in test3 and also will appear in test4
```

## Efficiency test
We used generators to read in all file names. We made sure that all for loops are in their most efficient form. We also combined print statements when possible. Also, for the loops:
1) Instead of looping through the whole directory every time we are comparing two files, we compare any of two files only once. For example, if we have compared file1 with file2, we wouldn't compare file2 with file1
2) Instead of looping through all the lines in the files, we compare any of two lines only once. For example, if we have compared line1 with line2, we wouldn't compare line2 with line1
Therefore, we think that our program is efficient. 

## References
- http://mywiki.wooledge.org/BashFAQ/036
- https://stackoverflow.com/questions/19007383/compare-two-different-files-line-by-line-in-python
- https://stackoverflow.com/questions/9585218/python-find-common-text-in-two-files

## Contributers
Fanghui He, Yining Hua, Yvonne Zhu, Qiaqia Ji
