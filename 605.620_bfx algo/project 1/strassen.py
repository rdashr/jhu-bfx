#!/usr/bin/env python3
# Programming Assignment 1: Strassen Algorithm
# Richard Ren - November 28, 2020 (Resubmit)

'''
This module implements the strassen method for matrix multiplication,
  which includes splitting matrix into quadrants and computing result.
'''

import numpy as np
import time

# split_matrix(): Split matrix A into quadrants, in preparation
#   for strassen multiplication. 
# input: matrix A to be split, and quadrant coordinates (row/column)
# output: quartered matrix "new_matrix"
def split_matrix(matrixA, row_start, row_end, col_start, col_end):
  new_matrix = list()
  for i in range(col_start, col_end):
    new_matrix_row = list()
    for j in range(row_start, row_end):
      # For when matrixA[i] is already an integer (n = 1)
      if not type(matrixA[i]) is list:
        new_matrix_row.append(matrixA[i])
      # For when matrixA[i] is still a matrix (n >= 2)
      else: 
        new_matrix_row.append(matrixA[i][j])
    new_matrix.append(new_matrix_row)
  
  return new_matrix

# strassen_multiply(): Implementation of the Strassen Algorithm.
#   Recursively called to split, compute, and merge two matrices.
# input: two matrices A, B to be multiplied
# output: result matrix C (C = A * B)
def strassen_multiply(A, B):

  strassen_multiply.counter += 1

  n = len(A)
  new_n = int(n/2)    # length of split matrices

  # Recursion end case
  if n == 1:
    return A[0][0] * B[0][0]
  
  # Splitting two matrices A, B
  A_1_1 = split_matrix(A, 0, new_n, 0, new_n)  # Top left
  A_1_2 = split_matrix(A, new_n, n, 0, new_n)  # Top right
  A_2_1 = split_matrix(A, 0, new_n, new_n, n)  # Bottom left
  A_2_2 = split_matrix(A, new_n, n, new_n, n)  # Bottom right

  A = [A_1_1, A_1_2, A_2_1, A_2_2]
  
  B_1_1 = split_matrix(B, 0, new_n, 0, new_n)
  B_1_2 = split_matrix(B, new_n, n, 0, new_n)
  B_2_1 = split_matrix(B, 0, new_n, new_n, n)
  B_2_2 = split_matrix(B, new_n, n, new_n, n)

  B = [B_1_1, B_1_2, B_2_1, B_2_2]

  # Computing Strassen matrices
  # Matrix addition and subtraction by numpy library;
  #   Result converted back to native list
  S1 = np.subtract(B_1_2, B_2_2).tolist()    # S1 = B12 - B22
  S2 = np.add(A_1_1, A_1_2).tolist()         # S2 = A11 + A12
  S3 = np.add(A_2_1, A_2_2).tolist()         # S3 = A21 + A22
  S4 = np.subtract(B_2_1, B_1_1).tolist()    # S4 = B21 - B11
  S5 = np.add(A_1_1, A_2_2).tolist()         # S5 = A11 + A22
  S6 = np.add(B_1_1, B_2_2).tolist()         # S6 = B11 + B22
  S7 = np.subtract(A_1_2, A_2_2).tolist()    # S7 = A12 - A22
  S8 = np.add(B_2_1, B_2_2).tolist()         # S8 = B21 + B22
  S9 = np.subtract(A_1_1, A_2_1).tolist()    # S9 = A11 - A21
  S10= np.add(B_1_1, B_1_2).tolist()         # S10= B11 + B12

  # Recursively computing Strassen products P1 - P7
  P1 = strassen_multiply(A_1_1, S1)   # P1 = A11 * S1
  P2 = strassen_multiply(S2, B_2_2)   # P2 = S2  * B22
  P3 = strassen_multiply(S3, B_1_1)   # P3 = S3  * B11
  P4 = strassen_multiply(A_2_2, S4)   # P4 = A22 * S4
  P5 = strassen_multiply(S5, S6)      # P5 = S5  * S6
  P6 = strassen_multiply(S7, S8)      # P6 = S7  * S8
  P7 = strassen_multiply(S9, S10)     # P7 = S9  * S10

  # Computing result matrices with Strassen products
  C_1_1 = np.add(np.subtract(np.add(P5, P4), P2), P6)
  C_1_2 = np.add(P1, P2)
  C_2_1 = np.add(P3, P4)
  C_2_2 = np.subtract(np.subtract(np.add(P5, P1), P3), P7)

  # Merging 4 quadrants of result matrix C using stack methods
  #   of numpy; result matrix C converted back to native list
  C_top_half = np.hstack((C_1_1, C_1_2))
  C_bottom_half = np.hstack((C_2_1, C_2_2))
  C = np.vstack((C_top_half, C_bottom_half)).tolist()

  return C