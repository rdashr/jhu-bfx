#!/usr/bin/env python3

'''
getInput module handles getting input file and desired hashing scheme from user.
	There are error handling methods to prevent a wrong filename or no keys detected.
	For each line, the module parses a number as key and populates the input key list
	using regex. Then it executes the hashing program. 
'''

import re
import sys
import os.path

import setScheme
import hash
import display
import hashMethod

def get_input():
	
	input_filename = input("Enter File Name: ")

	while not os.path.exists(input_filename):
		print('ERROR! File does not exist - Check your input.')
		input_filename = input("Enter File Name: ")

	f = open(input_filename)

	input_list = list()

	max_number_length = -1

	for line in f:
		line = line.rstrip()
		if re.search('\D', line):
			continue
		elif line:
			number = int(re.search('\d+', line).group())
			if len(str(number)) > max_number_length:
				max_number_length = len(str(number))

			input_list.append(number)

	if len(input_list) == 0:
		print('ERROR! There are no input keys to hash. System exiting.')
		exit()

	input_option = input("Enter hashing scheme number (1-11), or enter 'x' for all schemes: ")
	output_filename = input_filename[:-4] + "_scheme_" + input_option + ".txt"

	sys.stdout = open(output_filename, "wt")

	display.print_input(input_list, max_number_length)

	return input_list, input_option, max_number_length
