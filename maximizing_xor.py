'''
	https://www.hackerrank.com/challenges/maximizing-xor

	XOR: Exclusive disjunction or exclusive or is a logical operation that outputs true whenever both inputs 
	differ (one is true, the other is false).

	For example:
	    0101 (decimal 5)
	XOR 0011 (decimal 3)
	  = 0110 (decimal 6)

	Given two integers, L and R, find the maximal values of A xor B, where A and B satisfies the 
	following condition:

		L <= A <= B <= R

	Input Format 
	The input contains two lines, L is present in the first line and R in the second line.

	Constraints
	1 <= L <= R <= 103

	Output Format 
	The maximal value as mentioned in the problem statement.

	Sample Input#00
	1
	10

	Sample Output#00
	15

	Sample Input#01
	10
	15

	Sample Output#01
	7
'''

def maxXor(l, r):
	maximal_value = None

	l, r = int(l), int(r)

	for i in range(l, r + 1):
		for j in range(l, r + 1):
			current_value = i ^ j # ^ is the xor operator
			if current_value >= maximal_value or not maximal_value:
				maximal_value = current_value

	return maximal_value

_l = int(raw_input());


_r = int(raw_input());

# print maxXor(10, 15);
print maxXor(_l, _r);
