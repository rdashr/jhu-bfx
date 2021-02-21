#!/usr/bin/env python3
# Programming Assignment 3: Longest Common Subsequence
# Richard Ren - December 8, 2020

'''
This program finds the longest common substrings between two sequences.
  The input sequences are defined in the input text file(s), and the
  result will be printed in a separate file. This module invokes the 
  computation methods, and handles redirecting output to text file.
'''

import sys

import displayLCS
import getInput

def main():

	i_mode, r_name, r_seq, t_name, t_seq, o_fn = getInput.readInput()

	# sys.setrecursionlimit(1000000)  # Testing purposes only - memory intensive

	# Redirect output to defined filename
	sys.stdout = open(o_fn, "wt")
	stdout_fileno = sys.stdout

	# If computation mode is 1, we compare each sequences in the required input
	#   by themselves;
	if i_mode == 1:
		print(" " * 20, "--- REQUIRED INPUT COMPARISON ---")
		for i in range(len(r_seq)):
			for j in range(i + 1, len(r_seq)):
				displayLCS.display_LCS(r_name[i], r_seq[i], r_name[j], r_seq[j])

	# If computation mode is 2, we compare each of the sequences in the 
	#   required input with each of the sequences in the testing input
	elif i_mode == 2:
		print(" "* 20, "--- REQUIRED/TESTING COMPARISON ---")
		for i in range(len(r_seq)):
			for j in range(len(t_seq)):
				displayLCS.display_LCS(r_name[i], r_seq[i], t_name[j], t_seq[j])

	# End output redirection, close file
	sys.stdout.close()

# One driver to execute the entire code 
if __name__ == "__main__":
  main()
  
