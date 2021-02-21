#!/usr/bin/env python3
# Programming Assignment 3: Longest Common Subsequence
# Richard Ren - December 8, 2020

'''
This module hands input interface and input checking. The user gives:
  one or two input text files with input sequences, and a computation mode.
  The module parses from the input text file each sequence and a name for
  the sequence, and passes them to the main computation module.
'''

import os.path
import re

# parse_seq_name(): Checks if each line input text file is valid, then 
#   parses sequence and name of sequence from input text file.
# input: an open file object, passed from readInput()
# output: name, and sequence, parsed from each line in file
def parse_seq_name(file):
	name_list = list()
	seq_list = list()
	line_counter = 0
	
	for line in file:
		line_counter += 1
		line = line.rstrip()

		# Expect sequence in text file to be defined by:
		# $SOMENAME = $SOMESEQUENCE
		if not re.search('^.+=\s', line):
			print("Error! Line", line_counter)
			print("Input not defined with name and sequence. (Skipped)")
			continue

		# Expect sequence to not be empty
		name = re.match('^\S+', line).group()
		sequence = re.sub('^.+=\s', '', line)
		if (len(sequence) == 0):
			print("Error! Line", line_counter)
			print("Sequence is empty. (Skipped)")
			continue
		# Expect sequence to only contain DNA bases; however, if not,
		#   program will not terminate, but output a warning,
		elif re.search('[^AaTtCcGg]', sequence):
			print("Warning! Line", line_counter)
			print("Input contains non-base characters (A, T, C, G).")
		name_list.append(name)
		seq_list.append(sequence)

	print("File reading completed.")
	return name_list, seq_list


# readInput(): Gets filename and computation mode from user, 
#   checks if they are valid, opens file
# input: nothing
# output: computation mode; separated lists containing names and sequences
#   for required input and testing input, and output filename
def readInput():
	mode = input("Enter 1 for required input comparison, 2 for required/testing comparison: ")
	while not (mode == '1' or mode == '2'):
		print("Error! Invalid mode.")
		mode = input("Enter 1 or 2. ")

	mode = int(mode)

	req_fname = input("Enter file name for required input: ")

	# Keep attempting to open file until file is open
	while not os.path.exists(req_fname):
		print("Error! File does not exist. Check your input and try again.")
		req_fname = input("Enter file name for required input: ")

	req_file = open(req_fname)
	req_name, req_seq = parse_seq_name(req_file)
	req_file.close()

	req_fname = req_fname[:-4]
	output_fn = req_fname + "_output.txt"

	tst_name = None
	tst_seq = None

	# If computation mode is to compare required and testing input cases,
	# populate the testing sequence lists
	if mode == 2:
		tst_fname = input("Enter file name for testing input: ")
		
		while not os.path.exists(tst_fname):
			print("Error! File does not exist. Check your input and try again.")
			req_fname = input("Enter file name for testing input: ")

		tst_file = open(tst_fname)
		tst_name, tst_seq = parse_seq_name(tst_file)
		tst_file.close()

		tst_fname = tst_fname[:-4]
		output_fn = req_fname + "_" + tst_fname + "_output.txt" 

	print("Results will save to:", output_fn)

	print("-=" * 40)

	return mode, req_name, req_seq, tst_name, tst_seq, output_fn
