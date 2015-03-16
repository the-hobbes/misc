#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/filling-jars
'''

def main():
	first_line = raw_input()
	first_line = first_line.split(' ')
	n = int(first_line[0]) # the number of empty candy jars (bins)
	m = int(first_line[1]) # the number of operations  to be performed

	total = 0
	for operation in range(m):
		try:
			a, b, k = raw_input().split(' ') # a=low index, b=high index, k=value
			a = int(a)
			b = int(b)
			k = int(k)
			# fill each of the spots between b and a with the k value.
			total = total + (b - a + 1) * k
		except EOFError:
			break # end of file

	print total / n # average!

if __name__ == '__main__':
	main()