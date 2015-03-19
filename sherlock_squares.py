#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/sherlock-and-squares
'''

import sys, math

if __name__ == '__main__':
	T = map(int, sys.stdin.readline().split())[0]

	for _ in range(T):
		# do work
		low, high = map(int, sys.stdin.readline().split())

		count_squares = int( math.floor(math.sqrt(high)) - math.ceil(math.sqrt(low)) + 1)
		print count_squares
