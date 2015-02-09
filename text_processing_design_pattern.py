#!/usr/bin/env python

'''
	Text processing design pattern.
	How to process a stream of sorted input text, and total the values for each group.

	Example input: 
		Moscow	10.45
		Moscow	12.45
		Moscow	35.65
		Berlin	320.33
		Berlin	23.34
		Hamburg	12.43

	To calculate totals for each group, we need to keep track of:
		- current cost
		- total sales
		- current city 
		- previous city (so we know when we are changing cities)

'''

import sys


def reducer():
	# remember, the data comes into the reducer in order, so we can process it
	# as such. 

	sales_total = 0
	old_key = None

	for line in sys.stdin:
		data = line.strip().split('\t') # remove whitespace and break input into list on tab character
		if len(data) != 2:
			continue # skip arrays that don't meet our requirments, whatever they are

		this_key, this_sale = data # give the values of data[0] and data[1] to variables

		if old_key and (old_key != this_key): 
			# check if old_key is even set- if not, this is the first line
			# if the old_key is set and it is different that the key we've just read in, then the key has just changed (eg moscow to berlin )
			print old_key + "\t" + sales_total # since we've just changed keys, print out the total value of the key we've finished
			sales_total = 0 # reset sales total so it can be used with a new key

		# for every row we process, we set old_key to the key we are working on
		old_key = this_key
		# then, we add the sales value for that key to the running total
		sales_total += this_sale
		# loop back to the beginning and process the next line in stdin

	# we aren't done, because we haven't process the last key- we need to output that data
	if old_key != None:
		print old_key + "\t" + sales_total
	# this is because the store doesn't change when the last is processed, and thus won't trigger the print statement on line 43
	# we must do that manually


def main():
	reducer()

if __name__ == '__main__':
  main()