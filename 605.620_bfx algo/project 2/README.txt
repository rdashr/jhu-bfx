Programming Assignment 2: Hashing
Richard Ren - November 10, 2020

This program is an implementation of hashing, with various hashing functions, schemes, bucket sizes, and collision handling methods. 

This program contains 7 auxiliary modules: chain.py, display.py, displayTable.py, getInput.py, hash.py, probe.py, and setScheme.py - each handling various aspects of the program - with main.py as the main driver. (There is an incomplete module hashMethod.py that currently implements the hash_insert algorithm - not part of the requirements, but good foundation to build on for future version.)

This program expects an input file in text format, in the same working directory. The input file will be prompted to user to enter. In the input file, any line containing only one numeric input would be considered an input key. If there are more than one numbers in a line, then the first one will be taken; any line with non-numeric characters will be ignored. By the end of the file, if there are no input key parsed, then the program prompts an error message and exits.

There are 11 predetermined hashing schemes, based on hashing function (and its divisor/factor), table size, bucket size, collision handling scheme, and desired data printed across each line. These are customizable in setScheme.py module. If an input text file is correctly detected, the user will be prompted to enter a number from 1 to 11 for these schemes; furthermore, if the user enters "x", then all schemes will be run and output to the same file. 

Desired hashing scheme(s) will execute, and the program will output the input key list, the result hash table, and relevant statistics for each scheme into an output file in the working directory named after the input filename and desired hashing scheme. At the conclusion of the program, the system will prompt a message in the console indicating the successful generation of hash tables.

This program and all its modules are written in Python 3.8, with standard libraries re, math, os.path, sys and time. Deque from collections library is imported to implement a stack class. It was tested on native MacOS Terminal v2.10; however, it is presumed to be independent of operating systems.

This program is written for Programming Assignment 2 for course 605.620, Professor Chlan.
