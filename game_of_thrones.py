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

from collections import Counter

def find_palindrome(input_string):
	'''
		determine if any anagram (permutation of the input_string) is a palindrome by counting the number of
		times each letter occurs. A palindrome will have either all even occurences of letters, or all even 
		occurences and one odd occurence. 

		Thus, if more than 1 odd occurence is located, the string isn't a palindrome.
	'''
	odd_counts = 0
	c = Counter(input_string)
	
	for key in c:
		if c[key] % 2 == 1: # check if a count is odd
			odd_counts += 1 # if it is, increment the number of odd counts we've seen
			if odd_counts > 1: # if we've seen more than one, the input string isn't a palindrome
				return False

	return True # the input string is a palindrome

def main():
	input_string = raw_input()
	found = find_palindrome(input_string)

	if found:
		print 'YES'
	else:
		print 'NO'

if __name__ == '__main__':
	main()