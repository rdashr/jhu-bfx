#!/usr/bin/env python3
# Programming Assignment 1: Strassen Algorithm
# Richard Ren - November 28, 2020 (Resubmit)

import re
import math
import os.path

'''
Input Checking Module:
This module concerns reading & opening matrix input texts,
checking for errors, and outputting messages alerting user of
errors. It consists of 3 methods: read_input(); input_check(); 
error_message().
There are 6 specific error cases to check, each with specific
error case messages:
  Case 0: user's file name input is incorrect / file does not exist
    Pass: file opens, code executes
    Fail: file does not open; error message displayed; user is 
    prompted to re-enter file name
  Case 1: matrix length is too small (less than 2)
    Note: matrix length" is defined by the dimension n 
    in an n*n matrix. When matrix length is 1, algorithm trivially 
    holds, but it is assumed that matrix length is at least 2.
  Case 2: matrix length is not a power of 2
    Note: Requisite for Strassen algorithm
  Case 3: matrix row contains too many or too few columns
    Note: Input matrix needs to be an n*n square matrix, so each 
    row of the matrix must contain same number of columns.
  Case 4: matrix row contains invalid character
    Note: matrix elements must only contain numbers and negative
    sign "-". Fractions, decimal points, and other letters or symbols
    will fail this error case.
  Case 5: too many or too few matrix rows
    Note: Two matrices need to be of the same length defined in the
    input file. Otherwise, it is not clear which is Matrix A and
    which is Matrix B, and multiplication algorithms will fail.
In Cases 1-5, if matrix elements have error, program will print error
message, terminate current matrix calculation, and skip to next matrix.
'''

# read_input(): Prompting user input, check for Error Case 0,
#   open matrix input file
# output: opened input file object
def read_input():
  filename = input("Enter file name: ")

  while not os.path.exists(filename):    # Error Case 0 checking
    error_message(0, 0)
    filename = input("Enter file name: ")
  
  f = open(filename)
  o = "output_" + filename 
  return f, o

# input_check(): Check matrix items for Error Cases 1, 2, 3, 4
#   if error case triggered, flips have_error boolean flag to skip
#   current matrix to next matrix, prints error message.
# input: error case to check for, row/length to check, line counter
# output: method returns error case code; flips error flag
def input_check(case, item, matrix_length, line):
  if case == 1:     # Check for matrix length input
    # Error Case 1
    if item < 2:    
      error_message(1, line)
      have_error = True
      return 1
    # Error Case 2
    elif not (math.ceil(math.log2(item)) == math.floor(math.log2(item))):
      error_message(2, line)
      have_error = True
      return 2

  elif case == 2:     # Check for current matrix row input
    # Error Case 3
    if not len(item) == matrix_length:
      error_message(3, line)
      have_error = True
      return 3
    # Error Case 4
    else:
      for i in item:
        # Using regex to search for invalid characters
        if re.search("[^0-9\-]", i):    
          error_message(4, line)
          have_error = True
          return 4

# error_message(): Define error messages based on error case
# input: error case #, and line counter
# output: returns none; prints message to console
def error_message(code, line):
  messages = [ "File does not exist! Check your input.",
  "Matrix length must be greater than 1.",
  "Matrix length must be a power of 2.",
  "Matrix must contain same numbers of rows and columns.",
  "Matrix must not contain fractions or nonnumeric characters.",
  "Matrices must have same number of rows."]
  error = "ERROR! Line: " + str(line)
  skip = "Skipping to next matrix..."

  print(error, messages[code], sep = "\n", end = "\n")
  if code > 0:
    print(skip)
    print ("-=" * 40)
