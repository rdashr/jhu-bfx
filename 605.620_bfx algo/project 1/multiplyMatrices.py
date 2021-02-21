#!/usr/bin/env python3
# Programming Assignment 1: Strassen Algorithm
# Richard Ren - November 28, 2020

'''
This module calls for strassen and iterative methods for
matrix multiplcation.
'''

import numpy as np
import time

import iterative
import strassen

# multiply(): prints strassen & iterative multiplication 
#   results to console
# input: two matrices A, B to be multiplied
# output: returns none; prints input matrices (echoed), results, 
#   stastistics to console
def multiply(A, B):
  print ("{} x {} Matrix Multiplication".format(len(A), len(B)))
  print ("Matrix A:\n", np.array(A))
  print ("Matrix B:\n", np.array(B))

  # Compute matrix multiplication by iterative (ordinary) method
  ti_start = time.time()
  i_result, i_mul = iterative.iterative_multiply(A, B)
  ti_end = time.time()

  # Compute matrix multiplication by Strassen method
  ts_start = time.time()
  strassen.strassen_multiply.counter = 0
  s_result = strassen.strassen_multiply(A, B)
  s_mul = strassen.strassen_multiply.counter
  ts_end = time.time()

  ti = round((ti_end - ti_start) * 1000000)
  ts = round((ts_end - ts_start) * 1000000)

  # Display multiplication results
  print ("- " * 30)
  print ("Iterative (Ordinary) Multiplication Result:") 
  print (np.array(i_result))
  print ("Strassen Multiplication Result:") 
  print (np.array(s_result))

  # Display relevant statistics
  print ("- " * 30)
  print ("Statistics:")
  print ("Iterative - {} μs elapsed, with {} multiplications".format(ti, i_mul))
  print ("Strassen - {} μs elapsed, with {} multiplications".format(ts, s_mul))
  
  print ("-=" * 40)
