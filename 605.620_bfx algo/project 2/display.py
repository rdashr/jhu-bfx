#!/usr/bin/env python3

'''
display Module: It handles writing into an output file an echo of input (input key list),
	result hash table, and relevant statistics - all while making output look nice and neat.
'''

import displayTable

def print_input(l, length):    # Echos the input keys 
	print(" " * 20, "--- INPUT KEYS --- \n")
	counter = 0
	
	for num in l:
		print(str(num).zfill(length), end = " ")
		counter += 1
		
		if not counter % 10:    # Print 10 keys across each line
			print()
	print()
	print('-=' * 40)


def display_hash_table(hash_table, scheme, hash_stats):
	print(" " * 20, "--- HASHING SCHEME", scheme.scheme_number, "--- \n")
	print("Hash Function:", scheme.hash_function, "by", scheme.factor)
	print("Table Size:", scheme.table_size, "; Bucket Size:", scheme.bucket_size)
	print("Collision Handling Scheme:", scheme.collision_scheme)

	print("*" * 70)
	print(" " * 20, "--- HASH TABLE --- \n")
	displayTable.print_table(hash_table, scheme)

	print("*" * 70)
	print(" " * 20, "--- STATISTICS --- \n")
	print("Input Keys:", hash_stats.input_size, "; Stored Keys:", hash_stats.elements_stored)
	print("Load Factor:", round(hash_stats.load_factor, 3))
	print("Failed Keys:", hash_stats.failed_keys)
	print("Addresses Accessed:", hash_stats.accessed)
	print("Collisions:", hash_stats.collision)
	print("Time Elapsed:", round(hash_stats.time_elapsed), "μs")
	print('-=' * 40)