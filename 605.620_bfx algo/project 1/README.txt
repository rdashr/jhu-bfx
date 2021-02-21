Programming Assignment 1: Matrix Multiplication
Richard Ren - November 28, 2020 (Resubmit)

This program is an implementation of the iterative and the Strassen methods of Matrix Multiplication.

It is written in Python 3.8, with standard libraries lumpy, re, math, and os.path. It was tested on native MacOS Terminal v2.10; however, it is presumed to be independent of operating systems.

This program expects an input file in text format. This input text file must be in the same working directory as strassen.py script file. Here's a sample format of 2 4x4 matrices in the input text file that the program expects:

1	4
2	-5 6 -3 6
3	-5 -2 -3 -3
4	2 7 2 -5
5	5 -5 2 3
6	7 -2 1 -4
7	1 -5 5 8
8	2 8 -5 -1
9	-2 0 6 4
10

Line 1 defines the length of each matrix; this is expected to be an integer greater than 1 and a power of 2. Lines 2-5 will be populated as one matrix, each row in row major order, and Lines 6-9 will be populated as the second matrix. In Lines 1-9, the first character on each line must not be a whitespace character, and there must not be nonnumeric characters except negative sign "=". Line 10 divides the current matrices from the next matrices definition; on the very last line of the input text after the last matrix, there must be some whitespace character for the last pair of matrices to be computed.

To execute code, first execute main.py in console. Console will prompt for input text file name; enter full input file name, with extension, to continue execution. If the input file name is incorrect, program will prompt again until a correct input file name is entered.

After input file name is entered, program will read input file line-by-line and execute code. Result of matrix multiplication will be printed on the console. If there are any errors in any matrix entries, the program will skip the current pair of matrices to the next pair, as well as displaying an error message.

This program is written for Programming Assignment 1 for course 605.620, Professor Chlan.
