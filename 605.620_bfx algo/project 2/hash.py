#!/usr/bin/env python3

'''
hash module: handles actual computation of populating a hash table: computes a hash value
	with desired hash function, use this hash value to probe/chain, and populate the hash
	table. At the end it also stores various statistics for output. 
'''

import math
from collections import deque
import time

import chain
import probe
import display

def hash_key(key, scheme):
	if scheme.hash_function == "division":
		hash_value = key % scheme.factor
	
	elif scheme.hash_function == "multiplication":
		hash_value = math.floor(((key * scheme.factor) % 1) * scheme.table_size)

	return hash_value

def make_hash_table(input_list, scheme):

	t1 = time.time()

	class Table_Class:
		def __init__(self, key, next, prev):
			self.key = key
			self.next = next
			self.prev = prev

	hash_table = list()
	empty_stack = deque()
	
	for x in range (scheme.table_size):
		hash_table.append(Table_Class([None for y in range (scheme.bucket_size)], None, None))
		empty_stack.append(x)
	
	total_collision = 0
	address_accessed = 0
	elements_stored = 0
	failed = list()

	for key in input_list:
		hash_value = hash_key(key, scheme) 

		if hash_value >= scheme.table_size:
			failed.append(key)
			continue

		if scheme.collision_scheme == "chaining":
			col, add, elem = chain.chain(hash_table, empty_stack, key, hash_value, failed)
			total_collision += col
			address_accessed += add
			elements_stored += elem

		elif scheme.collision_scheme == "linear" or scheme.collision_scheme == "quadratic":
			col, add, elem = probe.probe(hash_table, key, hash_value, scheme, failed)
			total_collision += col
			address_accessed += add	
			elements_stored += elem

	class Stats_Class:
		def __init__(self, col, add, fail):
			self.collision = col    # Number of collisions
			self.accessed = add     # Number of addresses accessed
			self.failed_keys = fail # All keys failed to be input into hash table

	hash_stats = Stats_Class(total_collision, address_accessed, failed)
	hash_stats.input_size = len(input_list)
	hash_stats.elements_stored = elements_stored
	load_factor = elements_stored / (scheme.table_size * scheme.bucket_size)
	hash_stats.load_factor = load_factor

	t2 = time.time()

	hash_stats.time_elapsed = (t2 - t1) * 1000000

	display.display_hash_table(hash_table, scheme, hash_stats)

	return hash_table
