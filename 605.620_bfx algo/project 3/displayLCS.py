#!/usr/bin/env python3
# Programming Assignment 3: Longest Common Subsequence
# Richard Ren - December 8, 2020

'''
This module handles outputing LCS computation results to the external user.
  The output is separated into 2 sections (by dash delimiter): input echoing,
  and result with statistics.
'''

from textwrap import wrap

import computeLCS

# display_LCS(): Given sequences X & Y, invoke LCS computation methods,
#   and output the results.
# input: sequences X & Y, as well as monikers for sequences
# output: none returned; input echoed and result printed to console
def display_LCS(X_name, X, Y_name, Y):
	# Input echoing: input sequences, separated by 3 letters at a time
	print("Sequence {}: {}".format(X_name, split_string(X)))
	print("Sequence {}: {}".format(Y_name, split_string(Y)))
	print("Sequence {} length: {} bases".format(X_name, len(X)))
	print("Sequence {} length: {} bases".format(Y_name, len(Y)))
	print("Sequences total length: {} bases".format(len(X) + len(Y)))
	
	print("- " * 30)

	# Results with statistics: LCS length, # of direct comparisons, time elapsed
	print("Longest Common Substring:", end=" ")
	length, comparisons, time_elapsed = computeLCS.LCS_Length(X, Y)
	length = round(length)
	time_elapsed = round(time_elapsed)
	print("\nLCS length: {} bases".format(length))
	print("Total # Comparisons:", comparisons)
	print("Time Elapsed: {} μs".format(time_elapsed))
	print("-=" * 40)


# split_string(): Auxiliary methods to separate input string by 3 letters
#   at a time, by space delimiter.
def split_string(str):
	l = wrap(str, 3)
	s = " ".join(l)
	return s
