#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/angry-professor
'''

import sys

if __name__ == '__main__':
	T = map(int, sys.stdin.readline().split())[0] # number of test cases
	
	# there are 2 times the number of lines as there are test cases

	for _ in range(T): 
		on_time = 0
		N, K = map(int, sys.stdin.readline().split())
		students = map(int, sys.stdin.readline().split())
		for student in students:
			if student <=0: # the student is on time
				on_time += 1

		# if there are K or more students on time, the class isn't cancelled
		if on_time >= K:
			print 'NO'
		else:
			print 'YES'
