#!/usr/bin/env python3

'''
chain Module: handle chaining (open addressing) within the table.
	The algorithm works as such: for a key, check original hash value slot; if occupied,
	pop an index from the stack that keeps track of empty spaces, check if that
	index is empty; if it's empty, then store the key in it.
	Meanwhile, from the original position, build a doubly linked list with "prev"
	and "next" all the way to the final position, to signify "chaining".

'''


def chain(hash_table, empty_stack, key, hash_value, f_l):
	bucket = hash_table[hash_value].key
	collision = 0
	address = 0
	load = 0

	if bucket[0] == None:    # Case when there is no collision; original hash value slot open
		bucket[0] = key
		address += 1
		load += 1 

	else:    # Collision case
		collision = 1
		address += 1
		
		while len(empty_stack):
			chained = empty_stack.pop()    
			new_bucket = hash_table[chained].key
			address =+ 1    # Pop one from stack, check if empty; this accesses an address

			if new_bucket[0] == None:
				new_bucket[0] = key
				address += 1
				load += 1

				# Keep traversing through the "next" references to find a slot that's empty
				if hash_table[hash_value].next == None:
					# Maintain doubly linked-list structures
					hash_table[hash_value].next = chained
					hash_table[chained].prev = hash_value

				else:		
					chaining = hash_value
					
					while hash_table[chaining].next:
						address += 1
						chaining = hash_table[chaining].next

					hash_table[chaining].next = chained
					hash_table[chained].prev = chaining
				
				break

		if len(empty_stack) <= 0:    # Emoty stack is empty (more keys than table slots)
			f_l.append(key)

	return collision, address, load