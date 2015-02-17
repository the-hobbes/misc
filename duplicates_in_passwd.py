#!/usr/bin/python

'''
  Search for and print all entries in /etc/passwd with duplicate uuids.
'''

import sys

def read_passwd():
  PASSWD_FILE = '/etc/passwd'
  with open(PASSWD_FILE) as f:
    contents = f.readlines()

  return contents

def get_key(item):
  # this function constructs a key to sort each line in the passwd file on.
  # item[2] is the uuid.
  key = ''
  if item[0] != '#': # ignore comments
    item = item.split(':') # passwd is colon delimited
    key = item[2]
  
  return key

def find_duplicates(contents):
  # sort the file first
  sorted_contents = sorted(contents, key=get_key)

  previous_item = None
  current_item = None

  # now loop through it, printing duplicates
  for item in sorted_contents:
    if item[0] != '#': # ignore comments
      item = item.split(':')
      if not previous_item: # set up the previous_item the first time we run through the loop
        previous_item = item
        continue
        
      # compare the current item with the previous item to see if the uuid's match
      current_item = item
      if previous_item[2] == current_item[2]:
        print 'DUPLICATE ENTRY: ' + ':'.join(current_item)

      previous_item = current_item
      current_item = None


def main():
  # read in file
  contents = read_passwd()
  # search file for duplicates and print them
  find_duplicates(contents)

if __name__ == '__main__':
  main()