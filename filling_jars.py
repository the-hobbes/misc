#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/filling-jars
'''

import sys

def main():
	# map the call to int() to the result of the call to split, for the two values in the first line of input
	n, m = map(int, sys.stdin.readline().split())

	total = 0
	for _ in range(m):
		# do that same map, but for three items split instead of two
		a, b, k = map(int, sys.stdin.readline().split())
		# fill each of the spots between b and a with the k value.
		total = total + (b - a + 1) * k
		
	print total / n # average!

if __name__ == '__main__':
	main()