#!/usr/bin/python
'''
	Problem Statement

	James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides 
	to meddle with the letter. He changes all the words in the letter into palindromes.
	(A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or 
	forward).

	To do this, he follows 2 rules:

	(a) He can reduce the value of a letter, e.g. he can change 'd' to 'c', but he cannot change 'c' to 'd'. 
	(b) In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until 
	the letter becomes 'a'. Once a letter has been changed to 'a', it can no longer be changed.

	Each reduction in the value of any letter is counted as a single operation. Find the minimum number of 
	operations required to convert a given string into a palindrome. 


	Input Format 
	The first line contains an integer T, i.e., the number of test cases. 
	The next T lines will contain a string each. The strings do not contain any spaces.

	Output Format 
	A single line containing the number of minimum operations corresponding to each test case.

	Constraints 
	1 <= T <= 10
	1 <= length of string <= 104 
	All characters are lower case English letters.

	Sample Input #00
	4
	abc
	abcba
	abcd
	cba
	a

	Sample Output #00
	2
	0
	4
	2
	0

	Explanation

	For the first test case, abc -> abb -> aba.
	For the second test case, abcba is already palindromic string.
	For the third test case, abcd -> abcc -> abcb -> abca = abca -> abba.
	For the fourth test case, cba -> bba -> aba.
	For the fifth test case, a -> a.
'''

import sys

def get_input():
	# get dat input
	input_text = []
	for line in sys.stdin:
		line = line.strip()
		if line.isalpha(): # make sure the line is only letters
			input_text.append(line)
			
	return input_text

def count_operations(first_half, second_half):
	'''
		How many operations does it take to make the second half of a string a palindrome of the first?
		First, reverse the first half. This is what the second half must look like.
		Then using the ascii values of the characters in the second half, for each character compute how much
		must be subtracted from it in order to obtain the ordinal value for the corresponding character in the
		now-reversed first half.
	'''
	total_operations = 0
	reverse_first_half = first_half[::-1]

	for i in range(len(second_half)):
		if ord(second_half[i]) < ord(reverse_first_half[i]): # handle the possibility of either being bigger
			letter_difference = ord(reverse_first_half[i]) - ord(second_half[i])
		else:
			letter_difference = ord(second_half[i]) - ord(reverse_first_half[i])

		total_operations += letter_difference

	return total_operations

def calculate_palindrome(input_text):
	'''
		Find the middle of the string. 
		If the string is odd, the characters after the middle must be the reverse of the characters before middle.
		If the string is even, the string in the second half is the reverse of the strings in the first half.
		We can calculate distance between characters with the ord() function, to retrieve the ascii values.
	'''
	operation_count = None
	if input_text == input_text[::-1]: # is the string already a palindrome?
		return 0
	else:
		middle = len(input_text) / 2
		if len(input_text) % 2 == 1: # string is odd length
			first_half = input_text[:middle]
			second_half = input_text[middle + 1:] # discard the middle value, not needed

		else: # even
			first_half = input_text[:middle]
			second_half = input_text[middle:]

		operation_count = count_operations(first_half, second_half)
		
		if operation_count < 0:
			# if the op count is a negative number, then we have to change the first half to make the palindrome, 
			# not the second
			operation_count = count_operations(second_half, first_half)

	return operation_count

def main():
	input_text = get_input()
	for line in input_text:
		print calculate_palindrome(line)

if __name__ == '__main__':
	''' Run like so:
		cat love_input_output/input | ./love_letter_mystery.py
	'''
	main()