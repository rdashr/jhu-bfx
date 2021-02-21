#!/usr/bin/env python3

'''
setScheme module: Takes in an user-defined option, and create an object "scheme"
	that contains all the parameters for the hashing scheme. 
	These parameters include: hashing function (division or multiplication),
	m (divisor in division, factor in multiplication), table size, bucket size, 
	collision handling scheme (linear probing, quadratic probing, or chaining),
	and data across - to print across each row. These parameters are predefined
	but fully customizable.
'''

def set_scheme(option):

	class Scheme_Class:
		def __init__(self, h_func, m, b_size, t_size, c_scheme, data_a):
			self.hash_function = h_func
			self.factor = m
			self.table_size = t_size
			self.bucket_size = b_size
			self.collision_scheme = c_scheme
			self.data_across = data_a

	if option == 1:	
		scheme = Scheme_Class("division", 120, 1, 120, "linear", 5)
	elif option == 2:
		scheme = Scheme_Class("division", 120, 1, 120, "quadratic", 5)
	elif option == 3:
		scheme = Scheme_Class("division", 120, 1, 120, "chaining", 5)
	elif option == 4:
		scheme = Scheme_Class("division", 113, 1, 120, "linear", 5)
	elif option == 5:
		scheme = Scheme_Class("division", 113, 1, 120, "quadratic", 5)
	elif option == 6:
		scheme = Scheme_Class("division", 113, 1, 120, "chaining", 5)
	elif option == 7:
		scheme = Scheme_Class("division", 41, 3, 40, "linear", 3)
	elif option == 8:
		scheme = Scheme_Class("division", 41, 3, 40, "quadratic", 3)
	elif option == 9:
		scheme = Scheme_Class("multiplication", 0.618, 1, 120, "linear", 5)
	elif option == 10:
		scheme = Scheme_Class("multiplication", 0.618, 1, 120, "quadratic", 5)
	elif option == 11:
		scheme = Scheme_Class("multiplication", 0.618, 1, 120, "chaining", 5)

	scheme.scheme_number = option    # add a "scheme_number" attribute

	return scheme



