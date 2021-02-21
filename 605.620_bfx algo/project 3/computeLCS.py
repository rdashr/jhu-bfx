#!/usr/bin/env python3
# Programming Assignment 3: Longest Common Subsequence
# Richard Ren - December 8, 2020

'''
This module implements the dynamic programming algorithm for the LCS problem.
  The algorithm is largely derived from CLRS Section 15.4, with particular
  consideration given to convert 1-indexing pseudocode to 0-indexing Python
  list. LCS_Length() method uses dynamic programming to determine b, c tables
  storing LCS, and print_LCS() method uses the tables to construct and print
  the LCS sequences.
'''

import numpy as np
import math
import time

# LCS_Length(): Use dynamic programming to construct lcs between sequences 
#   X and Y.
# input: sequences X & Y
# output: tables b & c with lcs table (not returned); length of lcs, time
#   elapsed, and # of comparisons duing LCS construction.
def LCS_Length(X, Y):
	# Initialize timestamp for time elapsed
	t1 = time.time()

	m = len(X)
	n = len(Y)

	# Initialize tables b (as empty) & c (as negative infinity)
	b = np.full((m, n), "")
	c = np.full((m+1, n+1), -math.inf)
	for i in range(1, m+1):
		c[i][0] = 0
	for j in range(0, n+1):
		c[0][j] = 0

	# Initialize # of comparisons
	lcs_comp = 0

	for i in range(1, m+1):
		for j in range(1, n+1):
			if X[i - 1] == Y[j - 1]:
				c[i][j] = c[i-1][j-1] + 1
				b[i-1][j-1] = "⇖"    # 0-indexing conversion
				lcs_comp += 1
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i-1][j-1] = "⇑"
				lcs_comp += 2    # previous 1 comparison evaluates to False
			else:
				c[i][j] = c[i][j-1]
				b[i-1][j-1] = "⇐"
				lcs_comp += 3    # previous 2 comparisons evaluate to False
	
	t2 = time.time()
	lcs_time = (t2 - t1) * 1000000    # round to μs

	# print(b, c, sep="\n")    # in potential verbose mode, print tables b & c

	print_LCS(b, X, m, n)  # auxiliary method to construct & print LCS

	lcs_leng = c[m][n]

	return lcs_leng, lcs_comp, lcs_time


# print_LCS(): Auxiliary method to construct and print LCS between sequences.
# input: LCS table b, sequence X, lengths of sequences X & Y
# output: nothing returned; LCS sequence printed
def print_LCS(b, X, i, j):
	if i == 0 or j == 0:
		return
	# Depending on the item in b table, uses recursive methods to traverse
	#   upwards and leftwards while printing the substring (one by one).
	if b[i-1][j-1] == "⇖":
		print_LCS(b, X, i-1, j-1)
		print(X[i-1], end = "")
	elif b[i-1][j-1] == "⇑":
		print_LCS(b, X, i-1, j)
	else:
		print_LCS(b, X, i, j-1)
