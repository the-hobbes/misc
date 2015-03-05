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
		The maximum number of topics a 2 person team can know is 5 in this case.
		Only 2 teams can achieve this. 
		Thus, the output is:
			5
			2

	Note: in the above example, the number of possible combinations would be n choose k,
	which is 4 choose 2 in this case (for a total of 6 combinations).
'''

import itertools

# def person_comparer(person_1, person_2):
# 	# perform bitwise-or on two people, and return an integer array of the result
# 	comparison = []
# 	for i in range(len(person_1)):
# 		comparison.append( int(person_1[i]) | int(person_2[i]) ) # bitwise OR

# 	return comparison

def sum_string(string):
	return sum(int(character) for character in string if character.isdigit())

def find_max_topics(n, m, people):
	# find the maximum number of topics a 2 person team can know
	topics_known = {}
	max_value = 0

	for person in people: # dict of the string representing the person and the value of their known topics
		topics_known[person] = sum_string(person)
		if (topics_known[person] > max_value and topics_known[person] <= m):
			max_value = topics_known[person]


	for item in itertools.combinations(topics_known, 2): # go through every combination of 2 people
		print item


	# TODO(pheven): calculate the maximum possible value of any two teams, and then find all the teams 
	# with that value.


def find_top_teams():
	# find the number of teams that know the maximum number of topics
	pass

def main():
	first_line = raw_input()
	first_line = first_line.split(' ')
	n = int(first_line[0])
	m = int(first_line[1])

	people = [raw_input() for _ in range(0,n)]
	
	find_max_topics(n, m, people)
	

if __name__ == '__main__':
	main()