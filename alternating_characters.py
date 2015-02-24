#!/usr/bin/python
'''
	Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. 
	Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to 
	delete the characters in the string.

	Your task is to find the minimum number of required deletions.

	Input Format 
	The first line contains an integer T i.e. the number of test cases. 
	Next T lines contain a string each.

	Output Format 
	For each test case, print the minimum number of deletions required.

	Constraints

	1 <= T <= 10 
	1 <= lengthofString <= 105 

	Sample Input

	5
	AAAA
	BBBBB
	ABABABAB
	BABABA
	AAABBB
	Sample Output

	3
	4
	0
	0
	4
	Explanation

	AAAA=>A, 3 deletions
	BBBBB=>B, 4 deletions
	ABABABAB=>ABABABAB, 0 deletions
	BABABA=>BABABA, 0 deletions
	AAABBB=>AB, 4 deletions
'''

import sys, re

def get_input():
	# get the input from stdin and return it as a list of lists
	collected_input = []
	reg = re.compile('\d{1}')
	for line in sys.stdin:
		if reg.match(line):
			continue
		collected_input.append(line.strip())

	return collected_input

def process_input(text):
	# for each deletion you make, increase a counter by 1
	req_deletions = 0
	current = None
	previous = None

	for character in text:
		current = character
		if previous is None:
			previous = character
		elif current == previous:
			req_deletions += 1
			previous = character
		else:
			previous = character

	return req_deletions

def main():
	collected_input = get_input()
	for line in collected_input:
		print process_input(line)

if __name__ == '__main__':
	main()