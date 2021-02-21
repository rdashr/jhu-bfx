#!/usr/bin/env python3

'''
main module: The main driver to execute the code.
'''

import re
import sys
import os.path

import setScheme
import getInput
import hash

import hashMethod

def main():

	stdout_fileno = sys.stdout

	input_list, input_option, max_number_length = getInput.get_input()

	if input_option == 'x':    # Run all schemes
		for option in range (1, 12):
			scheme = setScheme.set_scheme(option)
			scheme.key_length = max_number_length
			scheme.index_length = len(str(scheme.table_size - 1))
			T = hash.make_hash_table(input_list, scheme)
	
	elif int(input_option) in range(1, 12):    # Run one scheme
		option = int(input_option)
		scheme = setScheme.set_scheme(option)
		scheme.key_length = max_number_length
		scheme.index_length = len(str(scheme.table_size - 1))
		T = hash.make_hash_table(input_list, scheme)

	else:    # Error case; there are no predetermined scheme for input option
		sys.stdout = stdout_fileno
		print("ERROR! Invalid Hashing Scheme - Hashing Unsuccessful, System Exiting.")
		exit()

	sys.stdout.close()
	sys.stdout = stdout_fileno

	print("Hash Table Successfully Generated")

	'''
	Future implementation; currently only supports hash_insert in linear or quadratic
	probing. (Feel free to un-comment and check it out though!)
	'''
	# hashMethod.hash_insert(T, 90123, scheme)

if __name__ == "__main__":
	main()
  
