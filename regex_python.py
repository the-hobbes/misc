#!/usr/bin/python

'''
	TODO: complete tutoria here: http://www.regular-expressions.info/quickstart.html
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

	Using re:
		import.re
		p = re.compile('ab*')

	Then:
		match()	Determine if the RE matches at the beginning of the string.
		search()	Scan through a string, looking for any location where this RE matches.
		findall()	Find all substrings where the RE matches, and returns them as a list.
		finditer()	Find all substrings where the RE matches, and returns them as an iterator.

	match() and search() return None if no match can be found. If they’re successful, a match object instance is returned, 
	containing information about the match: where it starts and ends, the substring it matched, and more.

		group()	Return the string matched by the RE
		start()	Return the starting position of the match
		end()	Return the ending position of the match
		span()	Return a tuple containing the (start, end) positions of the match

	So:
		p = re.compile('ab*')
		result = p.match('a')
		result.group()
		# prints 'a'
'''

import re

def main():
	pass

if __name__ == '__main__':
	main()