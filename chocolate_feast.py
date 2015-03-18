#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/chocolate-feast

	N = how much money is available
	C = the cost of each chocolate
	M = for every M wrappers given back, one more chocolate is given
	T = the number of test cases

	input format = N, C, and M

	Sample IN:
		3
		10 2 5
		12 4 4
		6 2 2

	Sample OUT:
		6
		3
		5
'''

import sys

if __name__ == '__main__':
	T = map(int, sys.stdin.readline().split())[0]
	
	for _ in range(T):
		N, C, M = map(int, sys.stdin.readline().split())

		total = 0
		chocolates_purchased = N / C
		pool_of_wrappers = chocolates_purchased
		total += chocolates_purchased

		while pool_of_wrappers >= M:
			additional_chocolates = pool_of_wrappers / M
			pool_of_wrappers -= M * additional_chocolates
			pool_of_wrappers += additional_chocolates
			total += additional_chocolates

		print total
