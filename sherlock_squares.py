#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/sherlock-and-squares
'''

import sys, math

if __name__ == '__main__':
	T = map(int, sys.stdin.readline().strip())[0]

	for _ in range(T):
		# do work
		square_count = 0
		point_a, point_b = map(int, sys.stdin.readline().split())
		# square_count += math.sqrt(number).is_integer()
		for number in range(point_a, point_b + 1):
			square_count += math.sqrt(number).is_integer()

		print square_count
