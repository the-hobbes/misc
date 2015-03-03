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

def check_palindrome(string):
	# check to see if a given string is a palindrome
	if string == string[::-1]:
		return True

	return False

def check_anagram(string):
	# find all possible anagrams, by generating all permutations of the given string

	from itertools import permutations # using itertools permutations library
	all_permutations = [''.join(perm) for perm in permutations(string)] # join the tuples returned into a list

	return all_permutations

def find_palindrome(string):

	# find all permutations (all possible anagrams)
	all_permutations = check_anagram(string)
	print all_permutations
	# determine if any permutation is a palindrome
	for item in all_permutations:
		contains_palindrome = check_palindrome(item)
		if contains_palindrome:
			return True

	return False

def main():
	string = raw_input()
	found = False

	found = find_palindrome(string)

	if found:
		print 'YES'
	else:
		print 'NO'

if __name__ == '__main__':
	main()