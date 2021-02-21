#!/usr/bin/env python3

'''
displayTable module: It handles some intricacies with outputting the input keys and
	hash table elements. pad_slot() method adds leading "0"s to make all input keys 
	of the same length, and if an element is None, it changes it to empty spaces -
	this method makes the output look much like an aligned table. 
	print_table() method will print out the table slot number and the keys in each 
	of its bucket; in the case of chaining, it will also print out the slot's 
	previous and next references (like a linked list), separated by arrows. It will
	also skip tables with nothing in any of its buckets to make the hash table
	appear compact. 
'''


def print_table(h_table, scheme): 
	column = 0
	hash_table = pad_slot(h_table, scheme)

	for i in range(len(hash_table)):
		bucket = hash_table[i]

		if not bucket.key[0] == ' ' * scheme.key_length:
			i = str(i).zfill(scheme.index_length)    # Pads index to same length
			print (i, ": ", end = '')

			if scheme.collision_scheme == "chaining":
				print(bucket.prev, '<-', *bucket.key, '->', bucket.next, end = " | ")
			
			else:
				print(*bucket.key, sep = ', ', end = " | ")

			column += 1

			if column % scheme.data_across == 0:    # Print to desired # of data in row
				print()

	print()


def pad_slot(hash_table, scheme):
	'''
	One limitation of this method is that by changing None to an empty string,
		it inherently changes the composition of the hash table. For future operations
		on this hash table, it may be very tricky to tell an empty table slot from
		an empty string. It may be better to duplicate the hash table and perserve
		the original hash table, but that will mean double the storage requirement.
	'''
	chaining = scheme.collision_scheme == "chaining"

	for bucket in hash_table:
	
		for i in range(len(bucket.key)):

			if bucket.key[i] == None:    # Change None to empty spaces
				bucket.key[i] = ' ' * scheme.key_length

			else:    # Add leading 0s to make keys of same length
				bucket.key[i] = str(bucket.key[i]).zfill(scheme.key_length)
	
		if chaining:
	
			if type(bucket.next) == int:
				bucket.next = str(bucket.next).zfill(scheme.index_length)
	
			elif bucket.next == None:
				bucket.next = ' ' * scheme.index_length

			if type(bucket.prev) == int:
				bucket.prev = str(bucket.prev).zfill(scheme.index_length)
	
			elif bucket.prev == None:
				bucket.prev = ' ' * scheme.index_length

	return hash_table
