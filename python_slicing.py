'''
  How do you get every fourth element in an array, starting with the third element?
'''

test_array = [chr(x) for x in range(ord('a'), ord('z') + 1)] # create an array of the alphabet

# naive way, using range:
for item in range(2, len(test_array), 4):
  print test_array[item]

# list comprehension using range (remember list comprehensions return arrays):
print [test_array[item] for item in range(2, len(test_array), 4)]

# using slicing:
print test_array[2::4]

'''
  Reverse an array, using only slicing.
'''

print test_array[::-1]