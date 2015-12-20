#!/usr/bin/python

'''
	Script to do string replacement of a cell in a file, respecting case.
	Find string pattern w/something like:
		grep -PRn '\bfindme\b' some/other/directory

	Usage:
		cat /path/to/file | ./caseSensitiveStringReplacement.py > /dest/file
'''

import sys
import re

OLD_CELL = 'old'
NEW_CELL = 'new'


def case_sensitive_replace(string, old, new):
	'''
		replace occurrences of old with new, within string
		replacements will match the case of the text it replaces
	'''
	def repl(match):
		current = match.group()
		result = ''
		all_upper = True
		for i, c in enumerate(current):
			if i >= len(new):
				break
			if c.isupper():
				result += new[i].upper()
			else:
				result += new[i].lower()
				all_upper = False
		# append any remaining characters from new
		if all_upper:
			result += new[i+1:].upper()
		else:
			result += new[i+1:].lower()
		return result

	regex = re.compile(re.escape(old), re.I)
	return regex.sub(repl, string)


def main():
	for line in sys.stdin:
		if line.lower().find(OLD_CELL) != -1:
			lower_line = case_sensitive_replace(line, OLD_CELL, NEW_CELL)
			all_replaced = case_sensitive_replace(lower_line,
												  OLD_CELL.upper(),
												  NEW_CELL.upper())
			line = all_replaced
		sys.stdout.write(line)  # preserve formatting

if __name__ == '__main__':
	main()
