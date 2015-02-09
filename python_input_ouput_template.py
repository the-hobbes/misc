#!/usr/bin/python
"""
	Standard I/O Template. 
"""

import sys

def mapper():

	for line in sys.stdin: # read data in from stdin
		data = line.strip().split("\t") # strip whitespace and break input into a list on tabs 
		# perform some checking and massaging of the data. Whatever your script requires
		if len(data) != 6:
			continue
		date = data[0]
		sales = data[4]
		weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
		# print the formatted results to stdout
		print '{0}\t{1}'.format(weekday, sales)

def main():
	mapper()


if __name__ == '__main__':
	main()

'''
Note about the name pattern above:

	This allows you to use the same file both as a library (by importing it) 
	or as the starting point for an application.
	This is because a special variable called __name__ which python will
	set based on whether the library is imported or run directly by the 
	interpreter.
	If run directly it will be set to __main__. If imported it will be set 
	to the library name. For example, the direct run:
		$ python hello.py
		hello, __main__
	versus the library import:
		from hello import hello
		print hello("world") 
	See:
	http://stackoverflow.com/questions/8228257/what-does-if-name-main-mean-in-python

'''