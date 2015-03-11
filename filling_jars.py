#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/filling-jars
'''

def do_work(n, m, operations):
	candy_jars = [0] * n
	
	for operation in operations:
		low = operations[operation][0]
		high = operations[operation][1]
		value = operations[operation][2]

		for i in range(int(low) - 1, int(high)):
			candy_jars[i] += int(value)

	print sum(candy_jars) / n

def main():
	first_line = raw_input()
	first_line = first_line.split(' ')
	n = int(first_line[0]) # the number of empty candy jars (bins)
	m = int(first_line[1]) # the number of operations  to be performed

	operations = {}
	for operation in range(n):
		try:
			operations[operation] = raw_input().split(' ') # a=low index, b=high index, k=value
		except EOFError:
			break # end of file

	do_work(n, m, operations)

if __name__ == '__main__':
	main()