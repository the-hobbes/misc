#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/game-of-thrones

	Robert ... needs a key that is an anagram of a certain palindrome string.	
	The king has a string composed of lowercase English letters. Help him figure 
	out if any anagram of the string can be a palindrome or not

	Input Format 
	A single line which contains the input string

	Constraints 
	1<=length of string <= 10^5 
	Each character of the string is a lowercase English letter.

	Output Format 
	A single line which contains YES or NO in uppercase.

	Anagram:
	An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce 
	a new word or phrase, using all the original letters exactly once; for example Torchwood can be rearranged 
	into Doctor Who.

	Palindrome:
	A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or 
	forward.
'''

from itertools import permutations # using itertools permutations library

def check_palindrome(input_string):
	# check to see if a given input_string is a palindrome by reversing and comparing
	return input_string == input_string[::-1]

def find_palindrome(input_string):
	# determine if any anagram (permutation of the input_string) is a palindrome. 
	for permutation in set(permutations(input_string)):
		if check_palindrome(permutation): # check if a given anagram is a palindrome
			return True # exit quickly if we find a match

	return False

def main():
	input_string = raw_input()
	found = False

	found = find_palindrome(input_string)

	if found:
		print 'YES'
	else:
		print 'NO'

if __name__ == '__main__':
	main()