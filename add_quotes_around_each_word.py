#! /usr/bin/python

"""Add quotes around each word in a comma separated file."""

import sys


def addquotes():
  for line in sys.stdin:
    data = line.strip().split(",")
    for word in data:
      print "'%s'," % word    


addquotes()
