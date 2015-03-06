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

# def sum_string(string):
# 	return sum(int(character) for character in string if character.isdigit())

def person_comparer(person_1, person_2):
	# perform bitwise-or on two people, and return an integer array of the result
	return [int(a) | int(b) for a,b in itertools.izip(person_1, person_2)]
	
def find_max_knowledge(n, m, people):
	# compute bitwise comparison of every pair of teams
	teams = {}
	for item in itertools.combinations(people, 2):
		teams[item] = person_comparer(item[0], item[1])

	# determine the max knowledge value
	max_knowledge = 0
	team_values = {}
	for team in teams:
		combined_knowledge = sum(teams[team])
		team_values[team] = combined_knowledge
		if combined_knowledge >= max_knowledge:
			max_knowledge = combined_knowledge
	
	return max_knowledge, team_values

def find_top_teams(max_knowledge, team_values):
	# determine how many teams have that max knowledge
	top_teams = 0
	for team in team_values:
		if team_values[team] == max_knowledge:
			top_teams += 1

	return top_teams

def main():
	first_line = raw_input()
	first_line = first_line.split(' ')
	n = int(first_line[0])
	m = int(first_line[1])

	people = [raw_input() for _ in range(0,n)]
	
	max_knowledge, team_values = find_max_knowledge(n, m, people)
	top_teams = find_top_teams(max_knowledge, team_values)

	print max_knowledge
	print top_teams
	

if __name__ == '__main__':
	main()