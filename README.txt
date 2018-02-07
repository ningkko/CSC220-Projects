# CSC220 Coding Challenge 1
A general description of our code:
This is a redundancy checker that (1)reads all the files in the input directory 
and (2)prints a report of the lines that are identical in any pair of files

## Installation and set-up
Download the file and run the file.

## Running the tests
Input: When the commend line asks for a directory, enter the absolute path of the directory you want to test
Output: A report of redundent lines in all the files in this directory. The first number is the index of the identical line in file 1, the second number is the index of that line in file 2, followed by content of the identical line.

### Example 1 
*Input:* /Users/apple/Desktop/csc220/test
*Output:*
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

## Acknowledgement
http://mywiki.wooledge.org/BashFAQ/036
https://stackoverflow.com/questions/19007383/compare-two-different-files-line-by-line-in-python
https://stackoverflow.com/questions/9585218/python-find-common-text-in-two-files

## Contributers
Fanghui He, Yining Hua, Yvonne Zhu, Qiaqia Ji

## Efficiency Test
