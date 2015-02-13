#!/usr/bin/python

'''
	Good reference: http://www.regular-expressions.info/refquick.html

	some common regex patterns, now in python flavor.

	The RE module provides PCRX patterns.

	Metacharacters:
		. ^ $ * + ? { } [ ] \ | ( )

	The [] metacharacters:
		Used for specifying a character class, which is a set of characters you want to match. Characters can be listed 
		individually, or specified as a range by using a -. For example, [a,b,c] is the same as [a-c]. All lowercase characters
		would be [a-z].
		- metacharacters are stripped of their special status inside a class (except for ^).
		- Typing a caret after the opening square bracket negates the character class. The result is that the character class 
		  matches any character that is not in the character class.
		  q[^x] matches qu in question. It does not match Iraq since there is no character after the q for the negated 
		  character class to match.

	The \ metacharacter 
		- Escapes metacharacters 

	Other metacharacters:
		| == the OR operator. 
		^ == Match the beginning of lines. 
				>>> print re.search('^From', 'From Here to Eternity')  
				<_sre.SRE_Match object at 0x...>
				>>> print re.search('^From', 'Reciting From Memory')
				None
		$ == The end of lines.
		+ == Match one or more occurences of the preceeding string.
				 Thus, a+ matches a, aa, aaaaaa but not an empty string.
		? == A quantifier. This means that it makes the preceding token in the regular expression optional.
				colou?r will match color and colour.
				You can write a regular expression that matches many alternatives by including more than one question mark. 
				Feb(ruary)? 23(rd)? matches February 23rd, February 23, Feb 23rd and Feb 23.
		* == Greedy quantifier. Tells the parser to match the preceding token zero or more times. 
		. == The dot matches a single character, without caring what that character is.

	Using re:
		import.re
		p = re.compile('ab*')

	Then:
		match()	Determine if the RE matches at the beginning of the string. IMPORTANT this tries to match the entire string. USE SEARCH instead.
		search()	Scan through a string, looking for any location where this RE matches.
		findall()	Find all substrings where the RE matches, and returns them as a list.
		finditer()	Find all substrings where the RE matches, and returns them as an iterator.

	match() and search() return None if no match can be found. If they are successful, a match object instance is returned, 
	containing information about the match: where it starts and ends, the substring it matched, and more.

		group()	Return the string matched by the RE
		start()	Return the starting position of the match
		end()	Return the ending position of the match
		span()	Return a tuple containing the (start, end) positions of the match

	So:
		p = re.compile('ab*')
		result = p.search('a')
		result.group()
		# prints 'a'
'''

import re

def shell_comments():
	''' match C or C++ shell comments'''
	should_pass = 'This line # contains a comment'
	should_fail = 'This line has no comment'
	should_fail_tricky = 'This line does#not contain a comment'

	pattern = re.compile('\s#') # match a '#' preceded by a whitespace anywhere in the string

	result = pattern.search(should_pass)
	print result
	result = pattern.search(should_fail)
	print result
	result = pattern.search(should_fail_tricky)
	print result

def phone_numbers():
	''' match US phone numbers'''
	should_pass = '802-922-3445'
	should_fail = '8029223445'
	should_fail_tricky = '902-2333-2323'

	#\d{3} is any three digits, and \d{4} is any 4 digits. the () aren't strictly necessary, but create groups you can retrieve with groups()
	pattern = re.compile('(\d{3})-(\d{3})-(\d{4})') 

	result = pattern.search(should_pass)
	print result
	result = pattern.search(should_fail)
	print result
	result = pattern.search(should_fail_tricky)
	print result


def scientific_notation():
	''' match scientific notation'''
	pass

def c_hex():
	''' match C-style hex'''
	pass

def ipv4_address():
	''' match ipv4 addresses'''
	should_pass = '192.168.1.1'
	should_fail = '192168.1.1'

	pattern = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$') # #\d{1,3} anything from 1 to 3 digits, ^==start, $==end

	result = pattern.search(should_pass)
	print result
	result = pattern.search(should_fail)
	print result

def mac_address():
	''' match MAC addresses'''
	pass

def main():
	# run each of the following matching functions
	shell_comments()
	phone_numbers()
	scientific_notation()
	c_hex()
	ipv4_address()
	mac_address()

if __name__ == '__main__':
	main()


