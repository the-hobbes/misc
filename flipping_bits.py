#!/usr/bin/python
'''
	Problem Statement

	You will be given a list of 32 bits unsigned integers. You are required to output the list of the unsigned 
	integers you get by flipping bits in its binary representation (i.e. unset bits must be set, and set bits must
	be unset).

	Input Format

	The first line of the input contains the list size T. T lines follow each line having an integer from the 
	list.

	Constraints

	1 <= T <= 100 
	0 <= integer < 232
	Output Format

	Output one line per element from the list with the requested result.

	Sample Input

	3 
	2147483647 
	1 
	0

	Sample Output

	2147483648 
	4294967294 
	4294967295
	Explanation

	Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001 and doing the flipping we get 
	11111111111111111111111111111110 which in turn is 4294967294
'''

import sys

def read_input():
	formatted_input = []
	is_first_line = True

	for line in sys.stdin:
		if is_first_line:
			is_first_line = False
			continue
		formatted_input.append(line.strip())

	return formatted_input

def flip_bits(formatted_input):
	bit_flipped_representation = None
	
	for number in formatted_input:
		integer_number = int(number)
		# convert number to binary, bin()
		binary_number = '{0:032b}'.format(integer_number)
		# change all ones to zeros, and vice-versa
		# convert number back to an integer
		# print the number
	return bit_flipped_representation

def main():
	formatted_input = read_input()
	flip_bits(formatted_input)

if __name__ == '__main__':
	main()