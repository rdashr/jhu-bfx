#!/usr/bin/env python3

'''
hashMethod module: currently incomplete; however, it supports hash_insert method that 
	takes in a hash table, a key to be inserted, and a scheme that defines collision
	handling scheme. (Can be tried out by uncommenting in main; not extensively tested)
'''

import hash
import probe
import displayTable

def hash_insert(Table, key, scheme):
	print("Hash Insert algorithm: Inserting", key)

	hash_value = hash.hash_key(key, scheme)
	h_table = Table

	if scheme.collision_scheme == "linear" or scheme.collision_scheme == "quadratic":
		col, add, elem = probe.probe(h_table, key, hash_value, scheme, [])
		
	displayTable.print_table(h_table, scheme)

'''
def hash_search(Table, key, scheme):


def hash_delete(Table, key, scheme):
	# Deleting is made easier with doubly linked-list structure in chaining
'''