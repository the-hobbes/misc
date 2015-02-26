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
	for number in formatted_input:
		bit_flipped_string = ''
		integer_number = int(number)
		# convert number to binary representation, and save in a string
		binary_number = '{0:032b}'.format(integer_number)
		for character in binary_number: # flip the 1's and 0's
			if character == '1':
				bit_flipped_string += '0'
			else:
				bit_flipped_string += '1'

		# cast the string into an int, from base 2 (binary)
		print int(bit_flipped_string, 2) # int(string or number, base)

def main():
	formatted_input = read_input()
	flip_bits(formatted_input)

if __name__ == '__main__':
	main()