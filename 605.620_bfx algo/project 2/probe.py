#!/usr/bin/env python3

'''
probe module: Probing with linear or quadratic (in one method). Both will handle
	wrapping. The probe() method will output collisions, addresses accessed, and 
	key stored.
'''

def probe(hash_table, key, hash_value, scheme, f_l):
	if scheme.collision_scheme == "linear":
		c1 = 1
		c2 = 0

	elif scheme.collision_scheme == "quadratic":
		c1 = 0.5
		c2 = 0.5

	i = 0
	address = 0
	load = 0

	slots = scheme.table_size * scheme.bucket_size
	
	while hash_value < scheme.table_size and address < slots:
		bucket = hash_table[hash_value].key
		unoccupied = False    # Check for each slot in bucket; if one is open, store
		
		for j in range (scheme.bucket_size):
			address += 1
		
			if bucket[j] == None or bucket[j] == ' ' * scheme.key_length:
				unoccupied = True
				break

		if unoccupied:
			bucket[j] = key
			load += 1
			break
		
		else:    # Collision Case
			i += 1
			# Calculate the offset defined by linear or quadratic
			offset = int((c1 * i + c2 * i * i) - (c1 * (i-1) + c2 * (i-1) * (i-1)))
			hash_value += offset

			# Wrap around
			if hash_value >= (scheme.table_size - 1):
				hash_value %= scheme.table_size

	if address == slots:
		# If a probe sequence has gone through the same number of addresses as there
		# are slots, without finding an open slot to store, the key is declared to 
		# have failed. This means that the quadratic probing has limitations that a 
		# key may not be inserted even if there are slots still open.
		f_l.append(key)
	
	return i, address, load