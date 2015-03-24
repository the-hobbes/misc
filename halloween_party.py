#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/halloween-party
'''

import sys

if __name__ == '__main__':
	K = map(int, sys.stdin.readline().split())[0]

	for _ in range(K):
		cuts = map(int, sys.stdin.readline().split())[0]
		first_half = cuts / 2
		second_half = cuts - first_half
		
		print first_half * second_half
	