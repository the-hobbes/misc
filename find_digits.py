#!/usr/bin/python

'''
  https://www.hackerrank.com/challenges/find-digits
'''

import sys

if __name__ == '__main__':
  T = map(int, sys.stdin.readline().split())[0]

  for _ in range(T):
    string_input = sys.stdin.readline().split()
    input_list = map(int, ''.join(letter for letter in string_input))
    int_input = int(string_input[0])
    counter = 0

    for number in input_list:
      try:
        remainder = int_input % number
        if remainder == 0:
          counter += 1 
      except ZeroDivisionError as zero:
        continue
        
    print counter
