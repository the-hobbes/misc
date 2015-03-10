#!/usr/bin/python

'''
	ACM ICPC Team
	https://www.hackerrank.com/challenges/acm-icpc-team

	Input format:
	First line contains 2 integers N and M, where
		N is the number of people 
		M is the number of topics
	N lines follow
		each line contains a binary string of length M
		1 indicates the person knows a topic
		0 indicates the person does not
	
	Example:
		4 5
		10101 => person 1 knows topics 1,3, and 5. 
		11100 => person 2 knows topics 1,2, and 3.
		11010 => person 3 knows topics 1,2, and 4.
		00101 => person 4 knows topics 3 and 5.

	Therefore:
		person 1 and person 3 together know all 5 topics.
		person 4 and person 4 together know all 5 topics.
		(The maximum number of topics a 2 person team can know is 5 in this case.)
		Only 2 teams can achieve this. 
		Thus, the output is:
			5
			2

	Note: in the above example, the number of possible combinations would be n choose k,
	which is 4 choose 2 in this case (for a total of 6 combinations).
'''

import itertools

def compute_values_itertools(n, m, people):
	format_string = '{0:0%sb}' % m
	best_value, team_count = 0, 0

	for combination in itertools.combinations(people, 2):
		bitwise_or = int(combination[0], 2) | int(combination[1], 2)
		count = format_string.format(bitwise_or).count('1')
		if count > best_value : 
			best_value = count 
			team_count = 1
		elif count == best_value:
			team_count += 1

	print '--------- using itertools... -------------'
	print best_value, '\n', team_count

def compute_values_nested(n, m, people):
	format_string = '{0:0%sb}' % m
	best_value, team_count = 0, 0

	for i in range(0, n):
		for j in range(i + 1, n):
			bitwise_or = int(people[i], 2) | int(people[j], 2)
			count = format_string.format(bitwise_or).count('1')
			if count > best_value : 
				best_value = count 
				team_count = 1
			elif count == best_value:
				team_count += 1

	print '--------- using nested... -------------'
	print best_value, '\n', team_count

def main():
	first_line = raw_input()
	first_line = first_line.split(' ')
	n = int(first_line[0])
	m = int(first_line[1])

	people = [raw_input() for _ in range(0,n)]
	
	compute_values_itertools(n, m, people)
	print '\n'
	compute_values_nested(n, m, people)
	

if __name__ == '__main__':
	main()