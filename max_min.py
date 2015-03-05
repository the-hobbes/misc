#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/angry-children

	Sort the list
	Pull out the lowest k integers from the list, and compute the unfairness:
		max(k1, k2, ... k) - min(k1, k2, ... k)
'''

def compute_min_diff(n, k, candies):
	'''
		You can profile your program by doing something like this:
			cat sample_input | python -m cProfile max_min.py
		to identify the bottlenecks.
	'''
	min_diff = None

	for i in range(n - k):
		diff = candies[(i + k) - 1] - candies[i] # since list is sorted, max is last element and min is first
		if min_diff == None or diff < min_diff: # mindiff == none because python treats 0 as false
			min_diff = diff

	return min_diff

def main():
	n = input() # the number of items in the list, passed in on stdin
	k = input() # the number of integers from the list we want to select

	candies = [input() for _ in range(0,n)]
	candies.sort()

	min_diff = compute_min_diff(n, k, candies)

	print min_diff

if __name__ == '__main__':
	main()

# print compute_min_diff(4, 3, None)