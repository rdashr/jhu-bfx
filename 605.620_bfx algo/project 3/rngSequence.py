#!/usr/bin/env python3
# Programming Assignment 3: Longest Common Subsequence
# Richard Ren - December 8, 2020

'''
This module is not a part of the main program. It is used to generate random
  sequences in an input file for input testing.
"Lab3InputRandom.txt" generates 50 random sequences up to 100 bases long;
"Lap3InputAsymptotic.txt"  generates 10 random sequences, of lengths
  incrementing by 100. 
It is included here for testing transparency; generate random sequences
  here at your own risk.
'''

import random
import sys

def main():

	sys.stdout = open("Lab3InputRandom.txt", "w")
	stdout_fileno = sys.stdout

	for i in range(50):
		print("seq_{} = ".format(i + 1), end = "")
		base_length = random.randrange(1, 100)
		for j in range(base_length):
			print(random.choice(['A', 'C', 'T', 'G']), end = "")
		print()

	sys.stdout.close()

	sys.stdout = open("Lab3InputAsymptotic.txt", "w")
	stdout_fileno = sys.stdout

	for i in range(10):
		print("seq_{} = ".format(i + 1), end = "")
		base_length = (i + 1) * 100
		for j in range(base_length):
			print(random.choice(['A', 'C', 'T', 'G']), end = "")
		print()

	sys.stdout.close()


if __name__ == "__main__":
  main()
  
