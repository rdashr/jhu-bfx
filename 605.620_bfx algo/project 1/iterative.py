#!/usr/bin/env python3
# Programming Assignment 1: Strassen Algorithm
# Richard Ren - November 28, 2020 (Resubmit)

'''
This module implements the ordinary iterative method
for matrix multiplication.
'''

# iterative_multiply(): Ordinary iterative algorithm for
#   multiplication of two square matrices A, B
#   (converted from pseudocode in CLRS Section 4.2)
# input: two matrices A, B to be multiplied
# output: returns result matrix C, multiplication counter
def iterative_multiply(A, B):  
  n = len(A)
  C = list()
  for m in range(n):
    C.append([0] * n)

  multiply_count = 0
  for i in range(n):
    for j in range(n):
      C[i][j] = 0
      for k in range(n):
        multiply_count += 1
        C[i][j]+= A[i][k] * B[k][j]
  
  return C, multiply_count
