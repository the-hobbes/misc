#!/usr/bin/python

'''
  https://www.hackerrank.com/challenges/cavity-map
'''
import sys

def check_adjacent_points(point_row, point_column, grid):
  # all positions
  above_left = None
  above = None
  above_right = None
  right = None
  left = None
  below_left = None
  below = None
  below_right = None

  print grid[point_row][point_column]

if __name__ == '__main__':
  n = map(int, sys.stdin.readline().split())[0]
  grid = [] # 2-dimensional list, accessed by: grid[row][column]
  for _ in range(n):
    line = list(sys.stdin.readline().strip())
    int_line = []
    for i in line: # this is clunky
      int_line.append(map(int, i))
    grid.append(int_line)

  check_adjacent_points(0, 0, grid) # also clunky
