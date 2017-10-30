import profile

# Sort an array of numbers such that s1 <= s2 >= s3 <= s4 ...
master = [12, 22, 6, 8, 3, 7, 7, 90, 0, 134]

def solution_1():
  # find min & max, remove them and add them to output
  # O(N^2)
  u = master[:]
  s = []
  while len(u) > 0:
    low = u.index(min(u))
    s.append(u[low])
    del(u[low])
    high = u.index(max(u))
    s.append(u[high])
    del(u[high])
    
  return s

def solution_2():
  # sort, then remove alternatively from front and back
  # O(N ln N)
  u = master[:]
  s = []
  u.sort()
  while len(u) > 0:
    s.append(u.pop(0))
    s.append(u.pop(-1))

  return s

def solution_3():
  # Find the median, cut the input into less-than & greater-or-equal-to the
  # median, then output alternating from the the two parts.
  # O(N)
  u = master[:]
  s = []

  u.sort()
  med = len(u) / 2
  low = u[0:med]
  high = u[med:]
  while (len(low) > 0) or (len(high) > 0):
    s.append(low.pop(0))
    s.append(high.pop(-1))  

  return s

print solution_1()
print solution_2()
print solution_3()

# profile.run('print(solution_1())')
# profile.run('print(solution_2())')
