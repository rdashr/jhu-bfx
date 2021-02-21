#!/usr/bin/env python3
# Programming Assignment 1: Strassen Algorithm
# Richard Ren - November 28, 2020 (Resubmit)

'''
This program implements iterative and Strassen algorithms for
matrix multiplication. Matrices are provided by an input text file 
from user, and the program checks for errors, echoes the correct input, 
and computes the multiplication result onto a separate file.
'''

import re
import numpy as np
import math
import sys

import getInput
import multiplyMatrices

'''
This module iterates through input file line by line, populates
two matrices, evaluates condition, and calls for multiplication
methods.
It consists 1 main() method.
'''

# main(): iterates through input file, populates matrices, calls
#   for multiplication methods
# output: returns none
def main():
  # Redirect output to write to a separate file
  f, output = getInput.read_input()
  sys.stdout = open(output, "wt")
  stdout_fileno = sys.stdout

  matrix_A = []
  matrix_B = []

  is_matrixA = True  # boolean: decide to populate matrix A or B
  i = 0              # length of matrix currently populating
  length = None      # length of each matrix, defined by input file
  line_counter = 0   # counter for current line (for error message)
  have_error = False # have_error flag; flipped if error triggers

  for line in f:
    line_counter += 1
    
    line = line.rstrip()
    x = re.split('\s+', line)  # split line into list by whitespace

    matrices_full = i == length
    matrix_A_full = len(matrix_A) == length
    matrix_B_full = len(matrix_B) == length

    # compute_condition: boolean flag to decide whether
    #   to call for multiplication methods;
    #   (both matrices are at the matrix length defined)
    compute_condition = matrices_full and matrix_A_full and matrix_B_full

    # current line is the blank/separating line
    if x[0] == '':
      if have_error == False:
        # If no errors and compute_condition is satisfied, compute
        if compute_condition:
          multiplyMatrices.multiply(matrix_A, matrix_B)     

        # If no errors but compute_condition is not satisfied,
        #   there are too few or too many rows (Error Case 5)
        #   ignore current matrices and skip onto next matrices
        else:
          getInput.error_message(5, line_counter)
        
      # If there are errors, error messages have already been printed
      # reset flags, counters, matrices
      matrix_A = []
      matrix_B = []
      i = 0
      is_matrixA = True
      have_error = False
      continue 

    # Current line is not a blank/separating line
    else:
      # If there are errors, skip current matrices
      if have_error:
        continue     
      # Current line defines matrix length
      elif len(x) == 1:
        length = int(x[0])
        # Check for Error Cases 1, 2
        if getInput.input_check(1, length, length, line_counter):
          have_error = True
          continue
      # Current line is a matrix row
      else:
        # Check for Error Cases 3, 4
        if getInput.input_check(2, x, length, line_counter):
          have_error = True
          continue
        # Populate current row for Matrix A or Matrix B
        row = list(map(int, x))
        if i == length:
          is_matrixA = not is_matrixA
          i = 0
        if is_matrixA:
          matrix_A.append(row)
        else:
          matrix_B.append(row)
        i += 1

# One driver to execute the entire code 
if __name__ == "__main__":
  main()
  
