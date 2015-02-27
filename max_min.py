#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/angry-children

	Sort the list
	Pull out the lowest k integers from the list, and compute the unfairness:
		max(k1, k2, ... k) - min(k1, k2, ... k)
'''

# NOTE: This solution is incredibly slow and unnecessary
# def compute_min_diff(n, k, candies):
# 	# for every three possible combination of numbers in candies, compute the min diff. 
# 	# save only the smallest min diff
# 	min_diff = None

# 	# yay for itertools, saving us from k nested loops
# 	from itertools import combinations
# 	all_combinations = set(combinations(candies, k))

# 	for combo in all_combinations:
# 		diff = max(combo) - min(combo)
# 		if not min_diff or diff < min_diff:
# 			min_diff = diff

# 	return min_diff

def compute_min_diff(n, k, candies):
	min_diff = None

	for i in range(len(candies)):
		subgroup = candies[i: i + k]
		if len(subgroup) ==  k:
			diff = subgroup[-1] - subgroup[0] # since list is sorted, max is last element and min is first
			if not min_diff or diff < min_diff:
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